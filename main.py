#!/usr/bin/env python3
import sys
import pyaudio
import speech_recognition as sr

print("Hello World!")
r = sr.Recognizer()

with sr.Microphone() as source:
    print("say something!")
    audio = r.listen(source, 10, 10)

try:
    print("tekst:" + r.recognize_google(audio, language="pl"))
except sr.UnknownValueError:
    print("dupa")
except sr.RequestError as e:
    print("lipa;{0}".format(e))
