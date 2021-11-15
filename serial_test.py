#!/usr/bin/env python3
import serial
import time
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()
    c = 1
    print(c)
    print("zaczynamy:")
    while True:
        #c = 1
        line = str(c)  # + "\n"
        ser.write(line.encode('ascii'))

        line = ser.readline().decode('ascii').rstrip()

        if (line == "1"):
            # print(line)
            print("nowa wiadomosc")
            #c = int(line)
            c = c+1
            print(c)
            #c = c + 1
            # print(c)
            # time.sleep(1)
