from tkinter import messagebox
from enum import Enum
import data
import sqlite3

# defines accepted range for all parameters
lrl_range1 = [30,50]
lrl_range2 = [50,90]
lrl_range3 = [90,175]
url_range = [50,175]
apw_range = [1,30]
vpw_range = [1,30]
aamp_range = [0,5]
vamp_range = [0,5]
asens_range = [0,5]
vsens_range = [0,5]
arp_range = [150,500]
vrp_range = [150,500]
pvarp_range = [150,500]
actThr_range = ["V-Low", "Low", "Med-Low", "Med", "Med-High","High","V-High"]
reactTime_range = [10,50]
respFactor_range = [1,16]
recoveryTime_range = [2,16]
maxSensRate_range = [50,175]
fixedAVdelay_range = [70,300]

# defines accepted increments for all parameters
lrl_r1_inc = 5
lrl_r2_inc = 1
lrl_r3_inc = 5
url_inc = 5
apw_inc = 1
vpw_inc = 1
aamp_inc = 0.1
vamp_inc = 0.1
asens_inc = 0.1
vsens_inc = 0.1
arp_inc = 10
vrp_inc = 10
pvarp_inc = 10
reactTime_inc = 10
respFactor_inc = 1
recoveryTime_inc = 1
maxSensRate_inc = 5
fixedAVdelay_inc = 10

errorTolerance = 0.00000001 #This is a value to account for the inaccuracy of computer calculations (specifically modulo of floats)

# determines whether number N is within range [smallNum, bigNum]
def isBetween(N, smallNum, bigNum):
    return smallNum <= N <= bigNum

class Params(Enum): 
    LRL = 1
    URL = 2
    APW = 3
    VPW = 4
    AAMP = 5
    VAMP = 6
    ASENS = 7
    VSENS = 8
    ARP = 9
    VRP = 10
    PVARP = 11
    ACTTHR = 12
    REACTTIME = 13
    RESPFACTOR = 14
    RECOVERYTIME = 15
    MAXSENSRATE = 16
    FIXEDAVDELAY = 17
    
class Errors(Enum): 
    TYPE = 1
    RANGE = 2
    INCREMENT = 3
    INVALID = 4


class Patient:
    # initializes patient with nominal values
    def __init__(self):
        self.username="NONE"

        self.lrl = 60
        self.url = 120
        self.pacingMode = "DDD"
        self.apw = 1
        self.vpw = 1
        self.aamp = 5
        self.vamp = 5
        self.asens = 2.5 #set to 2.5 instead of 0.75 since the latter contradicts increment restrictions
        self.vsens = 2.5
        self.arp = 250
        self.vrp = 320
        self.pvarp = 250
        self.actThr = "Med"
        self.reactTime = 30
        self.respFactor = 8
        self.recoveryTime = 5
        self.maxSensRate = 120
        self.fixedAVdelay = 150
        
        self.errors = []
        
    #Returns each of the increments for each of the parameters
    def getInc(self, param, range): 
        match param: 
            case "LRL": 
                if(range == 1): 
                    return lrl_r1_inc
                elif(range == 3): 
                    return lrl_r3_inc 
            case "URL": 
                return url_inc
            case "APW": 
                return apw_inc
            case "AAmp": 
                return aamp_inc
            case "VPW": 
                 return vpw_inc
            case "VAmp":  
                return vamp_inc
            case "ASens":
                return asens_inc
            case "ARP": 
                return arp_inc
            case "PVARP": 
                return pvarp_inc
            case "VSens": 
                return vsens_inc
            case "VRP": 
                return vrp_inc
            case "Reaction Time": 
                return reactTime_inc
            case "Response Factor": 
                return respFactor_inc 
            case "Recovery Time": 
                return recoveryTime_inc
            case "Max Sensor Rate": 
                return maxSensRate_inc
            case "Fixed AV Delay": 
                return fixedAVdelay_inc

    #Returns each of the ranges for each of the parameters (highest and lowest accepted values)    
    def getRange(self, param): 
        returnVal = []
        match param: 
            case "LRL": 
                returnVal.append(lrl_range1[0])
                returnVal.append(lrl_range3[1])
            case "URL": 
                returnVal =  url_range
            case "APW": 
                returnVal =  apw_range
            case "AAmp": 
                returnVal =  aamp_range
            case "VPW": 
                 returnVal =  vpw_range
            case "VAmp": 
                returnVal =  vamp_range
            case "ASens": 
                returnVal =  asens_range
            case "ARP": 
                returnVal =  arp_range
            case "PVARP": 
                returnVal =  pvarp_range
            case "VSens": 
                returnVal =  vsens_range
            case "VRP": 
                returnVal =  vrp_range
            case "Reaction Time": 
                returnVal =  reactTime_range
            case "Response Factor": 
                returnVal =  respFactor_range
            case "Recovery Time": 
                returnVal =  recoveryTime_range
            case "Max Sensor Rate": 
                returnVal =  maxSensRate_range
            case "Fixed AV Delay": 
                returnVal =  fixedAVdelay_range
        return returnVal
            
    def getType(self, param): 
        if(param == "LRL" or param == "URL" or param == "ARP" or param == "VRP" or param == "APW" or param == "VPW"  or param == "Reaction Time" or param == "Response Factor" or param == "Reaction Time" or param == "Response Factor" or param == "Recovery Factor" or param == "Recovery Time" or param == "Maximum Sensor Rate"):
            return "int"
        elif(param == "AAmp" or param == "VAmp" or param == "ASens" or param == "VSens" or param == "Fixed AV Delay"): 
            return "float"

    #Adding errors to the list of the all errors related to input variables - if range is not given, just give a value of 1 to avoid errors
    def addError(self, param, error, range = 1): 
        print(f'param: {param} & error: {error} & error = Type: {error == "Type"}')
        if(error == "Type"): 
            accType = self.getType(param)
            self.errors.append(f'Invalid type for {param}. {param} should be of type {accType}')
        elif(error == "Range"): 
            accRange = self.getRange(param)
            print(f'accRange: {accRange}')
            self.errors.append(f'{param} input out of range. Range should be {accRange[0]} to {accRange[1]}')
        elif(error == "Increment"): 
            inc = str(self.getInc(param, range))
            self.errors.append(f'Invalid increment for {param}. Value should be in increments of {inc}')
        elif(error == "Invalid"): 
            if(param == "URL"): 
                self.errors.append(f'Invalid URL. Inputted URL is less than the LRL. Please enter a URL greater than {self.lrl}.')
            if(param == "ARP"): 
                self.errors.append(f'Atrial Refractory Period cannot be greater than the time between pulses determined by the LRL')
            if(param == "VRP"): 
                self.errors.append(f'Ventricular Refractory Period cannot be greater than the time between pulses determined by the LRL')
                
    def displayErrors(self): 
        totalErrorMsg = "" 
        print(f'self.errors: {self.errors} & length: {len(self.errors)}')
        for i in self.errors: 
            totalErrorMsg += i
            totalErrorMsg += "\n"
 
        print(totalErrorMsg)
        messagebox.showerror(title = "Error", message = totalErrorMsg)

    def isValidIncrement(self, value, increment):
        return (value % increment < errorTolerance) or (abs((value % increment) - increment) < errorTolerance)
        
    
    def checkLRL(self):
        #Checking Lower Rate Limit
        try: 
            self.lrl = int(self.lrl)
            print(f'Type of self.lrl: {type(self.lrl)}')
            if(isBetween(self.lrl,lrl_range1[0],lrl_range1[1])): #Checks if the LRL is in the first range (30 - 50 ppm)
                if(not self.isValidIncrement(self.lrl,lrl_r1_inc)): #Checks the increment for this range
                    self.addError("LRL", "Increment", 1)
                    return False
            elif(isBetween(self.lrl, lrl_range2[0], lrl_range2[1])): #Checks if the LRL is in the second range (50 - 90 ppm) 
                pass #If self.lrl is an integer in this range, it is valid because the increments are by 1
            elif(isBetween(self.lrl, lrl_range3[0], lrl_range3[1])): #Checks if the LRL is in the third range (90 - 175 ppm)
                if(not self.isValidIncrement(self.lrl, lrl_r3_inc)):  #Checks increment for this range
                    self.addError("LRL", "Increment", 3)
                    return False
            else: 
                self.addError("LRL", "Range") #If the LRL value is not in any range, add an error
                return False
        except: 
            self.addError("LRL", "Type") #If it gets here there is most probably a type error (can't convert the input to an int)
            return False

    def checkURL(self): 
        #Checking Upper Rate Limit
        try: 
            self.url = int(self.url)
            if(isBetween(self.url,url_range[0],url_range[1])): #Checks if the URL value is within the valid range
                if(not self.isValidIncrement(self.url,url_inc)): #Checks the increment 
                    self.addError("URL", "Increment")
                    return False
                if(self.url <= self.lrl): 
                    self.addError("URL", "Invalid") #Checks to make sure that the URL value is not greater than the LRL value
                    return False
            else: 
                self.addError("URL", "Range") #If it gets here, the URL is outside of the valid range
                return False
        except: 
            self.addError("URL", "Type") #If it gets here there is probably an error converting to an int
            return False
        return True
    
    def checkAPW(self): 
        #Checking Atrial Pulse Width
        try: 
            self.apw = int(self.apw)
            if(isBetween(self.apw,apw_range[0],apw_range[1])): #Checks APW range
                if(not self.isValidIncrement(self.apw, apw_inc)): #Checks the increment
                    self.addError("APW", "Increment")
                    return False
            else: 
                self.addError("APW", "Range") #If it gets here, APW is outside of the valid range
                return False
        except: 
            self.addError("APW", "Type") #If it gets here, APW is not able to be converted to an int
            return False

    def checkAAmp(self): 
        #Checking Atrial Amplitude
        try: 
            self.aamp = float(self.aamp)
            if(isBetween(self.aamp,aamp_range[0],aamp_range[1])): #Checks to ensure Atrial Amp is within the valid range
                if(not self.isValidIncrement(self.aamp, aamp_inc)): #Checks the increment
                    self.addError("AAmp", "Increment")
                    return False 
            else: 
                self.addError("AAmp", "Range") #If it gets here APW out of valid range 
                return False
        except: 
            self.addError("AAmp", "Type") #If it gets here, APW not able to be converted to a float
            return False
    
    def checkVPW(self): 
        #Checking Ventricular Pulse Width
        try: 
            self.vpw = int(self.vpw)
            if(isBetween(self.vpw,vpw_range[0],vpw_range[1])): #Checks if VPW in valid range
                if(not self.isValidIncrement(self.vpw, vpw_inc)): #Checks if VPW is on an expected increment
                    self.addError("VPW", "Increment")
                    return False
            else: 
                self.addError("VPW", "Range") #Throws an error for out of range
                return False
        except: 
            self.addError("VPW", "Type") #Throws a type error as VPW not able to be converted to an int
            return False
        
    def checkVAmp(self): 
        #Checking Ventricular Amplitude
        try: 
            self.vamp = float(self.vamp)
            if(isBetween(self.vamp,vamp_range[0],vamp_range[1])): #Checks Vent Amp in valid range
                if(not self.isValidIncrement(self.vamp, vamp_inc)): #Checks VAmp on a valid increment 
                    self.addError("VAmp", "Increment")
                    return False
            else: 
                self.addError("VAmp", "Range") #Throws out of range error
                return False
        except: 
            self.addError("VAmp", "Type") #Throws incorrect type error (not able to be converted to a float)
            return False

    def checkASens(self): 
        #Checking Atrial Sensitivity
        try: 
            self.asens = float(self.asens)
            if(isBetween(self.asens,asens_range[0],asens_range[1])): #Ensures Atr Sensitivity in valid range
                if(not self.isValidIncrement(self.asens, asens_inc)): #Checks that ASens on expected increment 
                    self.addError("ASens", "Increment")
                    return False 
            else: 
                self.addError("ASens", "Range") #Throws out of range error
                return False
        except: 
            self.addError("ASens", "Type") #Throws incorrect type error (not able to be converted to a float)
            return False

    def checkARP(self): 
        #Checking Atrial Refractory Period
        try: 
            self.arp = int(self.arp)
            if(isBetween(self.arp,arp_range[0],arp_range[1])): #Checks that ARP in valid range  
                if(not self.isValidIncrement(self.arp,arp_inc)): #Checks if ARP is on a valid increment 
                    self.addError("ARP", "Increment") 
                    return False
                lrlTime = (1/self.lrl)*1000*60 #The time between pulses in ms
                if(self.arp > lrlTime): #Checks to make sure that ARP is not greater than the time between pulses 
                    self.addError("ARP", "Invalid")
                    return False
            else: 
                self.addError("ARP", "Range") #Throws out of range error
                return False
        except: 
            self.addError("ARP", "Type") #Throws type error as ARP not able to be converted to an int
            return False
        return True

    def checkPVARP(self): 
        #Checking PVARP
        try: 
            self.pvarp = int(self.pvarp)
            if(isBetween(self.pvarp,pvarp_range[0],pvarp_range[1])): #Checks that PVARP in valid range
                if(not self.isValidIncrement(self.pvarp,pvarp_inc)): #Checks that PVARP is on a valid increment
                    self.addError("PVARP", "Increment")
                    return False
            else: 
                self.addError("PVARP", "Range") #Throws out of range error
                return False
        except: 
            self.addError("PVARP", "Type") #Throws incorrect type error as PVARP not able to be converted to an int
            return False
        return True       

    def checkVSens(self): 
        #Checking Ventricular Sensitivity
        try: 
            self.vsens = float(self.vsens)
            if(isBetween(self.vsens,vsens_range[0],vsens_range[1])): #Checks that VSens is within the valid range
                if(not self.isValidIncrement(self.vsens, vsens_inc)): #Checks that VSens is on a valid increment
                    self.addError("VSens", "Increment")
                    return False 
            else: 
                self.addError("VSens", "Range") #Throws out of range error
                return False
        except: 
            self.addError("VSens", "Type") #Throws incorrect type error from vsens not being able to convert to a float
            return False

    def checkVRP(self): 
        #Checking VRP
        try: 
            self.vrp = int(self.vrp)
            if(isBetween(self.vrp,vrp_range[0],vrp_range[1])): #Checks that VRP is within the valid range 
                if(not self.isValidIncrement(self.vrp,vrp_inc)): #Checks that VRP is on a valid increment
                    self.addError("VRP", "Increment")
                    return False
                lrlTime = (1/self.lrl)*1000*60 #The time between pulses in ms
                if(self.vrp > lrlTime): 
                    self.addError("VRP", "Invalid") #Checks that the VRP is not greater than the time between pulses
                    return False
            else: 
                self.addError("VRP", "Range") #Throws out of range error
                return False
        except: 
            self.addError("VRP", "Type") #Throws incorrect type error as VRP not able to be converted to an int
            return False
        return True

    def checkActThr(self): 
        #Checking activity threshold
        found=False
        for item in actThr_range: #Sees if self.actThr is in the list of valid values
            if(self.actThr == item):
                found=True
        return found


    def checkReactTime(self):
        #Checking reaction time
        try: 
            self.reactTime = int(self.reactTime)
            if(isBetween(self.reactTime,reactTime_range[0],reactTime_range[1])): #Checks that the reaction time is within the valid range
                if(not self.isValidIncrement(self.reactTime,reactTime_inc)): #Checks that the reaction time is on a valid increment
                    self.addError("Reaction Time", "Increment")
                    return False
            else: 
                self.addError("Reaction Time", "Range") #Throws out of range error
                return False
        except: 
            self.addError("Reaction Time", "Type") #Throws incorrect type error
            return False
        return True

    def checkRespFactor(self):
        try: 
            self.respFactor = int(self.respFactor)
            if(isBetween(self.respFactor,respFactor_range[0],respFactor_range[1])): #Checks that the resp factor is in the valid range 
                if(not self.isValidIncrement(self.respFactor,respFactor_inc)): #Checks that the resp factor is on a valid increment 
                    self.addError("Response Factor", "Increment")
                    return False
            else: 
                self.addError("Response Factor", "Range") #Throws out of range error
                return False
        except: 
            self.addError("Response Factor", "Type") #Throws incorrect type erorr from not being able to convert to an int
            return False
        return True

    def checkRecoveryTime(self):
        #Checking recovery time
        try: 
            self.recoveryTime = int(self.recoveryTime)
            if(isBetween(self.recoveryTime,recoveryTime_range[0],recoveryTime_range[1])): #Checks that recovery time is within the valid range 
                if(not self.isValidIncrement(self.recoveryTime,recoveryTime_inc)): #Checks that recovery time is on a valid increment
                    self.addError("Recovery Time", "Increment")
                    return False
            else: 
                self.addError("Recovery Time", "Range") #Throws out of range error
                return False
        except: 
            self.addError("Recovery Time", "Type") #Throws inocrrect type error from not being able to convert to an int
            return False
        return True

    def checkMaxSensRate(self):
        #Checking Max Sensor Rate
        try: 
            self.maxSensRate = int(self.maxSensRate)
            if(isBetween(self.maxSensRate,maxSensRate_range[0],maxSensRate_range[1])): #Checks that MaxSensRate is within the valid range
                if(not self.isValidIncrement(self.maxSensRate,maxSensRate_inc)): #Checks that MaxSensRate is on a valid increment 
                    self.addError("Max Sensor Rate", "Increment")
                    return False
            else: 
                self.addError("Max Sensor Rate", "Range") #Throws out of range error
                return False
        except: 
            self.addError("Max Sensor Rate", "Type") #Throws incorrect type error if not able to convert to int
            return False
        return True

    def checkFixedAVdelay(self):
        #Checking Fixed AV Delay
        try: 
            self.fixedAVdelay = int(self.fixedAVdelay)
            if(isBetween(self.fixedAVdelay,fixedAVdelay_range[0],fixedAVdelay_range[1])): #Checks that Fixed AV Delay within the valid range 
                if(not self.isValidIncrement(self.fixedAVdelay,fixedAVdelay_inc)): #Checks that Fixed AV Delay falls on a valid increment 
                    self.addError("Fixed AV Delay", 'Increment')
                    return False
            else: 
                self.addError("Fixed AV Delay", "Range") #Throws out of range error
                return False
        except: 
            self.addError("Fixed AV Delay", "Type") #Throws incorrect type error from not being able to convert to int
            return False
        return True
    

    def numsValid(self,pMode): #the patient default values would be nominal values and wouldn't change unless there are relevant entries in that window. we could check for everything for every mode?? if we agree, we can take out the "mode" argument and take out commented code.
       
        valid = True #Variable to keep track if the inputs are valid
        
        # Checking validity of universal  parameters
        if(self.checkLRL() == False): 
            valid = False
        if(self.checkURL() == False): 
            valid = False
        
        #Checking validity of input parameters for AOO
        if(pMode=="AOO"):

            if(self.checkAPW() == False): 
                valid = False 
                
            if(self.checkAAmp() == False): 
                valid = False
            
        #Checking validity of input parameteres for VOO
        elif(pMode=="VOO"):
            
            if(self.checkVPW() == False): 
                valid = False

            if(self.checkVAmp() == False):
                valid = False

        #Checking validity of input parameters for AAI
        elif(pMode=="AAI"):
            
            if(self.checkAPW() == False):
                valid = False
            
            if(self.checkAAmp() == False):
                valid = False
            
            if(self.checkASens() == False): 
                valid = False
            
            if(self.checkARP() == False): 
                valid =  False
            
        #Checking validity of input parameters for VVI
        elif(pMode=="VVI"):
            
            if(self.checkVPW() == False):
                valid = False
            
            if(self.checkVAmp() == False): 
                valid = False

            if(self.checkVSens() == False): 
                valid = False 
            
            if(self.checkVRP() == False): 
                valid = False

        #Checking validity of input parameters for AOOR
        elif(pMode=="AOOR"):

            if(self.checkAPW() == False):
                valid = False
            
            if(self.checkAAmp() == False):
                valid =  False
            
            if(self.checkActThr() == False):
                valid = False

            if(self.checkReactTime() == False):
                valid = False

            if(self.checkRespFactor() == False):
                valid = False

            if(self.checkRecoveryTime() == False):
                valid = False

            if(self.checkMaxSensRate() == False):
                valid = False
            
        #Checking validity of input parameteres for VOOR
        elif(pMode=="VOOR"):
            
            if(self.checkVPW() == False): 
                valid = False

            if(self.checkVAmp() == False):
                valid = False

            if(self.checkActThr() == False):
                valid = False

            if(self.checkReactTime() == False):
                valid =  False

            if(self.checkRespFactor() == False):
                valid = False

            if(self.checkRecoveryTime() == False):
                valid = False

            if(self.checkMaxSensRate() == False):
                valid = False

        #Checking validity of input parameters for AAIR
        elif(pMode=="AAIR"):
            
            if(self.checkAPW() == False):
                valid = False
            
            if(self.checkAAmp() == False):
                valid = False
            
            if(self.checkASens() == False): 
                valid =  False
            
            if(self.checkARP() == False): 
                valid = False

            if(self.checkActThr() == False):
                valid = False

            if(self.checkReactTime() == False):
                valid =  False

            if(self.checkRespFactor() == False):
                valid = False

            if(self.checkRecoveryTime() == False):
                valid = False

            if(self.checkMaxSensRate() == False):
                valid = False
            
            

        #Checking validity of input parameters for VVIR
        elif(pMode=="VVIR"):
            
            if(self.checkVPW() == False):
                valid = False
            
            if(self.checkVAmp() == False): 
                valid =  False

            if(self.checkVSens() == False): 
                valid =  False 
            
            if(self.checkVRP() == False): 
                valid = False

            if(self.checkActThr() == False):
                valid = False

            if(self.checkReactTime() == False):
                valid = False

            if(self.checkRespFactor() == False):
                valid =  False

            if(self.checkRecoveryTime() == False):
                valid = False

            if(self.checkMaxSensRate() == False):
                valid = False
        
        elif(pMode=="DDD"):
            if(self.checkAPW() == False):
                valid = False
            
            if(self.checkAAmp() == False):
                valid = False
            
            if(self.checkASens() == False): 
                valid = False
            
            if(self.checkARP() == False): 
                valid =  False
            
            if(self.checkPVARP() == False): 
                valid = False
                
            if(self.checkVPW() == False):
                valid = False
            
            if(self.checkVAmp() == False): 
                valid = False

            if(self.checkVSens() == False): 
                valid = False 
            
            if(self.checkVRP() == False): 
                valid = False
            
            if(self.checkFixedAVdelay() == False):
                valid = False

        elif(pMode=="DDDR"):
            if(self.checkAPW() == False):
                valid = False
            
            if(self.checkAAmp() == False):
                valid = False
            
            if(self.checkASens() == False): 
                valid = False
            
            if(self.checkARP() == False): 
                valid =  False
            
            if(self.checkPVARP() == False): 
                valid = False

            if(self.checkVPW() == False):
                valid = False
            
            if(self.checkVAmp() == False): 
                valid = False

            if(self.checkVSens() == False): 
                valid = False 
            
            if(self.checkVRP() == False): 
                valid = False
            
            if(self.checkActThr() == False):
                valid = False

            if(self.checkReactTime() == False):
                valid = False

            if(self.checkRespFactor() == False):
                valid =  False

            if(self.checkRecoveryTime() == False):
                valid = False

            if(self.checkMaxSensRate() == False):
                valid = False
                
            if(self.checkFixedAVdelay() == False):
                valid = False
                
        if(valid == False): 
            self.displayErrors()
            self.errors.clear() #To prevent multiple of the same errors from previous attempts to input new variable values
        else: 
            messagebox.showinfo(title = "Changes Saved", message = "All inputs valid. Values saved to database.")
        return valid
        
    # retrieve database information for a given patient and save to patient
    def copyFromDB(self): 
        connection = sqlite3.connect('userdata.db')
        cursor = connection.cursor()


        cursor.execute("SELECT lrl FROM accounts WHERE username = (:username)", {
            'username': self.username
        })
        self.lrl = cursor.fetchone()[0]
        cursor.execute("SELECT url FROM accounts WHERE username = (:username)", {
            'username': self.username
        })
        self.url = cursor.fetchone()[0]
        cursor.execute("SELECT pacingMode FROM accounts WHERE username = (:username)", {
            'username': self.username
        })
        self.pacingMode=cursor.fetchone()[0]
        cursor.execute("SELECT apw FROM accounts WHERE username = (:username)", {
            'username': self.username
        })
        self.apw = cursor.fetchone()[0]
        cursor.execute("SELECT vpw FROM accounts WHERE username = (:username)", {
            'username': self.username
        })
        self.vpw = cursor.fetchone()[0]
        cursor.execute("SELECT aamp FROM accounts WHERE username = (:username)", {
            'username': self.username
        })
        self.aamp = cursor.fetchone()[0]
        cursor.execute("SELECT vamp FROM accounts WHERE username = (:username)", {
            'username': self.username
        })
        self.vamp = cursor.fetchone()[0]
        cursor.execute("SELECT asens FROM accounts WHERE username = (:username)", {
            'username': self.username
        })
        self.asens = cursor.fetchone()[0]
        cursor.execute("SELECT vsens FROM accounts WHERE username = (:username)", {
            'username': self.username
        })
        self.vsens = cursor.fetchone()[0]
        cursor.execute("SELECT arp FROM accounts WHERE username = (:username)", {
            'username': self.username
        })
        self.arp = cursor.fetchone()[0]
        cursor.execute("SELECT vrp FROM accounts WHERE username = (:username)", {
            'username': self.username
        })
        self.vrp = cursor.fetchone()[0]
        cursor.execute("SELECT pvarp FROM accounts WHERE username = (:username)", {
            'username': self.username
        })
        self.pvarp = cursor.fetchone()[0]
        cursor.execute("SELECT actThr FROM accounts WHERE username = (:username)", {
            'username': self.username
        })
        self.actThr = cursor.fetchone()[0]
        cursor.execute("SELECT reactTime FROM accounts WHERE username = (:username)", {
            'username': self.username
        })
        self.reactTime = cursor.fetchone()[0]
        cursor.execute("SELECT respFactor FROM accounts WHERE username = (:username)", {
            'username': self.username
        })
        self.respFactor = cursor.fetchone()[0]
        cursor.execute("SELECT recoveryTime FROM accounts WHERE username = (:username)", {
            'username': self.username
        })
        self.recoveryTime = cursor.fetchone()[0]
        cursor.execute("SELECT maxSensRate FROM accounts WHERE username = (:username)", {
            'username': self.username
        })
        self.maxSensRate = cursor.fetchone()[0]
        cursor.execute("SELECT fixedAVdelay FROM accounts WHERE username = (:username)", {
            'username': self.username
        })
        self.fixedAVdelay = cursor.fetchone()[0]
        
        connection.commit()

    # save current patient information/variables to the database
    def saveToDB(self):
        try:
            connection = sqlite3.connect('userdata.db')
            cursor = connection.cursor()
            cursor.execute('''UPDATE accounts 
                            SET pacingMode = (:pacingMode),
                                lrl = (:lrl),
                                url = (:url),
                                apw = (:apw),
                                vpw = (:vpw),
                                aamp = (:aamp),
                                vamp = (:vamp),
                                asens = (:asens),
                                vsens = (:vsens),
                                arp = (:arp),
                                vrp = (:vrp),
                                pvarp = (:pvarp),
                                actThr = (:actThr),
                                reactTime = (:reactTime),
                                respFactor = (:respFactor),
                                recoveryTime = (:recoveryTime),
                                maxSensRate = (:maxSensRate),
                                fixedAVdelay = (:fixedAVdelay)     
                            WHERE username = (:username)''', {
                                'pacingMode': self.pacingMode,
                                'lrl': self.lrl,
                                'url': self.url,
                                'apw': self.apw,
                                'vpw': self.vpw,
                                'aamp': round(self.aamp,1),
                                'vamp': round(self.vamp,1),
                                'asens': round(self.asens,1),
                                'vsens': round(self.vsens,1),
                                'arp': self.arp,
                                'vrp': self.vrp,
                                'pvarp': self.pvarp,
                                'actThr': self.actThr,
                                'reactTime': self.reactTime,
                                'respFactor': self.respFactor,
                                'recoveryTime': self.recoveryTime,
                                'maxSensRate': self.maxSensRate,
                                'fixedAVdelay': self.fixedAVdelay,
                                'username': self.username
                })
            connection.commit()
        except Exception as ep:
            print(ep)