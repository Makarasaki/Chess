#from _typeshed import Self
# import sys
# import pyaudio
# import wave
# import speech_recognition as sr
# import RPi.GPIO as GPIO
# import spidev
import time
import serial
from apa102 import *
from Fields import *
from math import ceil
from voice_recording import *
import chess

X_pos = 0
Y_pos = 0

legal = 0

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
    ser.reset_input_buffer()

    print("zaczynamy:")
    pixels = APA102(3)
    pixels.set_pixel(0, 0, 0, 0, 0)

    # tymczasowe homeowanie
    message = msg_gen(3, 3, 0)
    ser.write(message.encode('ascii'))
    while (ser.readline().decode('ascii').rstrip() != "1"):
        ser.write(message.encode('ascii'))
        # pass

    board = chess.Board()
    print(board)

    while True:

        pixels.set_pixel(0, 0, 0, 0, 0)
        pixels.clear_strip()

        while (legal != 1):
            field_1 = listen_field(1)
            print("Pole 1=" + field_1)
            field_2 = listen_field(2)
            print("Pole 2=" + field_2)

            if chess.Move.from_uci(str.lower(field_1)+str.lower(field_2)) in board.legal_moves:
                legal = 1
                break
            else:
                pixels.set_pixel_rgb(0, 0xFF0000, 1)
                pixels.set_pixel_rgb(1, 0xFF0000, 1)
                pixels.show()
                print("nielegalny ruch")
                legal = 0

        legal = 0
        board.push(chess.Move.from_uci(field_1+field_2))
        print(board)

        pixels.set_pixel_rgb(0, 0x00FF00, 1)
        pixels.set_pixel_rgb(1, 0x00FF00, 1)
        pixels.set_pixel_rgb(2, 0x0000FF, 1)
        pixels.show()

        # Jeśli bicie
        if eval(field_2).state == 1:
            # podjazd pod bite pole bez magnesu
            message = msg_gen(eval(field_2).X_center,
                              eval(field_2).Y_center, 0)
            ser.write(message.encode('ascii'))
            while (ser.readline().decode('ascii').rstrip() != "1"):
                pass

            # załączenie magnesu, podjechanie do kąta
            message = msg_gen(eval(field_2).X_corner,
                              eval(field_2).Y_corner, 1)
            ser.write(message.encode('ascii'))
            while (ser.readline().decode('ascii').rstrip() != "1"):
                pass

            # podjechanie do pozycji X śmietnika
            message = msg_gen(eval(field_2).X_dump, eval(field_2).Y_corner, 1)
            ser.write(message.encode('ascii'))
            while (ser.readline().decode('ascii').rstrip() != "1"):
                pass

            # podjechanie do pozycji Y śmietnika
            message = msg_gen(eval(field_2).X_dump, eval(field_2).Y_dump, 1)
            ser.write(message.encode('ascii'))
            while (ser.readline().decode('ascii').rstrip() != "1"):
                pass

        # Ruch z pola 1 na pole 2
        # wyłączenie magnesu i podjechanie pod pierwsze pole
        message = msg_gen(eval(field_1).X_center, eval(field_1).Y_center, 0)
        ser.write(message.encode('ascii'))
        while (ser.readline().decode('ascii').rstrip() != "1"):
            pass

        # włączenie magnesu i podjechanie do kąta
        message = msg_gen(eval(field_1).X_corner, eval(field_1).Y_corner, 1)
        ser.write(message.encode('ascii'))
        while (ser.readline().decode('ascii').rstrip() != "1"):
            pass

        # włączenie magnesu i podjechanie pozycji X kąta drugiego pola
        message = msg_gen(eval(field_2).X_corner, eval(field_1).Y_corner, 1)
        ser.write(message.encode('ascii'))
        while (ser.readline().decode('ascii').rstrip() != "1"):
            pass

        # włączenie magnesu i podjechanie pozycji Y kąta drugiego pola
        message = msg_gen(eval(field_2).X_corner, eval(field_2).Y_corner, 1)
        ser.write(message.encode('ascii'))
        while (ser.readline().decode('ascii').rstrip() != "1"):
            pass

        # włączenie magnesu i podjechanie środka drugiego pola
        message = msg_gen(eval(field_2).X_center, eval(field_2).Y_center, 1)
        ser.write(message.encode('ascii'))
        while (ser.readline().decode('ascii').rstrip() != "1"):
            pass

        eval(field_1).state = 0
        eval(field_2).state = 1

        pixels.set_pixel_rgb(2, 0x00FF00, 1)
        pixels.show()
        time.sleep(1)
