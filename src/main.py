import os

import openai
import pyttsx3
import speech_recognition as sr

from commands import EXIT_COMMANDS

recognizer = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.2)
            audio = recognizer.listen(source)

            text = recognizer.recognize_google(audio, language="es-ES").lower()

            if text in EXIT_COMMANDS:
                exit(0)

            print(text)
    except sr.UnknownValueError:
        recognizer = sr.Recognizer()
        continue
