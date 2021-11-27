#from _typeshed import Self
# import sys
# import pyaudio
# import wave
# import speech_recognition as sr
# import RPi.GPIO as GPIO
# import spidev
# from math import ceil
import time
import serial
from apa102 import *
from Fields import *
from voice_recording import *
import chess


def main():
    legal = 0

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

            move = "0000" if field_1[0] + field_1[1] == field_2[0] + \
                field_2[1] else field_1 + field_2
            print("Twój ruch:" + move)

            print(board.legal_moves)

            move_ch = chess.Move.from_uci(move)

            if move_ch in board.legal_moves:
                legal = 1
                break
            else:
                pixels.set_pixel_rgb(0, 0xFF0000, 1)
                pixels.set_pixel_rgb(1, 0xFF0000, 1)
                pixels.show()
                print("nielegalny ruch")
                legal = 0

        legal = 0
        print("ostateczny ruch:"+move)
        board.push(move_ch)
        print(board)

        pixels.set_pixel_rgb(0, 0x00FF00, 1)
        pixels.set_pixel_rgb(1, 0x00FF00, 1)
        pixels.set_pixel_rgb(2, 0x0000FF, 1)
        pixels.show()

        # Jeśli bicie
        if eval(field_2).state == 1:
            capture(field_2, ser)

        # Ruch z pola 1 na pole 2
        regular_move(field_1, field_2, ser)

        eval(field_1).state = 0
        eval(field_2).state = 1

        pixels.set_pixel_rgb(2, 0x00FF00, 1)
        pixels.show()
        time.sleep(1)


if __name__ == '__main__':
    main()


def capture(field_2, ser):
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


def regular_move(field_1, field_2, ser):
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
