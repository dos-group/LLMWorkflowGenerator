#!/usr/bin/env python3

####################################################################################################

from aioconsole import aprint, ainput
from aiohttp import ClientSession, MultipartReader
from asyncio import run
from json import loads
from os import environ
from time import time_ns
from traceback import format_exc

####################################################################################################

class Argument:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def format(self):
        return self.name + ": " + self.type

####################################################################################################

class Function:
    def __init__(self, name, arguments, return_type, callback):
        self.name = name
        self.arguments = arguments
        self.return_type = return_type
        self.callback = callback

    def format_arguments(self):
        return ", ".join(map(lambda argument: argument.format(), self.arguments))

    def format_return_type(self):
        if self.return_type is None or len(self.return_type) == 0:
            return ": void"

        return ": " + self.return_type

    def format(self):
        return "function " + self.name + "(" + self.format_arguments() + ")" + self.format_return_type()

####################################################################################################

def stub_function(name, return_value = None):
    def wrapper(*args):
        print('Execute "{}" and arguments {}'.format(name, ', '.join(map(lambda argument: '"' + str(argument) + '"', args))))

        return return_value

    return wrapper

####################################################################################################

FUNCTIONS = [
    Function(
        "find_file_id",
        [
            Argument("expression", "String"),
        ],
        "Integer|null",
        stub_function("find_file_id", 1),
    ),
    Function(
        "find_contact_id",
        [
            Argument("expression", "String"),
        ],
        "Integer|null",
        stub_function("find_contact_id", 1),
    ),
    Function(
        "find_contact_email",
        [
            Argument("contact_id", "Integer"),
        ],
        "String|null",
        stub_function("find_contact_email", "john.doe@example.com"),
    ),
    Function(
        "play_voice",
        [
            Argument("text", "String"),
        ],
        None,
        stub_function("play_voice"),
    ),
    Function(
        "ask_question",
        [
            Argument("question", "String"),
        ],
        "String",
        stub_function("ask_question", "Hello"),
    ),
    Function(
        "play_audio_file",
        [
            Argument("file", "File"),
        ],
        None,
        stub_function("play_audio_file"),
    ),
    Function(
        "send_email",
        [
            Argument("email", "String"),
            Argument("subject", "String"),
            Argument("text", "String"),
            Argument("attachments", "Collection<Integer>"),
        ],
        None,
        stub_function("send_email"),
    ),
    Function(
        "receive_email",
        [
            Argument("email", "String"),
            Argument("subject", "String"),
            Argument("text", "String"),
            Argument("attachments", "Collection<Integer>"),
        ],
        None,
        stub_function("receive_email"),
    ),
    Function(
        "print_screen",
        [
            Argument("text", "String"),
        ],
        None,
        stub_function("print_screen"),
    ),
    Function(
        "get_temperature",
        [
        ],
        "Integer",
        stub_function("get_temperature", 37),
    ),
    Function(
        "shell",
        [
            Argument("command", "String"),
        ],
        "String",
        stub_function("shell", "Document 0\nDocument 1\nDocument 2"),
    ),
]

functions_prompt = "\n".join(
    map(
        lambda function: function.format(),
        FUNCTIONS,
    )
)

####################################################################################################

def format_content(message):
    return """
You have the following application programming interface:

{functions_prompt}

Write Python 3 code only, which uses the application programming interface for the instruction
"{message}"
""".format(message=message, functions_prompt=functions_prompt)

####################################################################################################

async def request(url, key, model, prompt):
    await aprint("####################################################################################################\n")
    await aprint(functions_prompt)
    await aprint("\n####################################################################################################\n")

    request_headers = {
        "Authorization": "Bearer " + key,
    }

    request_body={
        "model": model,
        "messages": [
            {'role': 'system', 'content': 'You are a Python 3 code generator.'},
            {"role": "user", "content": format_content(prompt)},
        ],
        "stream": True,
    }

    start = time_ns()
    time_to_first_token_ns = None

    await aprint(url, model, prompt)
    await aprint("\n####################################################################################################\n")

    async with ClientSession() as session:
        async with session.post(url, headers=request_headers, json=request_body) as response:
            output = ""

            async for chunk in response.content:
                if chunk:
                    string = chunk.decode("utf-8").lstrip("data: ").strip()
                    if len(string) == 0:
                        continue

                    if time_to_first_token_ns is None:
                        time_to_first_token_ns = time_ns() - start

                    if string == "[DONE]":
                        break

                    data = loads(string, strict=False)

                    if 'content' in data["choices"][0]["delta"]:
                        output = output + data["choices"][0]["delta"]["content"]
                    else:
                        break
                else:
                    break

            marker = "```"
            left_marker = marker + "python"
            right_marker = "```"

            output = output.strip("\n\r ")
            code = output[output.index(left_marker) + len(left_marker):output.rindex(right_marker)]

            elapsed_s = (time_ns() - start) / (10 ** 9)
            time_to_first_token_ms = time_to_first_token_ns / (10 ** 6)

            await aprint("\n")
            await aprint(output)
            await aprint("\n####################################################################################################\n")

            await aprint(code)
            await aprint("\n####################################################################################################\n")

            try:
                exec(
                    code,
                    {
                        function.name:function.callback for function in FUNCTIONS
                    },
                    {},
                )

                await aprint("\n####################################################################################################\n")

                await aprint("Success (total {}s, ttft {}ms)".format(elapsed_s, time_to_first_token_ms))
            except Exception as e:
                await aprint("Failed (total {}s, ttft {}ms)".format(elapsed_s, time_to_first_token_ms))
                await aprint(format_exc())

            await aprint("\n####################################################################################################\n")

####################################################################################################

DEFAULT_MODEL = "gpt-4o-mini"

####################################################################################################

async def main():
    await request(
        "https://api.openai.com/v1/chat/completions",
        environ["OPENAI_KEY"],
        environ.get("MODEL", DEFAULT_MODEL),
        await ainput(),
    );

####################################################################################################

run(main())
