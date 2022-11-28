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
    connection.commit()

''' idk why i wrote this tbh
def getUserIndex(username): # returns an index (0-9) associated with a user in the database
    connection = sqlite3.connect('userdata.db')
    cursor = connection.cursor()


    cursor.execute("SELECT ROWID,* FROM accounts WHERE username = (:username)", {
        'username': username
    })

    if cursor.fetchone()!= None: # user is in the db
        index = cursor.fetchone()[0]-1 # to start from index 0
    else: # user is not in the db
        index=  -1 # return -1 if user was not found in the database

    print(index)

    return index
'''

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

