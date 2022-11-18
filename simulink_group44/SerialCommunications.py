#Author: Group 44
#Date: November 17 2022
#Purpose: To link the DCM and simulink model together through serial communications

import serial

def SendData(ser):
    if (ser.is_open):
        #Set the parameters to bytes and combine into one data structure
        SYNC = (16).to_bytes(1,byteorder='little')
        SetOrEcho = (55).to_bytes(1,byteorder='little')
        LRL = (90).to_bytes(1,byteorder='little')
        MSR = (120).to_bytes(1,byteorder='little')
        aPulseAmp = (4000).to_bytes(2,byteorder='little')
        aPulseWidth = (1).to_bytes(1,byteorder='little')
        aSensitivity = (2700).to_bytes(2,byteorder='little')
        ARP = (100).to_bytes(2,byteorder='little')
        vPulseAmp = (3000).to_bytes(2,byteorder='little')
        vPulseWidth = (1).to_bytes(1,byteorder='little')
        vSensitivity = (2500).to_bytes(2,byteorder='little')
        VRP = (320).to_bytes(2,byteorder='little')
        AVDelay = (150).to_bytes(2,byteorder='little')
        PVARP = (250).to_bytes(2,byteorder='little')
        ATH = (8).to_bytes(1,byteorder='little')
        RF = (8).to_bytes(1,byteorder='little')
        reactionT = (5).to_bytes(1,byteorder='little')
        recoveryT = (1).to_bytes(1,byteorder='little')
        mode = (9).to_bytes(1,byteorder='little')

        data = SYNC + SetOrEcho + LRL + MSR + aPulseAmp + aPulseWidth + aSensitivity + ARP + vPulseAmp + vPulseWidth + vSensitivity + VRP + AVDelay + PVARP + ATH + RF + reactionT + recoveryT + mode

        #Send data to FRDM board
        ser.write(data)

        #If echo, read for echoed params
        if (SetOrEcho == (22).to_bytes(1,byteorder='little')):
            boardVals = ser.read(25) # Reads all the params sent which excludes SYNC and SetOrEcho
            print("LRL:",boardVals[0],
            "\nMSR:",boardVals[1],
            "\naPulseAmp:",int.from_bytes(boardVals[2:4],'little'),
            "\naPulseWidth:",boardVals[4],
            "\naSensitivity:",int.from_bytes(boardVals[5:7],'little'),
            "\nARP:",int.from_bytes(boardVals[7:9],'little'),
            "\nvPulseAmp:",int.from_bytes(boardVals[9:11],'little'),
            "\nvPulseWidth:",boardVals[11],
            "\nvSensitivity:",int.from_bytes(boardVals[12:14],'little'),
            "\nVRP:",int.from_bytes(boardVals[14:16],'little'),
            "\nAVDelay:",int.from_bytes(boardVals[16:18],'little'),
            "\nPVARP:",int.from_bytes(boardVals[18:20],'little'),
            "\nATH:",boardVals[20],
            "\nRF:",boardVals[21],
            "\nreactionT:",boardVals[22],
            "\nrecoveryT:",boardVals[23],
            "\nmode:",boardVals[24])

    
    else:
        #Display error message saying that the serial port is not open
        pass

print("\n\n\n")
ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM7'
ser.open()
SendData(ser)