"""Voice assistant based on the gpt language model.

Author:
    Pablo Dorrio Vazquez (@pablodorrio)
"""

import os

import openai
import pyttsx3
import speech_recognition as sr

from commands import ACTIVATE_COMMANDS, DEACTIVATE_COMMANDS, EXIT_COMMANDS

openai.api_key = os.getenv("OPENAI_API_KEY")

messages = [{"role": "system", "content": "You are a helpful assistant."}]


def gpt_response(text: str) -> str:
    """Get the response from the dialog with gpt-3.5-turbo model.

    Args:
        text (str): The user input.
    """
    messages.append({"role": "user", "content": text})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    openai_response = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": openai_response})

    return openai_response


def speak(text: str) -> None:
    """Transform text to speech and speak it.

    Args:
        text (str): The text to speak.
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


exit_app = False
active = False

while not exit_app:
    try:
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            recognizer.adjust_for_ambient_noise(source, duration=0.2)
            audio = recognizer.listen(source)

            text = recognizer.recognize_google(audio, language="es-ES").lower()
            print(text)

            if text in ACTIVATE_COMMANDS:
                active = True
            elif text in DEACTIVATE_COMMANDS:
                active = False
            elif text in EXIT_COMMANDS:
                active = False
                exit_app = True

            if active:
                response = gpt_response(text)
                print(response)
                speak(response)

    except sr.UnknownValueError:
        recognizer = sr.Recognizer()
        continue
