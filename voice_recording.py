# import sys
# import pyaudio
# import wave
# from math import ceil
# import serial
# import spidev
# import time
import speech_recognition as sr
import RPi.GPIO as GPIO
from apa102 import *
from Fields import *
from main import *

pixels = APA102(3)
BUTTON = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)
r = sr.Recognizer()


def listen_field(field_n):
    flag = 0
    pixels.set_pixel_rgb(0, 0x00FF00, 1)
    pixels.set_pixel_rgb(1, 0x000000, 1)
    while(flag == 0):
        while(GPIO.input(BUTTON) == 1):
            pass
        pixels.set_pixel_rgb(field_n-1, 0x0000FF, 1)
        pixels.show()

        try:
            with sr.Microphone() as source:
                print("Podaj {} pole".format(field_n))
                audio = r.listen(source, 0x0000FF, 3)
                field = str.lower(r.recognize_google(audio, language="pl"))
                field = field[0]+field[-1]
                if field in all_fields:
                    flag = 1
                    pixels.set_pixel_rgb(field_n-1, 0x00FF00, 1)
                    pixels.show()
                    return field
                else:
                    print("nie ma takiego pola:"+field)
                    pixels.set_pixel_rgb(field_n-1, 0xFF0000, 1)
                    pixels.show()
        except:
            pixels.set_pixel_rgb(field_n-1, 0xFF0000, 1)
            pixels.show()
            print("error, try again")
