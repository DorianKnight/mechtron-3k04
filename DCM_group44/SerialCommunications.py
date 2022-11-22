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
        self.ser.open() #Opens the serial port
    def SendData(self, patient):
        if (self.ser.is_open):
            #Turn patient parameters into a steam of bytes that can be written to serial
            data = self.PackData(patient) #Data contains a byte stream to set parameters and echo parameters

            #Write data to pacemaker
            self.ser.write(data[0])

            #Read data from pacemaker
            self.ser.write(data[1])
            returnData = self.ser.read(41)

            
            
            #Process return data into a dictonary here later when you have time also make sure to convert the mV into V by dividing by 1000
            

            return returnData #Returns this data to the DCM so that we can ensure that the values on the board are the same as the values we sent over
        else:
            #Create an error flag that says that the serial port is not open
            pass
    def PackData(self,patient):
        
        #Translate pacing mode into an integer recognized by the simulink program
        pacingMode = 0 #Initalizing here such that the variable is within scope to the rest of the PackData method
        match patient.pacingMode:
            case "AOO":
                pacingMode = 1
            case "AOOR":
                pacingMode = 2
            case "AAI":
                pacingMode = 3
            case "AAIR":
                pacingMode = 4
            case "VOO":
                pacingMode = 5
            case "VOOR":
                pacingMode = 6
            case "VVI":
                pacingMode = 7
            case "VVIR":
                pacingMode = 8
            case "DDD":
                pacingMode = 9
            case "DDDR":
                pacingMode = 10


        #Pack the patient programmable parameters into bytes
        SYNC = struct.pack("B",16)
        set = struct.pack("B",55)
        echo = struct.pack("B",22)
        LRL = struct.pack("B",patient.lrl)
        MSR = struct.pack("B",patient.maxSensRate)
        aPulseAmp = struct.pack("H",patient.aamp*1000)
        aPulseWidth = struct.pack("B",patient.apw)
        aSensitivity = struct.pack("H",patient.asens*1000)
        ARP = struct.pack("H",patient.arp)
        vPulseAmp = struct.pack("H",patient.vamp*1000)
        vPulseWidth = struct.pack("B",patient.vpw)
        vSensitivity = struct.pack("H",patient.vsens*1000)
        VRP = struct.pack("H",patient.vrp)
        AVDelay = struct.pack("H",patient.fixedAVdelay)
        PVARP = struct.pack("H",patient.pvarp)
        ATH = struct.pack("B",patient.actThr)
        RF = struct.pack("B",patient.respFactor)
        reactionT = struct.pack("B",patient.reactTime)
        recoveryT = struct.pack("B",patient.recoveryTime)
        mode = struct.pack("B",pacingMode)

        #Collate data into a series of bytes that can be sent to the DCM
        setParams = SYNC + set + LRL + MSR + aPulseAmp + aPulseWidth + aSensitivity + ARP + vPulseAmp + vPulseWidth + vSensitivity + VRP + AVDelay + PVARP + ATH + RF + reactionT + recoveryT + mode
        echoParams = SYNC + echo + LRL + MSR + aPulseAmp + aPulseWidth + aSensitivity + ARP + vPulseAmp + vPulseWidth + vSensitivity + VRP + AVDelay + PVARP + ATH + RF + reactionT + recoveryT + mode

        return [setParams,echoParams]