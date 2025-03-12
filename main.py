#!/usr/bin/env python3

####################################################################################################

from aioconsole import aprint, ainput
from aiohttp import ClientSession, MultipartReader
from json import loads
from os import environ, listdir, path, get_terminal_size
from random import randint
from traceback import format_exc
from inspect import getfullargspec
import asyncio
import subprocess
import time

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

class PythonFunction:
    def __init__(self, name, function):
        self.__name = name
        self.__function = function

    def callback(self):
        return self.function

    def format(self):
        specification = getfullargspec(self.__function)

        arguments = ", ".join(
            map(
                lambda argument_key: argument_key + ": " + specification.annotations[argument_key],
                specification.args,
            )
        )

        return_type = specification.annotations["return"]
        if return_type is None:
            return_type = "void"

        return "function " + self.__name + "(" + arguments + "): " + return_type

####################################################################################################

def stub_function(name, return_value = None):
    def wrapper(*args):
        print('Execute "{}" and arguments {}'.format(name, ', '.join(map(lambda argument: '"' + str(argument) + '"', args))))

        return return_value

    return wrapper

####################################################################################################

def find_file(expression):
    directory = "files"

    for file_name in listdir(directory):
        if not path.isfile(path.join(directory, file_name)):
            continue

        if expression not in file_name:
            continue

        return file_name

    return None

def find_all_audio_files():
    directory = "files"

    return [
        f for f in listdir(directory) if path.isfile(path.join(directory, f))
    ]

def play_audio_file(file_path):
    result = subprocess.run(
        ["termux-media-player", "play", path.join("files", file_path)],
        text=True,
        check=True,
        capture_output=True,
    )

    print(result.stdout)

def stop_audio_player():
    result = subprocess.run(
        ["termux-media-player", "stop"],
        text=True,
        check=True,
        capture_output=True,
    )

    print(result.stdout)

def sleep(seconds: 'Integer') -> None:
    time.sleep(seconds)

print(PythonFunction("sleep", sleep).format())

####################################################################################################

FUNCTIONS = [
    Function(
        "find_file",
        [
            Argument("expression", "String"),
        ],
        "String|null",
        find_file,
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
            Argument("filePath", "String"),
        ],
        None,
        play_audio_file,
    ),
    Function(
        "stop_audio_player",
        [],
        None,
        stop_audio_player,
    ),
    Function(
        "sleep",
        [
            Argument("seconds", "Integer")
        ],
        None,
        sleep,
    ),
    Function(
        "send_email",
        [
            Argument("email", "String"),
            Argument("subject", "String"),
            Argument("text", "String"),
            Argument("attachments", "Collection<String>"),
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
            Argument("attachments", "Collection<String>"),
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
    Function(
        "find_files",
        [
            Argument("expression", "String"),
        ],
        "Collection<String>",
        stub_function("find_files", [0, 1, 2, 3, 4]),
    ),
    Function(
        "find_all_audio_files",
        [],
        "Collection<String>",
        find_all_audio_files,
    ),
    Function(
        "generate_random_number",
        [
            Argument("minimum", "Integer"),
            Argument("maximum", "Integer"),
        ],
        "Integer",
        lambda x, y: randint(x, y),
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

Write a Python 3 function, which uses the provided application programming interface for the instruction
"{message}"

Afterwards, execute the previously written Python 3 function. Do not use other functions, only those provided by the given application programming interface.
""".format(message=message, functions_prompt=functions_prompt)

####################################################################################################

async def print_separator(newlines = 0):
    await aprint(str(get_terminal_size().columns * "#") + str(newlines * "\n"))

####################################################################################################

async def request(url, key, model, temperature, prompt):
    await print_separator(0)
    await aprint(functions_prompt)
    await print_separator(0)

    request_headers = {}

    if key is not None and len(key) > 0:
        request_headers["Authorization"] = "Bearer " + key

    request_body={
        "model": model,
        "messages": [
            {'role': 'system', 'content': 'You are a Python 3 code generator.'},
            {"role": "user", "content": format_content(prompt)},
        ],
        "stream": True,
    }

    if temperature is not None:
        request_body["temperature"] = float(temperature)

    start = time.time_ns()
    time_to_first_token_ns = None

    await aprint(url, model, temperature, prompt)
    await print_separator(0)

    async with ClientSession() as session:
        async with session.post(url, headers=request_headers, json=request_body) as response:
            output = ""

            async for chunk in response.content:
                if chunk:
                    string = chunk.decode("utf-8").lstrip("data: ").strip()
                    if len(string) == 0:
                        continue

                    if time_to_first_token_ns is None:
                        time_to_first_token_ns = time.time_ns() - start

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

            elapsed_s = (time.time_ns() - start) / (10 ** 9)
            time_to_first_token_ms = time_to_first_token_ns / (10 ** 6)

            await aprint(output)
            await print_separator(0)

            await aprint(code)
            await print_separator(0)

            try:
                exec(
                    code,
                    {
                        function.name:function.callback for function in FUNCTIONS
                    },
                    {},
                )

                await print_separator(0)

                await aprint("Success (total {}s, ttft {}ms)".format(elapsed_s, time_to_first_token_ms))
            except Exception as e:
                await aprint("Failed (total {}s, ttft {}ms)".format(elapsed_s, time_to_first_token_ms))
                await aprint(format_exc())

            await print_separator(0)

####################################################################################################

DEFAULT_ENDPOINT_URL = "https://api.openai.com/v1/chat/completions"
DEFAULT_MODEL_NAME = "gpt-4o-mini"
DEFAULT_MODEL_TEMPERATURE = 0.0

####################################################################################################

async def main():
    await request(
        environ.get("ENDPOINT_URL", DEFAULT_ENDPOINT_URL),
        environ.get("ENDPOINT_KEY", None),
        environ.get("MODEL_NAME", DEFAULT_MODEL_NAME),
        environ.get("MODEL_TEMPERATURE", DEFAULT_MODEL_TEMPERATURE),
        await ainput(),
    );

####################################################################################################

asyncio.run(main())
