#!/usr/bin/env python3

####################################################################################################

from copy import deepcopy
from inspect import getfullargspec
from json import dumps, JSONEncoder, loads
from os import environ, listdir, path, get_terminal_size
from random import randint, seed
from traceback import format_exc
from typing import Collection,  get_origin, get_args
import requests
import subprocess
import time

####################################################################################################

def request_chat_completions(url, model, role, key, prompt, temperature):
    request_headers = {}

    if key:
        request_headers["Authorization"] = "Bearer " + key

    request_body = {
        "model": model,
        "messages": [],
        "stream": True,
    }

    if role:
        request_body["messages"].append(
            {"role": "system", "content": "You are a Python 3 code generator."}
        )

    request_body["messages"].append(
        {"role": "user", "content": prompt},
    )

    if temperature is not None:
        request_body["temperature"] = float(temperature)

    start_time = time.time_ns()
    time_to_first_token_ns = None
    output = ""

    response = requests.post(url, headers=request_headers, json=request_body, stream=True)

    if response.status_code != 200:
        raise Exception("Status is not 200")

    for chunk in response.iter_lines():
        if chunk:
            string = chunk.decode("utf-8").lstrip("data: ").strip()
            if not string:
                continue

            if time_to_first_token_ns is None:
                time_to_first_token_ns = time.time_ns() - start_time

            if string == "[DONE]":
                break

            data = loads(string, strict=False)

            if 'content' in data["choices"][0]["delta"]:
                output += data["choices"][0]["delta"]["content"]
            else:
                break

    elapsed_s = (time.time_ns() - start_time) / (10 ** 9)
    time_to_first_token_ms = time_to_first_token_ns / (10 ** 6) if time_to_first_token_ns else None

    return {
        "output": output,
        "elapsed_s": elapsed_s,
        "time_to_first_token_ms": time_to_first_token_ms,
    }

####################################################################################################

class Function:
    def __init__(self, callable, name = None, argument_types = None, return_type = None):
        self.__callable_specification = getfullargspec(callable)
        self.__callable = callable
        self.__name = name or callable.__name__

        self.__argument_types = argument_types
        if argument_types is None:
            context_filtered_argument_keys = [*self.__callable_specification.args]
            if self.has_context():
                del context_filtered_argument_keys[0]

            self.__argument_types = {
                argument_key:self.__callable_specification.annotations[argument_key] for argument_key in context_filtered_argument_keys
            }

        self.__return_type = return_type
        if "return" in self.__callable_specification.annotations:
            self.__return_type = self.__callable_specification.annotations["return"]

    @property
    def name(self):
        return self.__name

    @property
    def callable(self):
        return self.__callable

    @property
    def argument_types(self):
        return self.__argument_types

    def has_context(self):
        return len(self.__callable_specification.args) > 0 and self.__callable_specification.args[0] == "context"

    @property
    def return_type(self):
        return self.__return_type

    def stub(name, return_value = None):
        def wrapper(*args):
            print('Execute "{}" and arguments {}'.format(name, ', '.join(map(lambda argument: '"' + str(argument) + '"', args))))

            return return_value

        return wrapper

####################################################################################################

class FunctionSignatureFormatter:
    def format_type(self, type):
        if type is None:
            return "void"

        if isinstance(type, str):
            return type

        if get_origin(type) is None:
            return str(type)

        if get_origin(type).__name__ == 'Collection':
            types = ", ".join(
                map(
                    lambda forward_argument: forward_argument.__forward_arg__, get_args(type)
                )
            )

            return "Collection<" + types + ">"

        return str(type)

    def format(self, function):
        specification = getfullargspec(function.callable)

        arguments = ", ".join(
            map(
                lambda argument_type_key: argument_type_key + ": " + self.format_type(function.argument_types[argument_type_key]),
                function.argument_types,
            )
        )

        return_type = self.format_type(function.return_type)

        return "function " + function.name + "(" + arguments + "): " + return_type

####################################################################################################

class FunctionTable:
    def __init__(self, signature_formatter):
        self.__signature_formatter = signature_formatter
        self.__functions = {}

    def register(self, callable, **kwargs):
        function = Function(callable, **kwargs)

        if function.name in self.__functions:
            raise Exception("Function name is already in use")

        self.__functions[function.name] = function

    def format_prompt_specification(self):
        return "\n".join(
            map(
                self.__signature_formatter.format,
                self.__functions.values(),
            )
        )

    def evaluate(self, code, context = None, tracing = False):
        if context is None:
            context = {}

        result = {
            "context": context,
        }

        if tracing is True:
            result["trace"] = []

        exec(
            code,
            {
                function.name:self.__create_callable(function, result) for function in self.__functions.values()
            },
            {},
        )

        return result

    def __create_callable(self, function, result):
        def callable(*args, **kwargs):
            trace = {}

            if "trace" in result:
                trace = {
                    "name": function.name,
                    "before_context": deepcopy(result["context"]),
                    "arguments": deepcopy(args),
                    "keyword_arguments": deepcopy(kwargs),
                }

            return_value = None

            if function.has_context():
                return_value = function.callable(result["context"], *args, **kwargs)
            else:
                return_value = function.callable(*args, **kwargs)

            if "trace" in result:
                trace["return_value"] = deepcopy(return_value)
                trace["after_context"] = deepcopy(result["context"])

                result["trace"].append(trace)

            return return_value

        return callable

####################################################################################################

def format_content(message):
    return """
You have the following application programming interface:

{functions_prompt}

Write a Python 3 function, which uses the provided application programming interface for the instruction
"{message}"

Afterwards, execute the previously written Python 3 function. Do not use other functions, only those provided by the given application programming interface.
""".format(message=message, functions_prompt=table.format_prompt_specification())

####################################################################################################

def print_separator(newlines = 0):
    columns = 80
    try:
        columns = get_terminal_size().columns
    except:
        pass
    finally:
        pass

    print(str(columns * "#") + str(newlines * "\n"))

class TestCase:
    def __init__(
            self,
            function_table,
            url,
            key,
            model,
            temperature,
            prompt,
            correct_code = None,
    ):
        self.__function_table = function_table
        self.__url = url
        self.__key = key
        self.__model = model
        self.__temperature = temperature
        self.__prompt = prompt
        self.__correct_code = correct_code

    @property
    def url(self):
        return self.__url

    @property
    def key(self):
        return self.__key

    @property
    def model(self):
        return self.__model

    @property
    def temperature(self):
        return self.__temperature

    def run(self, context = None):
        if context is None:
            context = {}

        context["get_test_case"] = lambda: self

        print_separator(0)
        print(table.format_prompt_specification())
        print_separator(0)

        request_headers = {}

        if self.__key is not None and len(self.__key) > 0:
            request_headers["Authorization"] = "Bearer " + self.__key

        request_body={
            "model": self.__model,
            "messages": [
                {'role': 'system', 'content': 'You are a Python 3 code generator.'},
                {"role": "user", "content": format_content(self.__prompt)},
            ],
            "stream": True,
        }

        if self.__temperature is not None:
            request_body["temperature"] = float(self.__temperature)

        start_time = time.time_ns()
        time_to_first_token_ns = None

        print(self.__url, self.__model, self.__temperature, self.__prompt)
        print_separator(0)

        result = request_chat_completions(
            self.__url,
            self.__model,
            'You are a Python 3 code generator.',
            self.__key,
            format_content(self.__prompt),
            self.__temperature,
        )

        output = result["output"]
        elapsed_s = result["elapsed_s"]
        time_to_first_token_ms = result["time_to_first_token_ms"]

        print(output)
        print_separator(0)

        marker = "```"

        left_markers = [marker + "python3", marker + "python", marker]
        right_marker = marker

        output = output.strip("\n\r ")

        start = None
        start_padding = None

        for left_marker in left_markers:
            index = output.find(left_marker)

            if index < 0:
                continue

            start = index
            start_padding = len(left_marker)

            break

        end = output.find(right_marker, start + start_padding)
        if end < 0:
            end = len(output)

        code = output[start + start_padding:end]

        print(code)
        print_separator(0)

        try:
            execution_result = self.__function_table.evaluate(
                code,
                context = context,
                tracing = True,
            )

            print_separator(0)

            print("Success (total {}s, ttft {}ms)".format(elapsed_s, time_to_first_token_ms))

            return {
                "execution": execution_result,
                "generated_code": code,
                "response_time_in_seconds": elapsed_s,
                "time_to_first_token_in_milliseconds": time_to_first_token_ms,
            }
        except Exception as e:
            print("Failed (total {}s, ttft {}ms)".format(elapsed_s, time_to_first_token_ms))
            print(format_exc())

        print_separator(0)

####################################################################################################

def find_file(expression: 'String') -> 'String|null':
    directory = "files"

    for file_name in listdir(directory):
        if not path.isfile(path.join(directory, file_name)):
            continue

        if expression not in file_name:
            continue

        return file_name

    return None

def find_all_audio_files() -> Collection['String']:
    directory = "files"

    return [
        f for f in listdir(directory) if path.isfile(path.join(directory, f))
    ]

def play_audio_file(file_path: 'String') -> None:
    return
    result = subprocess.run(
        ["termux-media-player", "play", path.join("files", file_path)],
        text=True,
        check=True,
        capture_output=True,
    )

    print(result.stdout)

def stop_audio_player() -> None:
    return
    result = subprocess.run(
        ["termux-media-player", "stop"],
        text=True,
        check=True,
        capture_output=True,
    )

    print(result.stdout)

def sleep(seconds: 'Integer') -> None:
    time.sleep(seconds)

def generate_random_number(context, inclusiveStart: 'Integer', exclusiveEnd: 'Integer') -> 'Integer':
    if 'seed' in context:
        seed(context['seed'])

    return randint(inclusiveStart, exclusiveEnd)

def wrapper():
    return 'Berlin'

def query_llm(context, query: 'String') -> 'String':
    test_case = context["get_test_case"]()

    return request_chat_completions(
        test_case.url,
        test_case.model,
        None,
        test_case.key,
        query,
        test_case.temperature,
    )

table = FunctionTable(FunctionSignatureFormatter())

table.register(
    Function.stub("find_contact_id", 1),
    name = "find_contact_id",
    argument_types = {
        "expression": "String",
    },
    return_type = "Integer|null",
)
table.register(
    Function.stub("find_contact_email", "john.doe@example.com"),
    name = "find_contact_email",
    argument_types = {
        "contact_id": "Integer",
    },
    return_type = "String|null",
)
table.register(
    Function.stub("play_voice"),
    name = "play_voice",
    argument_types = {
        "text": "String",
    },
    return_type = None,
)
table.register(
    Function.stub("ask_question", "Hello"),
    name = "ask_question",
    argument_types = {
        "question": "String",
    },
    return_type = "String",
)
table.register(
    Function.stub("send_email"),
    name = "send_email",
    argument_types = {
        "email": "String",
        "subject": "String",
        "text": "String",
        "attachment_paths": "Collection<String>",
    },
    return_type = None,
)
table.register(
    Function.stub("get_temperature", 37),
    name = "get_temperature",
    argument_types = {},
    return_type = "Integer",
)
table.register(
    Function.stub("shell", "Document 0\nDocument 1\nDocument 2"),
    name = "shell",
    argument_types = {
        "command": "String",
    },
    return_type = "String",
)
table.register(
    Function.stub("find_files", [0, 1, 2, 3, 4]),
    name = "find_files",
    argument_types = {
        "expression": "String",
    },
    return_type = "Collection<String>"
)
table.register(
    Function.stub("print_screen"),
    name = "print_screen",
    argument_types = {
        "text": "String",
    },
)
table.register(sleep)
table.register(find_all_audio_files)
table.register(generate_random_number)
table.register(play_audio_file)
table.register(find_file)
table.register(stop_audio_player)
table.register(query_llm)

####################################################################################################

# Execution Correctness
# Syntax Correctness
#
# TTFT
# Total Response Time
# Response Size - Lines of Code
# Code execution time (limit)
#
# Lines of Code ?

intentions = [
    ################################################################################################
    {
        "prompt": "Please sleep for 5 seconds",
        "context" : {},
        "correct_code": """
def main():
    sleep(5)

main()
""",
    },
    ################################################################################################
    {
        "prompt": "Please tell me a random number between 1 and 100",
        "context": {},
        "correct_code": """
def main():
    number = generate_random_number(1, 1000)
    print_screen(number)

main()
""",
    },
    ################################################################################################
    {
        "prompt": "Please tell me the current temperature",
        "context": {},
        "correct_code": """
def main():
    number = get_temperature()
    print_screen(number)

main()
""",
    },
    ################################################################################################
    {
        "prompt": "Play a random song in my list for 5 seconds",
        "context" : {},
        "correct_code": """
def main():
    all_songs = find_all_audio_files()
    if len(all_songs) == 0:
        return

    play_audio_file(all_songs[generate_random_number(0, len(all_songs))])

    sleep(5)

    stop_audio_player()

main()
""",
    },
    ################################################################################################
    {
        "prompt": "Which is the largest city in germany?",
        "context": {},
        "correct_code": """
def main():
    print_screen("Berlin is the largest city in germany.")

main()
"""
    },
    ################################################################################################
    {
        "prompt": "Please tell me all files in my home directory",
        "context" : {},
        "correct_code": """
def main():
    files = list(
        map(
            lambda x: x.split('/')[-1]
            shell("ls ~"),
        )
    )

    print_screen(files)

main()
""",
    },
    ################################################################################################
    {
        "prompt": "Please send my car title to my insurance company",
        "context" : {},
        "correct_code": """
def main():
    pass

main()
""",
    },
    ################################################################################################
    {
        "prompt": "Please summarize the wikipedia article https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)",
        "context" : {},
        "correct_code": """
def main():
    pass

main()
""",
    },
    ################################################################################################
    {
        "prompt": "Please install nginx on the machine with the address 127.0.0.1:2222",
        "context" : {},
        "correct_code": """
def main():
    shell("ssh 127.0.0.1:2222 'sudo apt-get update && sudo apt-get install nginx -y'")

main()
""",
    },
    ################################################################################################
]

####################################################################################################

class Encoder(JSONEncoder):
    def default(self, instance):
        if callable(instance):
            return {}

        return super().default(instance)

####################################################################################################

DEFAULT_ENDPOINT_URL = "https://api.openai.com/v1/chat/completions"
DEFAULT_MODEL_NAME = "gpt-4o-mini"
DEFAULT_MODEL_TEMPERATURE = 0.0

intention = intentions[4]

context = {
    "seed": 2 ** 64 - 1,
}

correct_execution_result = table.evaluate(
    intention["correct_code"],
    context = context,
    tracing = True,
)

test_case = TestCase(
    table,
    environ.get("ENDPOINT_URL", DEFAULT_ENDPOINT_URL),
    environ.get("ENDPOINT_KEY", None),
    environ.get("MODEL_NAME", DEFAULT_MODEL_NAME),
    environ.get("MODEL_TEMPERATURE", DEFAULT_MODEL_TEMPERATURE),
    intention["prompt"],
    intention["correct_code"],
)

llm_result = test_case.run(context)

print(dumps(correct_execution_result, cls = Encoder, indent=4))
print(dumps(llm_result["execution"], cls = Encoder, indent = 4))

####################################################################################################

models = [
    {
        "endpoint_url": "https://api.openai.com/v1/chat/completions",
        "endpoint_key": None,
        "model_name": "gpt-4o-mini",
        "model_temperature": 0,
    },
]
