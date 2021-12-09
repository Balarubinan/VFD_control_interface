import random

from socketio import Client
import time
from Flask_server_files.RPI_operations import measure_voltage

sio=Client()

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
        val={"value":measure_voltage()/51}
        print("Sending value",val)
        sio.emit('valueUpdate',val)
        time.sleep(.5)

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
sio.connect("http://argo-server-1.herokuapp.com/")
# no refresh need as clients will request by name
# get("http://localhost:5000/refresh")
# sio.connect("http://localhost:5000")

# wrap all the above methods in a class
# design a buffer mode if the board goes offline
# send a disconnect signal to warn the server
