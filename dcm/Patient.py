import data
import sqlite3

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