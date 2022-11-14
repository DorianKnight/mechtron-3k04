#This file is meant to test the serial communications capability of the Simulink model housed on this branch

import serial
ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM7'
ser.open()

if (ser.is_open):
    SYNC = 16
    SetOREcho = 55 #55 for set and 22 for echo
    # Red = 1
    # Blue = 1
    # Green = 1
    LRL = 60
    URL = 120
    atrial_amplitude = 5
    apw = 1
    ventrical_amplitude = 5
    vpw = 1
    arp = 250
    vrp = 320
    activity_threshold = 4
    reaction_time = 30
    response_factor = 8
    recovery_time = 5
    max_sensor_rate = 120
    fixed_AV_delay = 150
    data = bytes([SYNC,SetOREcho,LRL,URL,atrial_amplitude, apw, ventrical_amplitude, vpw, arp, vrp, activity_threshold, reaction_time, response_factor, recovery_time, max_sensor_rate, fixed_AV_delay]) #Creates the message in 5 discrete bytes where each byte can represent a number from 0 to 255 (inclusive)
    ser.write(data)

    if (SetOREcho == 22):
        boardVals = ser.read(31) #Reads the three bytes sent back from the board
        print("Red =",boardVals[0],"Blue =",boardVals[1],"Green =",boardVals[2])
else:
    print("Error with Serial port - port not open")
