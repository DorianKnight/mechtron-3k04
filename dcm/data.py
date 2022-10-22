import sqlite3

def createDB():
    connection = sqlite3.connect('userdata.db')
    cursor = connection.cursor()

    # create database table
    cursor.execute('''CREATE TABLE IF NOT EXISTS accounts (
                        username text,
                        password text,
                        lrl INTEGER,
                        url INTEGER,
                        apw REAL,
                        vpw REAL,
                        aamp REAL,
                        vamp REAL,
                        asens REAL,
                        vsens REAL,
                        arp INTEGER,
                        vrp INTEGER,
                        pvarp INTEGER,
                        hyst boolean,
                        hrl INTEGER,
                        rs INTEGER
                )
                ''')
    connection.commit()