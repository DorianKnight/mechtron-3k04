import data
import sqlite3

lrl_range = [0,10]
url_range = [0,10]
apw_range = [0,10]
vpw_range = [0,10]
aamp_range = [0,10]
vamp_range = [0,10]
asens_range = [0,10]
vsens_range = [0,10]
arp_range = [0,10]
vrp_range = [0,10]
pvarp_range = [0,10]
hrl_range = [0,10]
rs_range = [0,10]

def isBetween(N, smallNum, bigNum):
    if(float(N)<float(smallNum) or float(N)>float(bigNum)):
        return False
    else:
        return True

class Patient:
    def __init__(self):
        self.username="NONE"

        self.lrl = 0
        self.url = 0
        self.pacingMode = "NONE"
        self.apw = 0.0
        self.vpw = 0.0
        self.aamp = 0.0
        self.vamp = 0.0
        self.asens = 0.0
        self.vsens = 0.0
        self.arp = 0
        self.vrp = 0
        self.pvarp = 0
        self.hrl = 0
        self.rs = 0

    def numsValid(self,pMode):
        if(not isBetween(self.lrl,lrl_range[0],lrl_range[1])):
            return False
        if(not isBetween(self.url,url_range[0],url_range[1])):
            return False
        
        if(pMode=="AOO"):
            if(not isBetween(self.apw,apw_range[0],apw_range[1])):
                return False
            if(not isBetween(self.aamp,aamp_range[0],aamp_range[1])):
                return False
            

        elif(pMode=="VOO"):
            if(not isBetween(self.vpw,vpw_range[0],vpw_range[1])):
                return False
            if(not isBetween(self.vamp,vamp_range[0],vamp_range[1])):
                return False

        elif(pMode=="AAI"):
            if(not isBetween(self.apw,apw_range[0],apw_range[1])):
                return False
            if(not isBetween(self.aamp,aamp_range[0],aamp_range[1])):
                return False
            if(not isBetween(self.asens,asens_range[0],asens_range[1])):
                return False
            if(not isBetween(self.arp,arp_range[0],arp_range[1])):
                return False
            if(not isBetween(self.pvarp,pvarp_range[0],pvarp_range[1])):
                return False
            if(self.hrl!=0 and self.hrl!=""):
                if(not isBetween(self.hrl,hrl_range[0],hrl_range[1])):
                    return False
            if(not isBetween(self.rs,rs_range[0],rs_range[1])):
                return False

        elif(pMode=="VVI"):
            if(not isBetween(self.vpw,vpw_range[0],vpw_range[1])):
                return False
            if(not isBetween(self.vamp,vamp_range[0],vamp_range[1])):
                return False
            if(not isBetween(self.vsens,vsens_range[0],vsens_range[1])):
                return False
            if(not isBetween(self.vrp,vrp_range[0],vrp_range[1])):
                return False
            if(self.hrl!=0 and self.hrl!=""):
                if(not isBetween(self.hrl,hrl_range[0],hrl_range[1])):
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
        cursor.execute("SELECT hrl FROM accounts WHERE username = (:username)", {
            'username': self.username
        })
        self.hrl = cursor.fetchone()[0]
        cursor.execute("SELECT rs FROM accounts WHERE username = (:username)", {
            'username': self.username
        })
        self.rs = cursor.fetchone()[0]

    def saveToDB(self):
        try:
            print("hi")
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
                                'hrl': self.hrl,
                                'rs': self.rs,
                                'username': self.username
                })
            connection.commit()
        except Exception as ep:
            print(ep)