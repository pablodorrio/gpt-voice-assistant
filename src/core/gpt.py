"""Use the OpenAI API to get a response from the dialog with gpt-3.5-turbo model.

Author:
    Pablo Dorrio Vazquez (@pablodorrio)
"""

import os

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

messages = [{"role": "system", "content": "You are a helpful assistant."}]


def gpt_response(text: str) -> str:
    """Get the response from the dialog with gpt-3.5-turbo model.

    Args:
        text (str): The user input.
    """
    messages.append({"role": "user", "content": text})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages)

    openai_response = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": openai_response})

    return openai_response
