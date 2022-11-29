import sqlite3
import Patient as P

# create database to store patient information
def createDB():
    connection = sqlite3.connect('userdata.db')
    cursor = connection.cursor()

    # create database table
    cursor.execute('''CREATE TABLE IF NOT EXISTS accounts (
                        username TEXT,
                        password TEXT,
                        pacingMode TEXT,
                        lrl INTEGER,
                        url INTEGER,
                        apw INTEGER,
                        vpw INTEGER,
                        aamp REAL,
                        vamp REAL,
                        asens REAL,
                        vsens REAL,
                        arp INTEGER,
                        vrp INTEGER,
                        pvarp INTEGER,
                        actThr TEXT,
                        reactTime INTEGER,
                        respFactor INTEGER,
                        recoveryTime INTEGER,
                        maxSensRate INTEGER,
                        fixedAVdelay INTEGER
                )
                ''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS pacemakers (
            serNum TEXT
        );
    ''')
    connection.commit()


def DeviceIsNew(serNum): 
    connection = sqlite3.connect('userdata.db')
    cursor = connection.cursor()


    cursor.execute("SELECT * FROM pacemakers WHERE serNum = (:serNum)", {
        'serNum': serNum
    })

    fet=cursor.fetchone()

    connection.commit()

    if fet!= None: # serial number is in the db
        return False
    else: # serial number is not in the db
        return True

    


def indexExists(index):
    connection = sqlite3.connect('userdata.db')
    cursor = connection.cursor()


    cursor.execute("SELECT * FROM accounts")
    maxIndex=len(cursor.fetchall())-1 # subtracting to start from 0
    print(maxIndex)

    if index>maxIndex:
        print("false")
        return False
    else:
        print("true")
        return True

