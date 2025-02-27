# LLMWorkflowGenerator

## Dependencies Overview

```
Python 3
virtualenv
```

## Environment Variables Overview

| Key               | Description                               | Default                                    |
|-------------------|-------------------------------------------|--------------------------------------------|
| ENDPOINT_KEY      | API key for the chat completions endpoint | -                                          |
| ENDPOINT_URL      | URL of the chat completions endpoint      | https://api.openai.com/v1/chat/completions |
| MODEL_NAME        | LLM model name                            | gpt-4o-mini                                |
| MODEL_TEMPERATURE | LLM model temperature                     | 0                                          |

## Environment Setup

```shell
virtualenv environment
source environment/bin/activate
pip3 install -r requirements.txt
```

## Execution Setup

```shell 
export OPENAI_KEY=...
export MODEL=gpt4-4o-mini

source environment/bin/activate

echo "Say hello world" | python3 main.py
```

## Execution Examples

```shell
echo "Please send my car title to my insurance company" | python3 main.py
echo "Please tell me the current temperature" | python3 main.py
echo "Please play the song beat it by michael jackson" | python3 main.py
echo "Please tell me all files in my home directory" | python3 main.py
```
