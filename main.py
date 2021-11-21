#from _typeshed import Self
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
from voice_recording import *

BUTTON = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)
# pixels = Pixels()

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
    ser.reset_input_buffer()
    c = 1
    # print(c)
    print("zaczynamy:")
    # r = sr.Recognizer()
    pixels = APA102(3)
    pixels.set_pixel(0, 0, 0, 0, 0)
    pixels.clear_strip()

    while True:

        # while(GPIO.input(BUTTON) == 1):
        #     pass
        # pixels.listening_1f()
        # # time.sleep(3)
        # try:
        #     with sr.Microphone() as source:
        #         print("Podaj pierwsze pole")
        #         audio = r.listen(source, 3, 3)
        #         field_1 = r.recognize_google(audio, language="pl")
        # except:
        #     print("error")
        # pixels.listening_1f()
        field_1 = first_field()

        print("pole 1="+field_1)
        pixels.listening_2f()

        try:
            with sr.Microphone() as source:
                print("Podaj drugie pole")
                audio = r.listen(source, 3, 3)
                field_2 = r.recognize_google(audio, language="pl")
        except:
            print("error")

        pixels.movement()
        print("pole 2="+field_2)

        ser.write(field_1.encode('ascii'))

        while (ser.readline().decode('ascii').rstrip() != "1"):
            pass
        pixels.done_movement()
