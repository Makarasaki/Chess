#!/usr/bin/env python3
import serial
import time
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()
    c = 0
    while True:
        ser.write(c.encode('ascii'))
        line = ser.readline().decode('utf-8').rstrip()
        c = int(line) + 1
        print(line)
        time.sleep(1)
