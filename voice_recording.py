import sys
import pyaudio
import wave
import speech_recognition as sr
import RPi.GPIO as GPIO
import time
import serial
import spidev
from LED import *
from apa102 import *
from Fields import *
from math import ceil
from main import *

pixels = APA102(3)
BUTTON = 17
r = sr.Recognizer()


def first_field():
    flag = 0
    while(flag == 0):
        while(GPIO.input(BUTTON) == 1):
            pass
        pixels.listening_1f()

        try:
            with sr.Microphone() as source:
                print("Podaj pierwsze pole")
                audio = r.listen(source, 3, 3)
                field_1 = r.recognize_google(audio, language="pl")
                flag = 1
                return field_1
        except:
            print("error, try again")
