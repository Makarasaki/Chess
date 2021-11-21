#!/usr/bin/env python3

import speech_recognition as sr
r = sr.Recognizer()
sr.__version__
harvard = sr.AudioFile('harvard.wav')
with harvard as source:
	audio = r.record(source)

type(audio)
print(r.recognize_google(audio, language="pl"))
