import datetime
from random import randint
from socketio import Client
import time
import os
from datetime import date
from tkinter import *
from tkinter import Tk
from tkinter import font
from requests import get,post
from BufferScript import *
from threading import Thread

devMode=True
baseUrl=None
if devMode:
    baseUrl="http://localhost:5000/restApi"
    print("In devmode!")
else:
    baseUrl="https://argo-server-1.herokuapp.com/restApi"
    print("In ProdMode!!")
sio=Client()

def wrapperFunc():

    while(1):
        time.sleep(1)
        simultateRotaryEncoder()

# for some reason connect even is not called
@sio.on('connect')
def connect():
    print("server is connected")

# send random value @ random time slots of max 5 secs
@sio.on("ready")
def ready_method(data):
    sio.emit('typeUpdate',{"type":"send",'devicename':"Tractor1"})
    # sio.emit('nameReg',{'devicename':"Tractor1"})
    while(1):
        os.system("cls\n")
        # start from here !!
        val={"value":randint(-12,12),"linValue":randint(-12,12)}
        print("Sending value",val)
        sio.emit('valueUpdate',val)
        time.sleep(2)

@sio.on('ping')
def ping_check(data):
    print("a viewer pinged me")

@sio.on("disconnect")
def disconnect():
    print("socket Disconnected")

@sio.on('success')
def typeUpdateSucccess(data):
    print("type update is done!!")

@sio.on('newValue')
def newValue(data):
    print("Data recieved is ",data)

@sio.on('nosenders')
def Nosend(data):
    print("NNo senders => sensor client not ready",data)

# only call connect after the handlers are defined
# not working
# works only with http:
from requests import get

# calling refresh metho before starting the comm
# get("https://argo-server-1.herokuapp.com/refresh")
# sio.connect("http://argo-server-1.herokuapp.com/")
# no refresh need as clients will request by name
# get("http://localhost:5000/
tractorOff=True
def startTractor():
    global tractorOff
    if tractorOff:
        b['text']="ON"
        b['bg']="green"
        print("Starting tractor")
        tractorStarted()
        sio.connect("http://localhost:5000")
        print("Tractor started")
        Thread(target=wrapperFunc).start()

    else:
        b['text']="OFF"
        b['bg']="red"
        print("Turning off Tractor")
        # Time in mins

        print(datetime.date.today())
        # actTime,movTime,clientId,date=23,12,"IIPC Test Client",datetime.date.today()
        # implement buffer script here
        tractorStoped()
        dataDict={
            "actTime":getActTime(),
            "movTime":getMovTime(),
            "clientId":getClientId(),
            "date":datetime.date.today()
        }
        print(dataDict)
        # post(baseUrl+"/saveRunData",data=dataDict)
        print("Tractor turned off")

    tractorOff=not(tractorOff)
        # DB calls here!


# finish UI and db calls
root=Tk()
root.geometry("500x300")
Label(root,text="Tractor status",font=font.Font(size=25)).pack()
f=Frame(root).pack()
Label(f,text="Tractor Status")
b=Button(f,text="OFF",command=startTractor,height=10, width=15)
b['bg']="red"
b.place(x=200,y=50)
root.mainloop()

# UI runs perfectly!!
# wrap all the above methods in a class
# design a buffer mode if the board goes offline
# send a disconnect signal to warn the server
