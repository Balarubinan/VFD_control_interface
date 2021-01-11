import sqlite3
from datetime import datetime
import time
# connecting to db
try:
    con=sqlite3.connect("database_readings.db")
    cur=con.cursor()
    print("Database Connect success!!")
except:
    print("Database Connection error dude!!")

def write_to_linear(reading):
    try:
        nw=datetime.now()
        cur.execute("insert into linear_readings values(?,?,?,?,?)"
                    ,(nw.date(),nw.hour,nw.minute,nw.second,reading))
        con.commit()
    except:
        print("Value linear write error!")


def write_to_rotary(reading):
    try:
        nw = datetime.now()
        cur.execute("insert into rotary_readings values(?,?,?,?,?)"
                    , (nw.date(), nw.hour, nw.minute, nw.second, reading))
        con.commit()
    except:
        print("Value rotary write error!")


def write_to_vfd(current,voltage,freq):
    pass


# returns last standby value
def fetch_from_linear():
    try:
        cur.execute("select value from last_linear_reading")
        a=cur.fetchall()
        print("fetched value is",a[0][0])
        return int(a[0][0])
    except:
        print("Value linear fetch error!")


def fetch_from_rotary(reading):
    pass

def fetch_from_vdf(reading):
    pass