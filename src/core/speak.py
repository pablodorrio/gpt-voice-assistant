"""Speak module.

Author:
    Pablo Dorrio Vazquez (@pablodorrio)
"""

import pyttsx3


def speak(text: str) -> None:
    """Transform text to speech and speak it.

    Args:
        text (str): The text to speak.
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
