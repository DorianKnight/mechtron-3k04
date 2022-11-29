#Author: Group 44
#Date: November 17 2022
#Purpose: To link the DCM and simulink model together through serial communications

import serial
import serial.tools.list_ports
import struct
from tkinter import messagebox
import connectionDisplay
import time
import data as d

def getPortName(): #returns string of port name/code as a string, such as "COM7". string can be passed to SerialObject constructor
    Vid="4966" #same for every pacemaker
    Pid="4117" #same for every pacemaker

    devicelist=serial.tools.list_ports.comports() #make a list of all connections
    port=""
    
    for Device in devicelist: #check if any connection has the pacemaker device attributes
        if(str(Device.vid)==Vid and str(Device.pid)==Pid):
            port=Device.device

    if(port==""):
        print("PORT NOT FOUND")
        connectionDisplay.connectionChecker=False #automatically updates value in connectionDisplay
        connectionDisplay.newDeviceChecker=False

        #throw exception?
    else:
        connectionDisplay.connectionChecker=True
        connectionDisplay.newDeviceChecker=True

    

    return port #return the port name/code of the connection we found

def checkHeartSer():
    Vid="1155"
    Pid="14155"

    devicelist=serial.tools.list_ports.comports() #make a list of all connections
    ser=""
    
    for Device in devicelist: #check if any connection has the pacemaker device attributes
        if(str(Device.vid)==Vid and str(Device.pid)==Pid):
            ser=Device.serial_number

    if(ser==""):
        print("HEART NOT FOUND")
    else:
        DevIsNew=d.DeviceIsNew(ser)
        if DevIsNew:
            connectionDisplay.newDeviceChecker=True
        else:
            connectionDisplay.newDeviceChecker=False
        

class SerialObject:
    def __init__(self):
        print("I've been created")
        self.ser = serial.Serial()
        self.ser.baudrate = 115200 #Sets baud rate
        self.ser.port = getPortName() #Sets the serial communication port
        print(self.ser.port)
        self.opened = False
        try:
            self.ser.open() #Opens the serial port
            self.opened = True
        except Exception as ep:
            print("not plugged in", ep)
        

    def SendData(self, patient):
        print("got here")
        if (self.ser.is_open):
            print("got here and we're open :)")
            #Turn patient parameters into a steam of bytes that can be written to serial
            data = self.PackData(patient) #Data contains a byte stream to set parameters and echo parameters

            #Write data to pacemaker
            self.ser.write(data[0])
            time.sleep(1)
            #Read data from pacemaker
            time.sleep(1)
            self.ser.write(data[1])
            time.sleep(1)
            print("Got to sleep :)")
            boardVals = self.ser.read(41)
            #Process return data into a dictonary (convert the mV into V by dividing by 1000)
            
            returnVals = self.ProcessData(boardVals)
            verified = self.verifyValues(returnVals, patient)

            if (verified == False):
                #Raise error message
                messagebox.showerror(title = "Error", message = "Error transmitting values to board. Please send again as the parameter values on the pacemaker do not match those stored locally.")

            messagebox.showinfo(title = "Confirm", message = "Changes applied to pacemaker device successfully.")
            return returnVals #Returns this data to the DCM so that we can ensure that the values on the board are the same as the values we sent over

        else:
            messagebox.showerror(title = "Error", message = "Serial port is not open")
            #Create an error flag that says that the serial port is not open
            
    def PackData(self,patient):
        
        #Translate pacing mode into an integer recognized by the simulink program
        print(patient.pacingMode)
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

        #Translating the activity threshold to an integer recognized by python
        match patient.actThr:
            case "V-Low":
                activityThresh = 1
            case "Low":
                activityThresh = 2
            case "Med-Low":
                activityThresh = 3
            case "Med":
                activityThresh = 4
            case "Med-High":
                activityThresh = 5
            case "High":
                activityThresh = 6
            case "V-High":
                activityThresh = 7


        #Pack the patient programmable parameters into bytes
        SYNC = struct.pack("B",16)
        set = struct.pack("B",55)
        echo = struct.pack("B",22)
        LRL = struct.pack("B",patient.lrl)
        MSR = struct.pack("B",patient.maxSensRate)
        aPulseAmp = struct.pack("H",int(patient.aamp*1000))
        aPulseWidth = struct.pack("B",patient.apw)
        aSensitivity = struct.pack("H",int(patient.asens*1000))
        ARP = struct.pack("H",patient.arp)
        vPulseAmp = struct.pack("H",int(patient.vamp*1000))
        vPulseWidth = struct.pack("B",patient.vpw)
        vSensitivity = struct.pack("H",int(patient.vsens*1000))
        VRP = struct.pack("H",patient.vrp)
        AVDelay = struct.pack("H",patient.fixedAVdelay)
        PVARP = struct.pack("H",patient.pvarp)
        ATH = struct.pack("B",activityThresh)
        RF = struct.pack("B",patient.respFactor)
        reactionT = struct.pack("B",patient.reactTime)
        recoveryT = struct.pack("B",patient.recoveryTime)
        mode = struct.pack("B",pacingMode)

        #Collate data into a series of bytes that can be sent to the DCM
        setParams = SYNC + set + LRL + MSR + aPulseAmp + aPulseWidth + aSensitivity + ARP + vPulseAmp + vPulseWidth + vSensitivity + VRP + AVDelay + PVARP + ATH + RF + reactionT + recoveryT + mode
        echoParams = SYNC + echo + LRL + MSR + aPulseAmp + aPulseWidth + aSensitivity + ARP + vPulseAmp + vPulseWidth + vSensitivity + VRP + AVDelay + PVARP + ATH + RF + reactionT + recoveryT + mode

        return [setParams,echoParams]
    
    def ProcessData(self,boardVals):
        #Take bytestream received and process the raw data into an easily accessable dictionary
        lrl = boardVals[0]
        maxSensRate = boardVals[1]
        aamp = (struct.unpack("H", boardVals[2:4])[0])/1000 #mV to V
        apw = boardVals[4]
        asens = (struct.unpack("H", boardVals[5:7])[0])/1000
        arp = struct.unpack("H", boardVals[7:9])[0]
        vamp = (struct.unpack("H", boardVals[9:11])[0])/1000
        vpw = boardVals[11]
        vsens = (struct.unpack("H", boardVals[12:14])[0])/1000
        vrp = struct.unpack("H", boardVals[14:16])[0]
        fixedAVdelay = struct.unpack("H", boardVals[16:18])[0]
        pvarp = struct.unpack("H", boardVals[18:20])[0]
        actThr = boardVals[20]
        respFactor = boardVals[21]
        reactTime = boardVals[22]
        recoveryTime = boardVals[23]
        pacingMode = boardVals[24]
        egramsAtrial =struct.unpack("d", boardVals[25:33])[0] *5000 #Converting to mV
        egramsVentricular = struct.unpack("d", boardVals[33:41])[0] *5000 #Converting to mV

        match pacingMode:
            case 1:
                mode = "AOO"
            case 2:
                mode = "AOOR"
            case 3:
                mode = "AAI"
            case 4:
                mode = "AAIR"
            case 5:
                mode = "VOO"
            case 6:
                mode = "VOOR"
            case 7:
                mode = "VVI"
            case 8:
                mode = "VVIR"
            case 9:
                mode = "DDD"
            case 10:
                mode = "DDDR"

        match actThr:
            case 1:
                activityThresh = 'V-Low'
            case 2:
                activityThresh = 'Low'
            case 3:
                activityThresh= 'Med-Low'
            case 4:
                activityThresh = 'Med'
            case 5:
                activityThresh = 'Med-High'
            case 6:
                activityThresh = 'High'
            case 7:
                activityThresh = "V-High"
                
        returnData = {
            'lrl':lrl,
            'maxSensRate':maxSensRate,
            'aamp':aamp,
            'apw':apw,
            'asens':asens,
            'arp':arp,
            'vamp':vamp,
            'vpw':vpw,
            'vsens':vsens,
            'vrp':vrp,
            'fixedAVdelay':fixedAVdelay,
            'pvarp':pvarp,
            'actThr':activityThresh,
            'respFactor':respFactor,
            'reactTime':reactTime,
            'recoveryTime':recoveryTime,
            'pacingMode':mode,
            'egramsAtrial':egramsAtrial,
            'egramsVentricular':egramsVentricular}

        return returnData #Returns this data to the DCM so that we can ensure that the values on the board are the same as the values we sent over
    
    
    def ReceiveEgramsData(self, patient):
        #This function does the same work as the SendData(self, patient) function however instead of setting parameter and echoing, this method only echoes so that we can minimize the workload on the pacemaker and increase the efficiency of the code
        if (self.ser.is_open):
            #Turn patient parameters into a steam of bytes that can be written to serial
            data = self.PackData(patient) #Data contains a byte stream to set parameters and echo parameters

            #Read data from pacemaker
            self.ser.write(data[1])
            boardVals = self.ser.read(41)
            #Process return data into a dictonary (convert the mV into V by dividing by 1000)
            egramsData = self.ProcessEgramsData(boardVals)
            return egramsData
        else:
            #Create an error flag that says that the serial port is not open
            pass
    
        
    def ProcessEgramsData(self,boardVals):
        #Take bytestream received and process the raw data into an easily accessable dictionary
        #This is a separate method to help reduce the strain on the computer
        
        egramsAtrial =struct.unpack("d", boardVals[25:33])[0] *5000 #Converting to mV
        egramsVentricular = struct.unpack("d", boardVals[33:41])[0] *5000 #Converting to mV

        egramsData = {
            'egramsAtrial':egramsAtrial,
            'egramsVentricular':egramsVentricular}
        return egramsData

    def verifyValues(self, valDict, patient): 
        
        if (patient.lrl != valDict["lrl"]):
            return False
        if (patient.maxSensRate != valDict["maxSensRate"]):
            return False
        if (patient.aamp != valDict["aamp"]):
            return False
        if (patient.apw != valDict["apw"]):
            return False
        if (patient.asens != valDict["asens"]):
            return False
        if (patient.arp != valDict["arp"]):
            return False
        if (patient.vamp != valDict["vamp"]):
            return False
        if (patient.vpw != valDict["vpw"]):
            return False
        if (patient.vsens != valDict["vsens"]):
            return False
        if (patient.fixedAVdelay != valDict["fixedAVdelay"]):
            return False
        if (patient.pvarp != valDict["pvarp"]):
            return False
        if (patient.actThr != valDict["actThr"]):
            return False
        if (patient.respFactor != valDict["respFactor"]):
            return False
        if (patient.reactTime != valDict["reactTime"]):
            return False
        if (patient.recoveryTime != valDict["recoveryTime"]):
            return False
        if (patient.pacingMode != valDict["pacingMode"]):
            return False
        return True