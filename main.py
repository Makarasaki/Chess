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

X_pos = 0
Y_pos = 0

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

    while True:
        pixels.clear_strip()

        field_1 = listen_field(1)

        print("Pole 1=" + field_1)
        print("środek pola 1=" + str(eval(str.upper(field_1)).X_center))

        # pixels.listening_2f()

        field_2 = listen_field(2)

        print("Pole 2=" + field_2)
        print("środek pola 2=" + str(eval(str.upper(field_2)).X_center))

        pixels.set_pixel_rgb(2, 0x0000FF, 10)
        pixels.show()

        message = msg_gen(eval(field_1).X_center, eval(
            field_1).Y_center, eval(field_1).state)

        ser.write(message.encode('ascii'))

        while (ser.readline().decode('ascii').rstrip() != "1"):
            pass
        pixels.set_pixel_rgb(2, 0x00FF00, 10)
        pixels.show()
