# import sys
# import pyaudio
# import wave
# from math import ceil
# import serial
# import spidev
# import time
from genericpath import exists
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
                print('Podaj {} pole'.format(field_n))
                audio = r.listen(source, 0x0000FF, 3)
                field = str.lower(r.recognize_google(audio, language='pl'))
                if field_n == 1 and field in ['pion', 'skoczek', 'koń', 'kon', 'konik', 'goniec', 'wieża', 'królowa', 'królówka', 'hetman', 'król']:
                    if field is 'pion':
                        field = 'P'
                    elif field in ['skoczek', 'koń', 'kon', 'konik']:
                        field = 'N'
                    elif field is 'goniec':
                        field = 'B'
                    elif field is 'król':
                        field = 'K'
                    elif field in ['królowa', 'królówka', 'hetman']:
                        field = 'Q'
                    elif field is 'wieża':
                        field = 'R'
                    return field
                else:
                    field = field[0]+field[-1]
                    if field in all_fields:
                        flag = 1
                        pixels.set_pixel_rgb(field_n-1, 0x00FF00, 1)
                        pixels.show()
                        return field
                    else:
                        print('nie ma takiego pola:'+field)
                        pixels.set_pixel_rgb(field_n-1, 0xFF0000, 1)
                        pixels.show()
        except:
            pixels.set_pixel_rgb(field_n-1, 0xFF0000, 1)
            pixels.show()
            print('error, try again')


def listen(argument1, argument2):
    flag = 0
    pixels.set_pixel_rgb(0, 0x00FF00, 1)
    pixels.set_pixel_rgb(1, 0x000000, 1)
    pixels.show()
    while(flag == 0):
        while(GPIO.input(BUTTON) == 1):
            pass
        pixels.set_pixel_rgb(0, 0x0000FF, 1)
        pixels.show()
        try:
            with sr.Microphone() as source:
                print('wybierz:'+argument1 + '/' + argument2)
                audio = r.listen(source, 0x0000FF, 3)
                mode = str.lower(r.recognize_google(audio, language='pl'))
                if mode in [argument1, argument2]:
                    flag = 1
                    print(mode)
                    pixels.set_pixel_rgb(0, 0x00FF00, 1)
                    pixels.show()
                    return mode
                else:
                    pixels.set_pixel_rgb(0, 0xFF0000, 1)
                    pixels.show()
                    print('Error')
        except:
            print('error, try again')
