# LLMWorkflowGenerator

This project investigates how Large Language Models (LLMs) can orchestrate workflows on mobile devices by translating high-level natural language goals into executable action sequences. Instead of relying on external simulation frameworks, the system is implemented entirely within Termux, which serves as a reproducible and portable execution environment. The approach focuses on prototyping and evaluating LLM-driven policies for personal assistance and everyday automation tasks. Natural language instructions are transformed into structured plans that are executed directly on the device. In this way, language is mapped to reliable closed-loop control of processes running locally. The main objective of the project is to provide a lightweight and adaptable pipeline for language-driven task automation on mobile platforms. Success rates, safety aspects, and efficiency are benchmarked within the Termux environment before any potential transfer to broader use cases.

## Research Context

Recent advances in LLMs have sparked interest in using them not only for textual tasks (e.g. translation, summarization, QA), but also as higher-level orchestrators: interpreting user intent, breaking down tasks, and issuing structured workflows of actions or API calls. However, bridging the gap from a freeform natural language instruction to a safe, well-formed, and reliable executable workflow remains an open challenge.

## Repository Structure

### main.py

Main script, which contains the required classes such as the `FunctionTable`, the implementation of Android-related functions for playing audio, as well as the glue
code for the external LLM service.

### files

A collection of static sample soundtracks for demonstration purposes.

### outputs

A collection of results produced by the experiments.

## Getting Started

The application requires Python 3 for execution and runs on Android as well as on Linux-based development systems.

### Setup

#### Android

- Install [Termux](https://f-droid.org/packages/com.termux/)
- Install [Termux::API](https://f-droid.org/packages/com.termux.api/)
- Open Termux

``` shell
pkg update
pkg upgrade -y
pkg install -y termux-api python3 git
virtualenv environment
source environment/bin/activate
pip3 install -r requirements.txt
```

#### Setup with virtualenv

```shell
virtualenv environment
source environment/bin/activate
pip3 install -r requirements.txt
```

#### Setup with pip

``` shell
pip install -r requirements.txt
```

### Execution

#### Environment Variables

| Key               | Description                               | Default                                    |
|-------------------|-------------------------------------------|--------------------------------------------|
| ENDPOINT_KEY      | API key for the chat completions endpoint | -                                          |
| ENDPOINT_URL      | URL of the chat completions endpoint      | https://api.openai.com/v1/chat/completions |
| MODEL_NAME        | LLM model name                            | gpt-4o-mini                                |
| MODEL_TEMPERATURE | LLM model temperature                     | 0                                          |

#### Run

```shell 
source environment/bin/activate

export ENDPOINT_KEY=...
export MODEL_NAME=gpt-4o-mini

echo "Say hello world" | python3 main.py
```

#### Examples 

```shell
echo "Please send my car title to my insurance company" | python3 main.py
echo "Please tell me the current temperature" | python3 main.py
echo "Please play the song beat it by michael jackson" | python3 main.py
echo "Please tell me all files in my home directory" | python3 main.py
echo "Play a random song in my list for 10 seconds" | python3 main.py
```

#### Run Experiments

```shell
python3 main.py experiments

```
