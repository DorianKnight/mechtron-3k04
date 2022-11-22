#Author: Group 44
#Date: November 17 2022
#Purpose: To link the DCM and simulink model together through serial communications

import serial
import serial.tools.list_ports
import struct

class SerialObject:
    def __init__(self,commPort):
        self.ser = serial.Serial()
        self.ser.baudrate = 115200 #Sets baud rate
        self.ser.port = commPort #Sets the serial communication port
        ser.open() #Opens the serial port
def SendData(self, patient):
    if (ser.is_open):
        #Set the parameters to bytes and combine into one data structure
        SYNC = struct.pack("B",16)
        SetOrEcho = struct.pack("B",55)
        LRL = struct.pack("B",patient.LRL)
        MSR = struct.pack("B",120)
        aPulseAmp = struct.pack("H",5000)
        aPulseWidth = struct.pack("B",2)
        aSensitivity = struct.pack("H",3500)
        ARP = struct.pack("H",500)
        vPulseAmp = struct.pack("H",5000)
        vPulseWidth = struct.pack("B",2)
        vSensitivity = struct.pack("H",3500)
        VRP = struct.pack("H",150)
        AVDelay = struct.pack("H",350)
        PVARP = struct.pack("H",350)
        ATH = struct.pack("B",4)
        RF = struct.pack("B",16)
        reactionT = struct.pack("B",5)
        recoveryT = struct.pack("B",1)
        mode = struct.pack("B",9)
        #SYNC = (16).to_bytes(1,byteorder='little')
        #SetOrEcho = (55).to_bytes(1,byteorder='little')
        #LRL = (60).to_bytes(1,byteorder='little')
        #MSR = (120).to_bytes(1,byteorder='little')
        #aPulseAmp = (5000).to_bytes(2,byteorder='little')
        #aPulseWidth = (2).to_bytes(1,byteorder='little')
        #aSensitivity = (3500).to_bytes(2,byteorder='little')
        #ARP = (320).to_bytes(2,byteorder='little')
        #vPulseAmp = (5000).to_bytes(2,byteorder='little')
        #vPulseWidth = (2).to_bytes(1,byteorder='little')
        #vSensitivity = (3500).to_bytes(2,byteorder='little')
        #VRP = (150).to_bytes(2,byteorder='little')
        #AVDelay = (150).to_bytes(2,byteorder='little')
        #PVARP = (250).to_bytes(2,byteorder='little')
        #ATH = (1).to_bytes(1,byteorder='little')
        #RF = (16).to_bytes(1,byteorder='little')
        #reactionT = (5).to_bytes(1,byteorder='little')
        #recoveryT = (1).to_bytes(1,byteorder='little')
        #mode = (9).to_bytes(1,byteorder='little')

        data = SYNC + SetOrEcho + LRL + MSR + aPulseAmp + aPulseWidth + aSensitivity + ARP + vPulseAmp + vPulseWidth + vSensitivity + VRP + AVDelay + PVARP + ATH + RF + reactionT + recoveryT + mode

        #Send data to FRDM board
        ser.write(data)

        #If echo, read for echoed params
        if (SetOrEcho == (22).to_bytes(1,byteorder='little')):
            boardVals = ser.read(41) # Reads all the params sent which excludes SYNC and SetOrEcho
            #print("LRL:",boardVals[0],
            #"\nMSR:",boardVals[1],
            #"\naPulseAmp:",int.from_bytes(boardVals[2:4],'little'),
            #"\naPulseWidth:",boardVals[4],
            #"\naSensitivity:",int.from_bytes(boardVals[5:7],'little'),
            #"\nARP:",int.from_bytes(boardVals[7:9],'little'),
            #"\nvPulseAmp:",int.from_bytes(boardVals[9:11],'little'),
            #"\nvPulseWidth:",boardVals[11],
            #"\nvSensitivity:",int.from_bytes(boardVals[12:14],'little'),
            #"\nVRP:",int.from_bytes(boardVals[14:16],'little'),
            #"\nAVDelay:",int.from_bytes(boardVals[16:18],'little'),
            #"\nPVARP:",int.from_bytes(boardVals[18:20],'little'),
            #"\nATH:",boardVals[20],
            #"\nRF:",boardVals[21],
            #"\nreactionT:",boardVals[22],
            #"\nrecoveryT:",boardVals[23],
            #"\nmode:",boardVals[24])
            print("LRL:",boardVals[0],
            "\nMSR:",boardVals[1],
            "\naPulseAmp:",struct.unpack("H", boardVals[2:4])[0],
            "\naPulseWidth:",boardVals[4],
            "\naSensitivity:",struct.unpack("H", boardVals[5:7])[0],
            "\nARP:",struct.unpack("H", boardVals[7:9])[0],
            "\nvPulseAmp:",struct.unpack("H", boardVals[9:11])[0],
            "\nvPulseWidth:",boardVals[11],
            "\nvSensitivity:",struct.unpack("H", boardVals[12:14])[0],
            "\nVRP:",struct.unpack("H", boardVals[14:16])[0],
            "\nAVDelay:",struct.unpack("H", boardVals[16:18])[0],
            "\nPVARP:",struct.unpack("H", boardVals[18:20])[0],
            "\nATH:",boardVals[20],
            "\nRF:",boardVals[21],
            "\nreactionT:",boardVals[22],
            "\nrecoveryT:",boardVals[23],
            "\nmode:",boardVals[24],
            "\nATR_SIGNAL:",struct.unpack("d", boardVals[25:33])[0],
            "\nVENT_SIGNAL:",struct.unpack("d", boardVals[33:41])[0])

    
    else:
        #Display error message saying that the serial port is not open
        pass

print("\n\n\n")
ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM7'
ser.open()
SendData(ser)