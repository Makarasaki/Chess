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
    string_to_number_pl = {'jeden': '1', 'dwa': '2', 'trzy': '3',
                           'cztery': '4', 'pięć': '5', 'sześć': '6', 'siedem': '7', 'osiem': '8'}
    flag = 0
    pixels.set_pixel_rgb(0, 0x00FF00, 1)
    pixels.set_pixel_rgb(1, 0x000000, 1)
    while(flag == 0):
        if GPIO.input(BUTTON) == 0:
            pixels.set_pixel_rgb(field_n-1, 0x0000FF, 1)
            pixels.show()

            try:
                with sr.Microphone() as source:
                    print("Podaj {} pole".format(field_n))
                    audio = r.listen(source, 0x0000FF, 3)
                    text = str.lower(r.recognize_google(audio, language="pl"))
                    text_split = text.split()

                    if len(text_split) > 1 and not text_split[1].isnumeric():
                        text_split[1] = string_to_number_pl[text_split[1]]
                        field = text_split[0][0] + text_split[1][0]
                    else:
                        field = text[0] + text[-1]
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


def listen(argument1, argument2):
    flag = 0
    pixels.set_pixel_rgb(0, 0x00FF00, 1)
    pixels.set_pixel_rgb(1, 0x000000, 1)
    pixels.show()
    while(flag == 0):
        if GPIO.input(BUTTON) == 0:
            pixels.set_pixel_rgb(0, 0x0000FF, 1)
            pixels.show()
            try:
                with sr.Microphone() as source:
                    print("wybierz:"+argument1 + "/" + argument2)
                    audio = r.listen(source, 0x0000FF, 3)
                    mode = str.lower(r.recognize_google(audio, language="pl"))
                    if mode in [argument1, argument2, 'rysowanie']:
                        flag = 1
                        print(mode)
                        pixels.set_pixel_rgb(0, 0x00FF00, 1)
                        pixels.show()
                        return mode
                    else:
                        pixels.set_pixel_rgb(0, 0xFF0000, 1)
                        pixels.show()
                        print("Error")
            except:
                print("error, try again")
