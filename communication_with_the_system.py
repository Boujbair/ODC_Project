from tracemalloc import stop
import speech_recognition as sr
from gtts import gTTS
import playsound
import time
import os

def speak(text):
    tts= gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception" + str(e))

    return said.lower()

# Example to test the system

# if the user said "I want to wash my hands"
text = get_audio()
if "Hands" in text:
    speak("you need 250 ml")         