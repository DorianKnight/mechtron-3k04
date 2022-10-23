import data
import sqlite3

lrl_range1 = [30,50]
lrl_range2 = [51,90]
lrl_range3 = [95,175]
url_range = [50,175]
apw_low = 0.05
apw_range = [0.1,1.9]
vpw_low = 0.05
vpw_range = [0.1,1.9]
aamp_range1 = [0.5,3.2]
aamp_range2 = [3.5,7]
vamp_range1 = [0.5,3.2]
vamp_range2 = [3.5,7]
asens_range1 = [0.25, 0.75]
asens_range2 = [1,10]
vsens_range1 = [0.25,0.75]
vsens_range2 = [1,10]
arp_range = [150,500]
vrp_range = [15,500]
pvarp_range = [150,500]
hrl_low = 0
hrl_range1 = lrl_range1
hrl_range2 = lrl_range2
hrl_range3 = lrl_range3
rs_range = [0,21]
rs_multiplier = 0.25 #The highest value of rate smoothing is 25% 

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
hrl_r1_inc = lrl_r1_inc
hrl_r2_inc = lrl_r2_inc
hrl_r3_inc = lrl_r3_inc
rs_inc = 3
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
        self.hystBool = 0 # use 0 for false and 1 for true because SQLite doesn't support boolean
        self.hrl = 0
        self.rs = 0

    def checkLRL(self):
        #Checking Lower Rate Limit
        try: 
            self.lrl = int(self.lrl)
            if(isBetween(self.lrl,lrl_range1[0],lrl_range1[1])):
                if(not self.lrl % lrl_r1_inc == 0): 
                    print("false 1")
                    return False
            elif(isBetween(self.lrl, lrl_range2[0], lrl_range2[1])):
                pass #If self.lrl is an integer in this range, it is valid because the increments are by 1
            elif(isBetween(self.lrl, lrl_range3[0], lrl_range3[1])):
                if(not self.lrl % lrl_r3_inc == 0): 
                    print("false 3")
                    return False
            else: 
                print("FALSE")
                return False
        except: 
                print("LRL Conversion to integer error")
                return False

    def checkURL(self): 
        #Checking Upper Rate Limit
        try: 
            self.url = int(self.url)
            if(isBetween(self.url,url_range[0],url_range[1])):
                if(not self.url % url_inc == 0): 
                    print("false 1")
                    return False
            else: 
                print("FALSE")
                return False
        except: 
            print("URL Conversion to integer error")
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
                    print("false 1")
                    return False
            else: 
                print("FALSE")
                return False
        except: 
            print("APW Conversion to float error")
            return False

    def checkAAmp(self): 
        #Checking Atrial Amplitude
        try: 
            self.aamp = float(self.aamp)
            if(isBetween(self.aamp,aamp_range1[0],aamp_range1[1])): 
                if(self.aamp % aamp_r1_inc != 0 and (aamp_r1_inc - (self.aamp % aamp_r1_inc) > errorTolerance)):
                    print("false 1")
                    return False 
            elif(isBetween(self.aamp,aamp_range2[0],aamp_range2[1])):
                if(self.aamp % aamp_r2_inc != 0 and (aamp_r2_inc - (self.aamp % aamp_r2_inc) > errorTolerance)): 
                    print("false 1")
                    return False
            else: 
                print("FALSE")
                return False
        except: 
            print("AAMP Conversion to float error")
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
                    print("false 1")
                    return False
            else: 
                print("FALSE")
                return False
        except: 
            print("APW Conversion to float error")
            return False
        
    def checkVAmp(self): 
        #Checking Ventricular Amplitude
        try: 
            self.vamp = float(self.vamp)
            if(isBetween(self.vamp,vamp_range1[0],vamp_range1[1])): 
                if(self.vamp % vamp_r1_inc != 0 and (vamp_r1_inc - (self.vamp % vamp_r1_inc) > errorTolerance)):
                    print("false 1")
                    return False 
            elif(isBetween(self.vamp,vamp_range2[0],vamp_range2[1])):
                if(self.vamp % vamp_r2_inc != 0 and (vamp_r2_inc - (self.vamp % vamp_r2_inc) > errorTolerance)): 
                    print("false 1")
                    return False
            else: 
                print("FALSE")
                return False
        except: 
            print("AAMP Conversion to float error")
            return False

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
            #Checking Atrial Pulse Width
            try: 
                self.apw = float(self.apw)
                if(self.apw == apw_low): 
                    pass #This is a good thing so it shouldn't do anything
                elif(isBetween(self.apw,apw_range[0],apw_range[1])):
                    if(self.apw % apw_inc != 0 and (apw_inc - (self.apw % apw_inc) > errorTolerance)): 
                        print(apw_inc - (self.apw % apw_inc))
                        print("false 1")
                        return False
                else: 
                    print("FALSE")
                    return False
            except: 
                print("APW Conversion to float error")
                return False
            
            #Checking Atrial Amplitude
            try: 
                self.aamp = float(self.aamp)
                if(isBetween(self.aamp,aamp_range1[0],aamp_range1[1])): 
                    if(self.aamp % aamp_r1_inc != 0 and (aamp_r1_inc - (self.aamp % aamp_r1_inc) > errorTolerance)):
                        print("false 1")
                        return False 
                elif(isBetween(self.aamp,aamp_range2[0],aamp_range2[1])):
                    if(self.aamp % aamp_r2_inc != 0 and (aamp_r2_inc - (self.aamp % aamp_r2_inc) > errorTolerance)): 
                        print("false 1")
                        return False
                else: 
                    print("FALSE")
                    return False
            except: 
                print("AAMP Conversion to float error")
                return False
            
            if(not isBetween(self.asens,asens_range1[0],asens_range1[1])):
                return False
            if(not isBetween(self.arp,arp_range[0],arp_range[1])):
                return False
            if(not isBetween(self.pvarp,pvarp_range[0],pvarp_range[1])):
                return False
            if(self.hrl!=0 and self.hrl!=""):
                if(not isBetween(self.hrl,hrl_range1[0],hrl_range1[1])):
                    return False
            if(not isBetween(self.rs,rs_range[0],rs_range[1])):
                return False

        #Checking validity of input parameters for VVI
        elif(pMode=="VVI"):
            if(not isBetween(self.vpw,vpw_range[0],vpw_range[1])):
                return False
            if(not isBetween(self.vamp,vamp_range1[0],vamp_range1[1])):
                return False
            if(not isBetween(self.vsens,vsens_range1[0],vsens_range1[1])):
                return False
            if(not isBetween(self.vrp,vrp_range[0],vrp_range[1])):
                return False
            if(self.hrl!=0 and self.hrl!=""):
                if(not isBetween(self.hrl,hrl_range1[0],hrl_range1[1])):
                    return False
            if(not isBetween(self.rs,rs_range[0],rs_range[1])):
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
        cursor.execute("SELECT hystBool FROM accounts WHERE username = (:username)", {
            'username': self.username
        })
        self.hystBool = cursor.fetchone()[0]
        cursor.execute("SELECT hrl FROM accounts WHERE username = (:username)", {
            'username': self.username
        })
        self.hrl = cursor.fetchone()[0]
        cursor.execute("SELECT rs FROM accounts WHERE username = (:username)", {
            'username': self.username
        })
        self.rs = cursor.fetchone()[0]
        
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
                                hystBool = (:hystBool),
                                hrl = (:hrl),
                                rs = (:rs) 
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
                                'hystBool': self.hystBool,
                                'hrl': self.hrl,
                                'rs': self.rs,
                                'username': self.username
                })
            connection.commit()
        except Exception as ep:
            print(ep)