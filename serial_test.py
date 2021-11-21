#!/usr/bin/env python3
import serial
import time
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
    ser.reset_input_buffer()
    c = 1
    # print(c)
    print("zaczynamy:")
    while True:
        print(c)
        line = str(c) + "\n"
        ser.write(line.encode('ascii'))

        line = ser.readline().decode('ascii').rstrip()

        if (line == "1"):
            #print("nowa wiadomosc")
            c = c+1
            # print(c)
