"""Voice assistant based on the gpt language model.

Author:
    Pablo Dorrio Vazquez (@pablodorrio)
"""


import speech_recognition as sr

from core.commands import ACTIVATE_COMMANDS, DEACTIVATE_COMMANDS, EXIT_COMMANDS
from core.gpt import gpt_response
from core.speak import speak

if __name__ == "__main__":
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
