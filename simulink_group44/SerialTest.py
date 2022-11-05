#This file is meant to test the serial communications capability of the Simulink model housed on this branch

import serial
ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM7'
ser.open()

if (ser.is_open):
    SYNC = 16
    SetOREcho = 55 #55 for set and 22 for echo
    Red = 1
    Blue = 1
    Green = 1
    data = bytes([SYNC,SetOREcho,Red,Blue,Green]) #Creates the message in 5 discrete bytes where each byte can represent a number from 0 to 255 (inclusive)
    ser.write(data)

    if (SetOREcho == 22):
        boardVals = ser.read(3) #Reads the three bytes sent back from the board
        print("Red =",boardVals[0],"Blue =",boardVals[1],"Green =",boardVals[2])
else:
    print("Error with Serial port - port not open")
