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
from math import ceil

BUTTON = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)
pixels = Pixels()

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
    ser.reset_input_buffer()
    c = 1
    # print(c)
    print("zaczynamy:")

    pixels = APA102(3)

    while True:

        while(GPIO.input(BUTTON) == 1):
            pass

        # if(GPIO.input(BUTTON) == 0):
        print("Hello World!")
        pixels.set_pixel(0, 0, 0, 0, 0)
        pixels.set_pixel(0, 10, 10, 0, 50)
        pixels.show()
        time.sleep(3)
        pixels.clear_strip()

        print(c)
        line = str(c) + "\n"
        ser.write(line.encode('ascii'))

        line = ser.readline().decode('ascii').rstrip()

        if (line == "1"):
            #print("nowa wiadomosc")
            c = c+1
            # print(c)


# print("Hello World!")
# r = sr.Recognizer()

# with sr.Microphone() as source:
#     print("say something!")
#     audio = r.listen(source, 10, 10)

# try:
#     print("tekst:" + r.recognize_google(audio, language="pl"))
# except sr.UnknownValueError:
#     print("dupa")
# except sr.RequestError as e:
#     print("lipa;{0}".format(e))
