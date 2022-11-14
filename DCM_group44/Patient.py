from tkinter import messagebox
import data
import sqlite3

lrl_range1 = [30,50]
lrl_range2 = [50,90]
lrl_range3 = [90,175]
url_range = [50,175]
apw_low = 0.05
apw_range = [0.1,1.9]
vpw_low = 0.05
vpw_range = [0.1,1.9]
aamp_range1 = [0.5,3.2]
aamp_range2 = [3.2,7]
vamp_range1 = [0.5,3.2]
vamp_range2 = [3.2,7]
asens_range1 = [0.25, 0.75]
asens_range2 = [0.75,10]
vsens_range1 = [0.25,0.75]
vsens_range2 = [0.75,10]
arp_range = [150,500]
vrp_range = [15,500]
pvarp_range = [150,500]
actThr_range = ["V-Low", "Low", "Med-Low", "Med", "Med-High","High","V-High"]
reactTime_range = [10,50]
respFactor_range = [1,16]
recoveryTime_range = [2,16]
maxSensRate_range = [50,175]
fixedAVdelay_range = [70,300]

lrl_r1_inc = 5
lrl_r2_inc = 1
lrl_r3_inc = 5
url_inc = 5
apw_inc = 0.1
vpw_inc = 0.1
aamp_r1_inc = 0.1
aamp_r2_inc = 0.5
vamp_r1_inc = 0.1
vamp_r2_inc = 0.5
asens_r1_inc = 0.25
asens_r2_inc = 0.5  
vsens_r1_inc = 0.25
vsens_r2_inc = 0.5
arp_inc = 10
vrp_inc = 10
pvarp_inc = 10
reactTime_inc = 10
respFactor_inc = 1
recoveryTime_inc = 1
maxSensRate_inc = 5
fixedAVdelay_inc = 10

errorTolerance = 0.00000001 #This is a value to account for the inaccuracy of computer calculations (specifically modulo of floats)

def isBetween(N, smallNum, bigNum):
    if(float(N)<float(smallNum) or float(N)>float(bigNum)):
        return False
    else:
        return True

class Patient:
    def __init__(self):
        self.username="NONE"

        self.lrl = 60
        self.url = 120
        self.pacingMode = "NONE"
        self.apw = 0.4
        self.vpw = 0.4
        self.aamp = 3.5
        self.vamp = 3.5
        self.asens = 0.75
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

    def checkLRL(self):
        #Checking Lower Rate Limit
        try: 
            self.lrl = int(self.lrl)
            if(isBetween(self.lrl,lrl_range1[0],lrl_range1[1])):
                if(not self.lrl % lrl_r1_inc == 0): 
                    messagebox.showerror(title="Error", message="Invalid increment for LRL. Increment should be "+str(lrl_r1_inc))
                    return False
            elif(isBetween(self.lrl, lrl_range2[0], lrl_range2[1])):
                pass #If self.lrl is an integer in this range, it is valid because the increments are by 1
            elif(isBetween(self.lrl, lrl_range3[0], lrl_range3[1])):
                if(not self.lrl % lrl_r3_inc == 0): 
                    messagebox.showerror(title="Error", message="Invalid increment for LRL. Increment should be "+str(lrl_r3_inc))
                    return False
            else: 
                messagebox.showerror(title="Error", message=" LRL Out of range. Acceptable range is ["+str(lrl_range1[0])+", "+str(lrl_range3[1])+"]")
                return False
        except: 
                messagebox.showerror(title="Error", message="LRL must be an integer.")
                return False

    def checkURL(self): 
        #Checking Upper Rate Limit
        try: 
            self.url = int(self.url)
            if(isBetween(self.url,url_range[0],url_range[1])):
                if(not self.url % url_inc == 0): 
                    messagebox.showerror(title="Error", message="Invalid increment for URL. Increment should be "+str(url_inc))
                    return False
                if(self.url < self.lrl): 
                    messagebox.showerror(title = "Error", message = "The Upper Rate Limit cannot be less the Lower Rate Limit. Please input a valid value")
                    return False
                elif(self.url == self.lrl): 
                    messagebox.showerror(title = "Error", message = "The Upper Rate Limit cannot be equal to the Lower Rate Limit. Please input a valid value")
                    return False
            else: 
                messagebox.showerror(title="Error", message=" URL Out of range. Acceptable range is ["+str(url_range[0])+", "+str(url_range[1])+"]")
                return False
        except: 
            messagebox.showerror(title="Error", message="URL must be an integer.")
            return False
        return True
    
    def checkAPW(self): 
        #Checking Atrial Pulse Width
        try: 
            self.apw = float(self.apw)
            if(self.apw == apw_low): 
                pass #This is a good thing so it shouldn't do anything
            elif(isBetween(self.apw,apw_range[0],apw_range[1])):
                if(self.apw % apw_inc != 0 and (apw_inc - (self.apw % apw_inc) > errorTolerance)): 
                    print(apw_inc - (self.apw % apw_inc))
                    messagebox.showerror(title="Error", message="Invalid increment for APW. Increment should be "+str(apw_inc))
                    return False
            else: 
                messagebox.showerror(title="Error", message=" APW Out of range. Acceptable range is ["+str(apw_range[0])+", "+str(apw_range[1])+"]")
                return False
        except: 
            messagebox.showerror(title="Error", message="APW must be a float.")
            return False

    def checkAAmp(self): 
        #Checking Atrial Amplitude
        try: 
            self.aamp = float(self.aamp)
            if(isBetween(self.aamp,aamp_range1[0],aamp_range1[1])): 
                if(self.aamp % aamp_r1_inc != 0 and (aamp_r1_inc - (self.aamp % aamp_r1_inc) > errorTolerance)):
                    messagebox.showerror(title="Error", message="Invalid increment for AAmp. Increment should be "+str(aamp_r1_inc))
                    return False 
            elif(isBetween(self.aamp,aamp_range2[0],aamp_range2[1])):
                if(self.aamp % aamp_r2_inc != 0 and (aamp_r2_inc - (self.aamp % aamp_r2_inc) > errorTolerance)): 
                    messagebox.showerror(title="Error", message="Invalid increment for AAmp. Increment should be "+str(aamp_r2_inc))
                    return False
            else: 
                messagebox.showerror(title="Error", message=" AAmp Out of range. Acceptable range is ["+str(aamp_range1[0])+", "+str(aamp_range2[1])+"]")
                return False
        except: 
            messagebox.showerror(title="Error", message="AAmp must be a float.")
            return False
    
    def checkVPW(self): 
        #Checking Ventricular Pulse Width
        try: 
            self.vpw = float(self.vpw)
            if(self.vpw == vpw_low): 
                pass #This is a good thing so it shouldn't do anything
            elif(isBetween(self.vpw,vpw_range[0],vpw_range[1])):
                if(self.vpw % vpw_inc != 0 and (vpw_inc - (self.vpw % vpw_inc) > errorTolerance)): 
                    print(vpw_inc - (self.vpw % vpw_inc))
                    messagebox.showerror(title="Error", message="Invalid increment for VPW. Increment should be "+str(vpw_inc))
                    return False
            else: 
                messagebox.showerror(title="Error", message="VPW Out of range. Acceptable range is ["+str(vpw_range[0])+", "+str(vpw_range[1])+"]")
                return False
        except: 
            messagebox.showerror(title="Error", message="VPW must be a float.")
            return False
        
    def checkVAmp(self): 
        #Checking Ventricular Amplitude
        try: 
            self.vamp = float(self.vamp)
            if(isBetween(self.vamp,vamp_range1[0],vamp_range1[1])): 
                if(self.vamp % vamp_r1_inc != 0 and (vamp_r1_inc - (self.vamp % vamp_r1_inc) > errorTolerance)):
                    messagebox.showerror(title="Error", message="Invalid increment for VAmp. Increment should be "+str(vamp_r1_inc))
                    return False 
            elif(isBetween(self.vamp,vamp_range2[0],vamp_range2[1])):
                if(self.vamp % vamp_r2_inc != 0 and (vamp_r2_inc - (self.vamp % vamp_r2_inc) > errorTolerance)): 
                    messagebox.showerror(title="Error", message="Invalid increment for VAmp. Increment should be "+str(vamp_r2_inc))
                    return False
            else: 
                messagebox.showerror(title="Error", message="VAmp Out of range. Acceptable range is ["+str(vamp_range1[0])+", "+str(vamp_range2[1])+"]")
                return False
        except: 
            messagebox.showerror(title="Error", message="VAmp must be a float.")
            return False

    def checkASens(self): 
        #Checking Atrial Sensitivity
        try: 
            self.asens = float(self.asens)
            if(isBetween(self.asens,asens_range1[0],asens_range1[1])): 
                if(self.asens % asens_r1_inc != 0 and (asens_r1_inc - (self.asens % asens_r1_inc) > errorTolerance)):
                    messagebox.showerror(title="Error", message="Invalid increment for Asens. Increment should be "+str(asens_r1_inc))
                    return False 
            elif(isBetween(self.asens,asens_range2[0],asens_range2[1])):
                if(self.asens % asens_r2_inc != 0 and (asens_r2_inc - (self.asens % asens_r2_inc) > errorTolerance)): 
                    messagebox.showerror(title="Error", message="Invalid increment for Asens. Increment should be "+str(asens_r2_inc))
                    return False
            else: 
                messagebox.showerror(title="Error", message="Asens Out of range. Acceptable range is ["+str(asens_range1[0])+", "+str(asens_range2[1])+"]")
                return False
        except: 
            messagebox.showerror(title="Error", message="Asens must be a float.")
            return False

    def checkARP(self): 
        #Checking Atrial Refractory Period
        try: 
            self.arp = int(self.arp)
            if(isBetween(self.arp,arp_range[0],arp_range[1])):
                if(not self.arp % arp_inc == 0): 
                    messagebox.showerror(title="Error", message="Invalid increment for ARP. Increment should be "+str(arp_inc))
                    return False
                lrlTime = (1/self.lrl)*1000 #The time between pulses in ms
                if(self.arp > lrlTime): 
                    messagebox.showerror(title = "Error", message = "Invalid input for Atrial Refractory Period. Time cannot be greater than the time between pulses at Lower Rate Limit. In this case that is " + str(round(lrlTime, 2)) + "ms so please input a value smaller than this.")                
                    return False
            else: 
                messagebox.showerror(title="Error", message="ARP Out of range. Acceptable range is ["+str(arp_range[0])+", "+str(arp_range[1])+"]")
                return False
        except: 
            messagebox.showerror(title="Error", message="ARP must be an integer.")
            return False
        return True

    def checkPVARP(self): 
        #Checking PVARP
        try: 
            self.pvarp = int(self.pvarp)
            if(isBetween(self.pvarp,pvarp_range[0],pvarp_range[1])):
                if(not self.pvarp % pvarp_inc == 0): 
                    messagebox.showerror(title="Error", message="Invalid increment for PVARP. Increment should be "+str(pvarp_inc))
                    return False
            else: 
                messagebox.showerror(title="Error", message="PVARP Out of range. Acceptable range is ["+str(pvarp_range[0])+", "+str(pvarp_range[1])+"]")
                return False
        except: 
            messagebox.showerror(title="Error", message="PVARP must be an integer.")
            return False
        return True       

    
    
        
    def checkVSens(self): 
        #Checking Ventricular Sensitivity
        try: 
            self.vsens = float(self.vsens)
            if(isBetween(self.vsens,vsens_range1[0],vsens_range1[1])): 
                if(self.vsens % vsens_r1_inc != 0 and (vsens_r1_inc - (self.vsens % vsens_r1_inc) > errorTolerance)):
                    messagebox.showerror(title="Error", message="Invalid increment for Vsens. Increment should be "+str(vsens_r1_inc))
                    return False 
            elif(isBetween(self.vsens,vsens_range2[0],vsens_range2[1])):
                if(self.vsens % vsens_r2_inc != 0 and (vsens_r2_inc - (self.vsens % vsens_r2_inc) > errorTolerance)): 
                    messagebox.showerror(title="Error", message="Invalid increment for Vsens. Increment should be "+str(vsens_r2_inc))
                    return False
            else: 
                messagebox.showerror(title="Error", message="Vsens Out of range. Acceptable range is ["+str(vsens_range1[0])+", "+str(vsens_range2[1])+"]")
                return False
        except: 
            messagebox.showerror(title="Error", message="Vsens must be a float.")
            return False

    def checkVRP(self): 
        #Checking VRP
        try: 
            self.vrp = int(self.vrp)
            if(isBetween(self.vrp,vrp_range[0],vrp_range[1])):
                if(not self.vrp % vrp_inc == 0): 
                    messagebox.showerror(title="Error", message="Invalid increment for VRP. Increment should be "+str(vrp_inc))
                    return False
            else: 
                messagebox.showerror(title="Error", message="VRP Out of range. Acceptable range is ["+str(vrp_range[0])+", "+str(vrp_range[1])+"]")
                return False
        except: 
            messagebox.showerror(title="Error", message="VRP must be an integer.")
            return False
        return True

    def checkActThr(self):
        found=False
        for item in actThr_range:
            if self.actThr==item:
                found=True

        if found==False:
            messagebox.showerror(title="Error", message="Activity Threshold invalid.")
            return False
        else:
            return True


    def checkReactTime(self):
        try: 
            self.reactTime = int(self.reactTime)
            if(isBetween(self.reactTime,reactTime_range[0],reactTime_range[1])):
                if(not self.reactTime % reactTime_inc == 0): 
                    messagebox.showerror(title="Error", message="Invalid increment for Reaction Time. Increment should be "+str(reactTime_inc))
                    return False
            else: 
                messagebox.showerror(title="Error", message="Reaction Time Out of range. Acceptable range is ["+str(reactTime_range[0])+", "+str(reactTime_range[1])+"]")
                return False
        except: 
            messagebox.showerror(title="Error", message="Reaction Time must be an integer.")
            return False
        return True

    def checkRespFactor(self):
        try: 
            self.respFactor = int(self.respFactor)
            if(isBetween(self.respFactor,respFactor_range[0],respFactor_range[1])):
                if(not self.respFactor % respFactor_inc == 0): 
                    messagebox.showerror(title="Error", message="Invalid increment for Response Factor. Increment should be "+str(respFactor_inc))
                    return False
            else: 
                messagebox.showerror(title="Error", message="Response Factor Out of range. Acceptable range is ["+str(respFactor_range[0])+", "+str(respFactor_range[1])+"]")
                return False
        except: 
            messagebox.showerror(title="Error", message="Response Factor must be an integer.")
            return False
        return True

    def checkRecoveryTime(self):
        try: 
            self.recoveryTime = int(self.recoveryTime)
            if(isBetween(self.recoveryTime,recoveryTime_range[0],recoveryTime_range[1])):
                if(not self.recoveryTime % recoveryTime_inc == 0): 
                    messagebox.showerror(title="Error", message="Invalid increment for Recovery Time. Increment should be "+str(recoveryTime_inc))
                    return False
            else: 
                messagebox.showerror(title="Error", message="Recovery Time Out of range. Acceptable range is ["+str(recoveryTime_range[0])+", "+str(recoveryTime_range[1])+"]")
                return False
        except: 
            messagebox.showerror(title="Error", message="Recovery Time must be an integer.")
            return False
        return True

    def checkMaxSensRate(self):
        try: 
            self.maxSensRate = int(self.maxSensRate)
            if(isBetween(self.maxSensRate,maxSensRate_range[0],maxSensRate_range[1])):
                if(not self.maxSensRate % maxSensRate_inc == 0): 
                    messagebox.showerror(title="Error", message="Invalid increment for Maximum Sensor Rate. Increment should be "+str(maxSensRate_inc))
                    return False
            else: 
                messagebox.showerror(title="Error", message="Maximum Sensor Rate Out of range. Acceptable range is ["+str(maxSensRate_range[0])+", "+str(maxSensRate_range[1])+"]")
                return False
        except: 
            messagebox.showerror(title="Error", message="Maximum Sensor Rate must be an integer.")
            return False
        return True

    def checkFixedAVdelay(self):
        try: 
            self.fixedAVdelay = int(self.fixedAVdelay)
            if(isBetween(self.fixedAVdelay,fixedAVdelay_range[0],fixedAVdelay_range[1])):
                if(not self.fixedAVdelay % fixedAVdelay_inc == 0): 
                    messagebox.showerror(title="Error", message="Invalid increment for Fixed AV Delay. Increment should be "+str(fixedAVdelay_inc))
                    return False
            else: 
                messagebox.showerror(title="Error", message="Fixed AV Delay Out of range. Acceptable range is ["+str(fixedAVdelay_range[0])+", "+str(fixedAVdelay_range[1])+"]")
                return False
        except: 
            messagebox.showerror(title="Error", message="Fixed AV Delay must be an integer.")
            return False
        return True
    

    def numsValid(self,pMode):
        if(self.checkLRL() == False):
            return False
             
        if(self.checkURL() == False):
            return False
        
        
        #Checking validity of input parameters for AOO
        if(pMode=="AOO"):

            if(self.checkAPW() == False):
                return False
            
            if(self.checkAAmp() == False):
                return False
            
            
        #Checking validity of input parameteres for VOO
        elif(pMode=="VOO"):
            
            if(self.checkVPW() == False): 
                return False

            if(self.checkVAmp() == False):
                return False

        #Checking validity of input parameters for AAI
        elif(pMode=="AAI"):
            
            if(self.checkAPW() == False):
                return False
            
            if(self.checkAAmp() == False):
                return False
            
            if(self.checkASens() == False): 
                return False
            
            if(self.checkARP() == False): 
                return False
            
            if(self.checkPVARP() == False): 
                return False
            
            

        #Checking validity of input parameters for VVI
        elif(pMode=="VVI"):
            
            if(self.checkVPW() == False):
                return False
            
            if(self.checkVAmp() == False): 
                return False

            if(self.checkVSens() == False): 
                return False 
            
            if(self.checkVRP() == False): 
                return False

        else: #if it's any rate adaptive mode
            if(self.checkActThr()==False):
                return False
            
            if(self.checkReactTime()==False):
                return False

            if(self.checkRespFactor()==False):
                return False

            if(self.checkRecoveryTime()==False):
                return False

            if(self.checkMaxSensRate()==False):
                return False

            if(self.checkFixedAVdelay()==False):
                return False

        print("Nums valid")
        return True

    def copyFromDB(self): #Takes a username string and returns a patient instance
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
                                'aamp': self.aamp,
                                'vamp': self.vamp,
                                'asens': self.asens,
                                'vsens': self.vsens,
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