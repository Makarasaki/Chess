# from _typeshed import Self
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
import chess.engine


def human():
    legal = 0
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
    ser.reset_input_buffer()

    print("zaczynamy:")
    pixels = APA102(3)
    pixels.set_pixel(0, 0, 0, 0, 0)

    # tymczasowe homeowanie
    time.sleep(3)
    home(ser)

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
        print("ostateczny ruch:" + move)
        board.push(move_ch)
        print(board)

        pixels.set_pixel_rgb(0, 0x00FF00, 1)
        pixels.set_pixel_rgb(1, 0x00FF00, 1)
        pixels.set_pixel_rgb(2, 0x0000FF, 1)
        pixels.show()

        move_exe(move, field_1, field_2, ser)

        pixels.set_pixel_rgb(2, 0x00FF00, 1)
        pixels.show()
        time.sleep(1)


def engine():
    legal = 0
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
    ser.reset_input_buffer()

    print("zaczynamy:")
    pixels = APA102(3)
    pixels.set_pixel(0, 0, 0, 0, 0)

    # tymczasowe homeowanie
    time.sleep(3)
    home(ser)

    engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")
    board = chess.Board()

    print("kliknij aby wybrać kolor")
    color = listen("biały", "czarny")

    print(board)

    if color == "czarny":
        # ruch silnika
        engine_move = engine.play(board, chess.engine.Limit(depth=1))
        field_1 = str(engine_move.move)[0] + str(engine_move.move)[1]
        field_2 = str(engine_move.move)[2] + str(engine_move.move)[3]
        move_exe(engine_move.move, field_1, field_2, ser)
        board.push(engine_move.move)
        print("ruch silnika:")
        print(engine_move.move)
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

        move_exe(move, field_1, field_2, ser)

        pixels.set_pixel_rgb(2, 0x00FF00, 1)
        pixels.show()
        time.sleep(1)

        # ruch silnika
        engine_move = engine.play(board, chess.engine.Limit(depth=1))
        field_1 = str(engine_move.move)[0] + str(engine_move.move)[1]
        field_2 = str(engine_move.move)[2] + str(engine_move.move)[3]
        move_exe(engine_move.move, field_1, field_2, ser)
        board.push(engine_move.move)
        print("ruch silnika:")
        print(board)


def main():
    pixels.set_pixel(0, 0, 0, 0, 0)
    pixels.clear_strip()
    print("kliknij, żeby rozpocząć")
    mode = listen("jednoosobowy", "wieloosobowy")
    if mode == "jednoosobowy":
        engine()
    else:
        human()


if __name__ == '__main__':
    main()


def move_exe(move, field_1, field_2, ser):
    if move == "e1g1":
        castling_white_short(ser)
    elif move == "e1c1":
        castling_white_long(ser)
    elif move == "e8g8":
        castling_black_short(ser)
    elif move == "e8c8":
        castling_black_long(ser)
    elif eval(field_2).state != '0':
        capture(field_2, ser)
        # Ruch z pola 1 na pole 2
        if eval(field_1).state in ('N', 'n'):
            knight_move(field_1, field_2, ser)
        else:
            regular_move(field_1, field_2, ser)
    else:
        if eval(field_1).state in ('N', 'n'):
            knight_move(field_1, field_2, ser)
        else:
            regular_move(field_1, field_2, ser)

    eval(field_2).state = eval(field_1).state
    eval(field_1).state = '0'


def capture(field_2, ser):
    movement(eval(field_2).X_center, eval(field_2).Y_center, 0, ser)
    movement(eval(field_2).X_corner, eval(field_2).Y_corner, 1, ser)
    movement(eval(field_2).X_dump, eval(field_2).Y_corner, 1, ser)
    movement(eval(field_2).X_dump, eval(field_2).Y_dump, 1, ser)


def knight_move(field_1, field_2, ser):
    movement(eval(field_1).X_center, eval(field_1).Y_center, 0, ser)
    print('srodek')
    movement(eval(field_1).X_corner, eval(field_1).Y_corner, 1, ser)
    print('corner')
    movement(eval(field_2).X_corner, eval(field_1).Y_corner, 1, ser)
    print('X corner')
    movement(eval(field_2).X_corner, eval(field_2).Y_corner, 1, ser)
    print('Y corner')
    movement(eval(field_2).X_center, eval(
        field_2).Y_center - a1.jump_offset, 1, ser)
    print('srodek2')


def regular_move(field_1, field_2, ser):
    movement(eval(field_1).X_center, eval(field_1).Y_center, 0, ser)
    movement(eval(field_2).X_center, eval(
        field_2).Y_center - a1.jump_offset, 1, ser)


def castling_white_short(ser):
    movement(eval("e1").X_center, eval("e1").Y_center, 0, ser)
    movement(eval("e1").X_corner, eval("e1").Y_corner, 1, ser)
    movement(eval("h1").X_center, eval("h1").Y_center, 0, ser)
    movement(eval("f1").X_center, eval("f1").Y_center, 1, ser)
    movement(eval("e1").X_corner, eval("e1").Y_corner, 0, ser)
    movement(eval("g1").X_corner, eval("g1").Y_corner, 1, ser)
    movement(eval("g1").X_center, eval("g1").Y_center, 1, ser)


def castling_white_long(ser):
    movement(eval("e1").X_center, eval("e1").Y_center, 0, ser)
    movement(eval("e1").X_corner, eval("e1").Y_corner, 1, ser)
    movement(eval("a1").X_center, eval("a1").Y_center, 0, ser)
    movement(eval("d1").X_center, eval("d1").Y_center, 1, ser)
    movement(eval("e1").X_corner, eval("e1").Y_corner, 0, ser)
    movement(eval("c1").X_corner, eval("c1").Y_corner, 1, ser)
    movement(eval("c1").X_center, eval("c1").Y_center, 1, ser)


def castling_black_short(ser):
    movement(eval("e8").X_center, eval("e8").Y_center, 0, ser)
    movement(eval("e8").X_corner, eval("e8").Y_corner, 1, ser)
    movement(eval("h8").X_center, eval("h8").Y_center, 0, ser)
    movement(eval("f8").X_center, eval("f8").Y_center, 1, ser)
    movement(eval("e8").X_corner, eval("e8").Y_corner, 0, ser)
    movement(eval("g8").X_corner, eval("g8").Y_corner, 1, ser)
    movement(eval("g8").X_center, eval("g8").Y_center, 1, ser)


def castling_black_long(ser):
    movement(eval("e8").X_center, eval("e8").Y_center, 0, ser)
    movement(eval("e8").X_corner, eval("e8").Y_corner, 1, ser)
    movement(eval("a8").X_center, eval("a8").Y_center, 0, ser)
    movement(eval("d8").X_center, eval("d8").Y_center, 1, ser)
    movement(eval("e8").X_corner, eval("e8").Y_corner, 0, ser)
    movement(eval("c8").X_corner, eval("c8").Y_corner, 1, ser)
    movement(eval("c8").X_center, eval("c8").Y_center, 1, ser)


def movement(X, Y, M, ser):
    ser.write(msg_gen(X, Y, M).encode('ascii'))
    while True:
        ser.write(msg_gen(X, Y, M).encode('ascii'))
        if ser.readline().decode('ascii').rstrip() == "1":
            print("git")
            break


def home(ser):
    ser.write("H1 ".encode('ascii'))
    while True:
        if ser.readline().decode('ascii').rstrip() == "1":
            print("git")
            break
