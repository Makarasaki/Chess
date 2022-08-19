#!/usr/bin/python3

# from _typeshed import Self
# import sys
# import pyaudio
# import wave
# import speech_recognition as sr
# import RPi.GPIO as GPIO
# import spidev
# from math import ceil
# from cgitb import text
# from cmath import sqrt
# from ast import While
# from ctypes.wintypes import tagRECT
# from multiprocessing.connection import wait
# import re
import time
# from tracemalloc import start
import serial
from apa102 import *
from Fields import *
from voice_recording import *
import chess
import chess.engine
# import math
# from datetime import datetime
# import pdb
# import asyncio
# import os


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

    while True:  # While not board.is_game_over():

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

    while True:  # While not board.is_game_over():

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

        # ruch silnika
        engine_move = engine.play(board, chess.engine.Limit(depth=1))
        field_1 = str(engine_move.move)[0] + str(engine_move.move)[1]
        field_2 = str(engine_move.move)[2] + str(engine_move.move)[3]
        move_exe(engine_move.move, field_1, field_2, ser)
        board.push(engine_move.move)
        print("ruch silnika:")
        print(board)


def game_test():
    # print(f"A: 1:X:{eval('a1').X_center} Y:{eval('a1').Y_center}, 2:X:{eval('a2').X_center} Y:{eval('a2').Y_center}, 3:X:{eval('a3').X_center} Y:{eval('a3').Y_center}, 4:X:{eval('a4').X_center} Y:{eval('a4').Y_center}, 5:X:{eval('a5').X_center} Y:{eval('a5').Y_center}, 6:X:{eval('a6').X_center} Y:{eval('a6').Y_center}, 7:X:{eval('a7').X_center} Y:{eval('a7').Y_center}, 8:X:{eval('a8').X_center} Y:{eval('a8').Y_center}")
    # print(f"B: 1:X:{eval('b1').X_center} Y:{eval('b1').Y_center}, 2:X:{eval('b2').X_center} Y:{eval('b2').Y_center}, 3:X:{eval('b3').X_center} Y:{eval('b3').Y_center}, 4:X:{eval('b4').X_center} Y:{eval('b4').Y_center}, 5:X:{eval('b5').X_center} Y:{eval('b5').Y_center}, 6:X:{eval('b6').X_center} Y:{eval('b6').Y_center}, 7:X:{eval('b7').X_center} Y:{eval('b7').Y_center}, 8:X:{eval('b8').X_center} Y:{eval('b8').Y_center}")
    # print(f"C: 1:X:{eval('c1').X_center} Y:{eval('c1').Y_center}, 2:X:{eval('c2').X_center} Y:{eval('c2').Y_center}, 3:X:{eval('c3').X_center} Y:{eval('c3').Y_center}, 4:X:{eval('c4').X_center} Y:{eval('c4').Y_center}, 5:X:{eval('c5').X_center} Y:{eval('c5').Y_center}, 6:X:{eval('c6').X_center} Y:{eval('c6').Y_center}, 7:X:{eval('c7').X_center} Y:{eval('c7').Y_center}, 8:X:{eval('c8').X_center} Y:{eval('c8').Y_center}")
    # print(f"D: 1:X:{eval('d1').X_center} Y:{eval('d1').Y_center}, 2:X:{eval('d2').X_center} Y:{eval('d2').Y_center}, 3:X:{eval('d3').X_center} Y:{eval('d3').Y_center}, 4:X:{eval('d4').X_center} Y:{eval('d4').Y_center}, 5:X:{eval('d5').X_center} Y:{eval('d5').Y_center}, 6:X:{eval('d6').X_center} Y:{eval('d6').Y_center}, 7:X:{eval('d7').X_center} Y:{eval('d7').Y_center}, 8:X:{eval('d8').X_center} Y:{eval('d8').Y_center}")
    # print(f"E: 1:X:{eval('e1').X_center} Y:{eval('e1').Y_center}, 2:X:{eval('e2').X_center} Y:{eval('e2').Y_center}, 3:X:{eval('e3').X_center} Y:{eval('e3').Y_center}, 4:X:{eval('e4').X_center} Y:{eval('e4').Y_center}, 5:X:{eval('e5').X_center} Y:{eval('e5').Y_center}, 6:X:{eval('e6').X_center} Y:{eval('e6').Y_center}, 7:X:{eval('e7').X_center} Y:{eval('e7').Y_center}, 8:X:{eval('e8').X_center} Y:{eval('e8').Y_center}")
    # print(f"F: 1:X:{eval('f1').X_center} Y:{eval('f1').Y_center}, 2:X:{eval('f2').X_center} Y:{eval('f2').Y_center}, 3:X:{eval('f3').X_center} Y:{eval('f3').Y_center}, 4:X:{eval('f4').X_center} Y:{eval('f4').Y_center}, 5:X:{eval('f5').X_center} Y:{eval('f5').Y_center}, 6:X:{eval('f6').X_center} Y:{eval('f6').Y_center}, 7:X:{eval('f7').X_center} Y:{eval('f7').Y_center}, 8:X:{eval('f8').X_center} Y:{eval('f8').Y_center}")
    # print(f"G: 1:X:{eval('g1').X_center} Y:{eval('g1').Y_center}, 2:X:{eval('g2').X_center} Y:{eval('g2').Y_center}, 3:X:{eval('g3').X_center} Y:{eval('g3').Y_center}, 4:X:{eval('g4').X_center} Y:{eval('g4').Y_center}, 5:X:{eval('g5').X_center} Y:{eval('g5').Y_center}, 6:X:{eval('g6').X_center} Y:{eval('g6').Y_center}, 7:X:{eval('g7').X_center} Y:{eval('g7').Y_center}, 8:X:{eval('g8').X_center} Y:{eval('g8').Y_center}")
    # print(f"H: 1:X:{eval('h1').X_center} Y:{eval('h1').Y_center}, 2:X:{eval('h2').X_center} Y:{eval('h2').Y_center}, 3:X:{eval('h3').X_center} Y:{eval('h3').Y_center}, 4:X:{eval('h4').X_center} Y:{eval('h4').Y_center}, 5:X:{eval('h5').X_center} Y:{eval('h5').Y_center}, 6:X:{eval('h6').X_center} Y:{eval('h6').Y_center}, 7:X:{eval('h7').X_center} Y:{eval('h7').Y_center}, 8:X:{eval('h8').X_center} Y:{eval('h8').Y_center}")
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
    ser.reset_input_buffer()
    moves_times = {}
    only_times = {0: '11.43', 1: '11.15', 2: '7.48', 3: '5.89', 4: '7.47', 5: '6.83', 6: '10.50', 7: '10.02', 8: '5.89', 9: '16.33', 10: '7.81', 11: '6.54', 12: '6.53', 13: '6.50', 14: '21.52', 15: '14.98', 16: '7.48', 17: '9.40', 18: '9.08', 19: '6.84', 20: '16.57', 21: '17.87', 22: '5.90', 23: '9.88', 24: '6.20', 25: '20.74', 26: '18.04', 27: '16.57', 28: '19.43', 29: '9.22',
                  30: '15.67', 31: '12.44', 32: '6.20', 33: '10.50', 34: '6.20', 35: '9.70', 36: '7.48', 37: '6.53', 38: '6.84', 39: '8.12', 40: '11.15', 41: '7.81', 42: '11.14', 43: '9.07', 44: '22.89', 45: '17.52', 46: '7.18', 47: '6.53', 48: '8.44', 49: '6.20', 50: '5.25', 51: '6.53', 52: '8.74', 53: '10.50', 54: '8.58', 55: '9.71', 56: '21.66', 57: '20.39', 58: '9.06', 59: '7.14'}
    duda_nakamura_moves = ["g1f3", "g8f6", "d2d4", "e7e6", "c2c4", "d7d5", "b1c3", "f8b4", "c1d2", "e8g8", "e2e3", "b7b6", "a2a3", "b4e7", "c3d5", "e6d5", "a1c1", "c8a6", "d1a4", "c7c5", "d4c5", "b6c5", "d2c3", "f6e4", "c3e5", "a6c4", "f1c4", "d5c4", "a4c4",
                           "e4f6", "e1g1", "b8d7", "e5c3", "d7b6", "c4e2", "d8d5", "f1d1", "d5e6", "c3a5", "f8d8", "f3d2", "d8d7", "d2f3", "a8d8", "d1d7", "d8d7", "h2h3", "h7h6", "e2b5", "d7d5", "b5a6", "e6d7", "a6e2", "f6e4", "f3e1", "d7a4", "a5b6", "a7b6", "c1c4", "a4d1"]
    # duda_nakamura_moves = ["a3h3"]
    i = 0
    time.sleep(3)
    home(ser)
    # move_exe('h8h7', 'h8', 'h7', ser)
    # movement(eval('a3').X_center, eval('a3').Y_center, 0, ser)
    # time.sleep(2)
    print("start timer!!!")
    while i < len(duda_nakamura_moves):
        field_1dn = str(duda_nakamura_moves[i])[
            0] + str(duda_nakamura_moves[i])[1]
        field_2dn = str(duda_nakamura_moves[i])[
            2] + str(duda_nakamura_moves[i])[3]
        # print(f"ruch: {duda_nakamura_moves[i]}")
        tic = time.perf_counter()
        # print(f"tic: {tic}")
        # move_exe(duda_nakamura_moves[i], field_1dn, field_2dn, ser)
        tac = time.perf_counter()
        # print(f"tac: {tac}")
        # print(f"Czas: {tac - tic}")
        print(only_times[i])
        moves_times[duda_nakamura_moves[i]] = format(tac - tic, '.2f')
        # only_times[i] = format(tac - tic, '.2f')
        # print(moves_times)
        i = i + 1
    print(moves_times)
    print(only_times)
    file = open("log.txt", "w")
    file.write(f"{moves_times} {only_times}")
    file.close()


def motor_reliability_test():
    BUTTON = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON, GPIO.IN)
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
    ser.reset_input_buffer()
    outside_fields = ["a1", "d4", "a7", "g8", "f3", "a5", "c8", "b7", "h2", "e3", "c1",
                      "a3", "g7", "g1", "d1", "f3", "h6", "b1", "a2", "e7", "a8", "h7", "a1", "koniec"]
    # tymczasowe homeowanie
    time.sleep(3)
    home(ser)
    i = 0
    movement(eval('a1').X_center,
             eval('a1').Y_center, 0, ser)
    while outside_fields[i] != "koniec":
        time.sleep(1)
        print(outside_fields[i])
        movement(eval(outside_fields[i]).X_corner,
                 eval(outside_fields[i]).Y_corner, 1, ser)
        i = i + 1


def draw_chessboard():
    BUTTON = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON, GPIO.IN)
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
    ser.reset_input_buffer()
    outside_fields = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8",
                      "b1",                                     "b8",
                      "c1",                                     "c8",
                      "d1",                                     "d8",
                      "e1",                                     "e8",
                      "f1",                                     "f8",
                      "g1",                                     "g8",
                      "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8"]

    # tymczasowe homeowanie
    time.sleep(3)
    home(ser)
    i = 0
    while True:
        if GPIO.input(BUTTON) == 0:
            time.sleep(1)
            print(outside_fields[i])
            movement(eval(outside_fields[i]).X_corner,
                     eval(outside_fields[i]).Y_corner, 1, ser)
            i = i + 1
            if i == len(outside_fields):
                i = 0


def voice_recognition_test():
    while True:
        if GPIO.input(BUTTON) == 0:
            try:
                with sr.Microphone() as source:
                    print("talk now")
                    audio = r.listen(source, 0x0000FF, 3)
                    text = str.lower(r.recognize_google(audio, language="pl"))
                    text_split = text.split()
                    print(text_split)
            except:
                print("error, try again")


def main():
    pixels.set_pixel(0, 0, 0, 0, 0)
    pixels.clear_strip()
    print("kliknij, żeby rozpocząć")
    # voice_recognition_test()
    game_test()
    # mode = listen("jednoosobowy", "wieloosobowy")
    # if mode == "jednoosobowy":
    #     engine()
    # elif mode == "wieloosobowy":
    #     human()
    # else:
    #     # draw_chessboard()
    #     # motor_reliability_test()
    #     # game_test()


if __name__ == '__main__':
    main()


def move_exe(move, field_11, field_22, ser):
    if move == "e1g1":
        castling_white_short(ser)
        eval("e1").state = '0'
        eval('h1').state = '0'
        eval('f1').state = 'K'
        eval('g1').state = 'R'
    elif move == "e1c1":
        castling_white_long(ser)
        eval("e1").state = '0'
        eval('a1').state = '0'
        eval('c1').state = 'K'
        eval('d1').state = 'R'
    elif move == "e8g8":
        castling_black_short(ser)
        eval("e8").state = '0'
        eval('h8').state = '0'
        eval('f8').state = 'k'
        eval('g8').state = 'r'
    elif move == "e8c8":
        castling_black_long(ser)
        eval("e8").state = '0'
        eval('a8').state = '0'
        eval('c8').state = 'k'
        eval('d8').state = 'r'
    elif eval(field_22).state != '0':
        capture(field_22, ser)
        # Ruch z pola 1 na pole 2
        if eval(field_11).state in ('N', 'n'):
            knight_move(field_11, field_22, ser)
        else:
            regular_move(field_11, field_22, ser)
        eval(field_22).state = eval(field_11).state
        eval(field_11).state = '0'
    else:
        if eval(field_11).state in ('N', 'n'):
            knight_move(field_11, field_22, ser)
        else:
            regular_move(field_11, field_22, ser)
        eval(field_22).state = eval(field_11).state
        eval(field_11).state = '0'


# def magnet_correction(field_1, field_2, position):
#     diagonal_correction_mm = 2.0
#     correction_mm = 4.0
#     return 0
#     if eval(field_1).X_center != eval(field_2).X_center:
#         if position == 1:
#             if eval(field_2).X_pos > 4:
#                 return diagonal_correction_mm
#             else:
#                 return -diagonal_correction_mm
#         if position == 2:
#             if eval(field_2).Y_pos > 4:
#                 return diagonal_correction_mm
#             else:
#                 return -diagonal_correction_mm
#     elif position == 2 and eval(field_1).X_center == eval(field_2).X_center:
#         return correction_mm if eval(field_1).Y_pos < eval(field_2).Y_pos else -correction_mm
#     elif position == 1 and eval(field_1).Y_center == eval(field_2).Y_center:
#         return correction_mm if eval(field_1).X_pos < eval(field_2).X_pos else -correction_mm
#     else:
#         return 0


def capture(field_2, ser):
    movement(eval(field_2).X_center, eval(field_2).Y_center, 0, ser)
    movement(eval(field_2).X_corner, eval(field_2).Y_corner, 1, ser)
    movement(eval(field_2).X_corner, eval(field_2).Y_dump, 1, ser)
    movement(eval(field_2).X_dump, eval(field_2).Y_dump, 1, ser)


def knight_move(field_1, field_2, ser):
    if eval(field_1).X_pos < eval(field_2).X_pos:
        X_corner_1 = eval(field_1).X_corner_R
        X_corner_2 = eval(field_2).X_corner_L
    else:
        X_corner_1 = eval(field_1).X_corner_L
        X_corner_2 = eval(field_2).X_corner_R

    if eval(field_1).Y_pos < eval(field_2).Y_pos:
        Y_corner_1 = eval(field_1).Y_corner_U
        Y_corner_2 = eval(field_2).Y_corner_D
    else:
        Y_corner_1 = eval(field_1).Y_corner_D
        Y_corner_2 = eval(field_2).Y_corner_U

    movement(eval(field_1).X_center, eval(field_1).Y_center, 0, ser)
    movement(X_corner_1, Y_corner_1, 1, ser)
    movement(X_corner_2, Y_corner_1, 1, ser)
    movement(X_corner_2, Y_corner_2, 1, ser)
    movement(eval(field_2).X_center, eval(field_2).Y_center, 1, ser)


def regular_move(field_1, field_2, ser):
    movement(eval(field_1).X_center, eval(field_1).Y_center, 0, ser)
    movement(eval(field_2).X_center, eval(field_2).Y_center, 1, ser)


def castling_white_short(ser):
    movement(eval("h1").X_center, eval("h1").Y_center, 0, ser)
    movement(eval("f1").X_center, eval("f1").Y_center, 1, ser)
    movement(eval("e1").X_center, eval("e1").Y_center, 0, ser)
    movement(eval("e1").X_corner, eval("e1").Y_corner, 1, ser)
    movement(eval("g1").X_corner_L, eval("g1").Y_corner_U, 1, ser)
    movement(eval("g1").X_center, eval("g1").Y_center, 1, ser)


def castling_white_long(ser):
    movement(eval("a1").X_center, eval("a1").Y_center, 0, ser)
    movement(eval("d1").X_center, eval("d1").Y_center, 1, ser)
    movement(eval("e1").X_center, eval("e1").Y_center, 0, ser)
    movement(eval("e1").X_corner_L, eval("e1").Y_corner_U, 1, ser)
    movement(eval("c1").X_corner, eval("c1").Y_corner, 1, ser)
    movement(eval("c1").X_center, eval("c1").Y_center, 1, ser)


def castling_black_short(ser):
    movement(eval("h8").X_center, eval("h8").Y_center, 0, ser)
    movement(eval("f8").X_center, eval("f8").Y_center, 1, ser)
    movement(eval("e8").X_center, eval("e8").Y_center, 0, ser)
    movement(eval("e8").X_corner, eval("e8").Y_corner, 1, ser)
    movement(eval("g8").X_corner_L, eval("g8").Y_corner_D, 1, ser)
    movement(eval("g8").X_center, eval("g8").Y_center, 1, ser)


def castling_black_long(ser):
    movement(eval("a8").X_center, eval("a8").Y_center, 0, ser)
    movement(eval("d8").X_center, eval("d8").Y_center, 1, ser)
    movement(eval("e8").X_center, eval("e8").Y_center, 0, ser)
    movement(eval("e8").X_corner_L, eval("e8").Y_corner, 1, ser)
    movement(eval("c8").X_corner, eval("c8").Y_corner, 1, ser)


def movement(X, Y, M, ser):
    # print("start")
    ser.write(msg_gen(X, Y, M).encode('ascii'))
    ser.reset_input_buffer()
    time.sleep(1)
    while ser.read().decode('ascii').rstrip() != "1":
        pass


def home(ser):
    ser.write("H1 ".encode('ascii'))
    ser.reset_input_buffer()
    time.sleep(1)
    while ser.read().decode('ascii').rstrip() != "1":
        pass
    # while True:
    #     if ser.readline().decode('ascii').rstrip() == "1":
    #         break
