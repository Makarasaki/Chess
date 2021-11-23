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


def listen_field(field_n):
    flag = 0
    while(flag == 0):
        while(GPIO.input(BUTTON) == 1):
            pass
        pixels.set_pixel_rgb(field_n-1, 0x0000FF, 10)
        pixels.show()

        try:
            with sr.Microphone() as source:
                print("Podaj {} pole".format(field_n))
                audio = r.listen(source, 3, 3)
                field = r.recognize_google(audio, language="pl")
                if field in all_fields:
                    flag = 1
                    pixels.set_pixel_rgb(field_n-1, 0x00FF00, 10)
                    pixels.show()
                    return str.upper(field)
                else:
                    print("nie ma takiego pola:"+field)
                    pixels.set_pixel_rgb(field_n-1, 0xFF0000, 10)
                    pixels.show()
        except:
            pixels.set_pixel_rgb(field_n-1, 0xFF0000, 10)
            pixels.show()
            print("error, try again")
