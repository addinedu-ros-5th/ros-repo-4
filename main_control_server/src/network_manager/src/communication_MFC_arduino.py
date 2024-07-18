#!/usr/bin/env python3

import serial
import time

def main():
    port = '/dev/rfcomm0'
    baud_rate = 9600  # 아두이노와 동일한 통신 속도

    try:
        ser = serial.Serial(port, baud_rate)
        print(f"Connected to {port} at {baud_rate} baud rate.")
    except serial.SerialException as e:
        print(f"Failed to connect to {port}: {e}")
        exit()

    try:
        while True:
            if ser.in_waiting > 0:
                data = ser.readline().decode('utf-8').rstrip()
                print(f"Received from Arduino: {data}")

            message = input("Send a number to Arduino: ")
            if message.isdigit():  # 입력이 숫자인지 확인
                ser.write((message + '\n').encode('utf-8'))
            else:
                print("Please enter a valid number.")

    except KeyboardInterrupt:
        print("Exiting program.")
    finally:
        ser.close()
        print("Serial port closed.")

if __name__ == "__main__":
    main()