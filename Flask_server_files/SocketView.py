import random

from socketio import Client
from .RPI_operations import *
import time

sio=Client()

# for some reason connect even is not called
@sio.on('connect')
def connect():
    print("server is connected")

# send random value @ random time slots of max 5 secs
@sio.on("ready")
def ready_method(data):
    sio.emit('typeUpdate',{"type":"view"})

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
    print("NNo senders => sensor client not ready")

# only call connect after the handlers are defined
sio.connect("https://argo-server-1.herokuapp.com/",{"secure":True})
# sio.connect("http://localhost:5000")

# wrap all the above methods in a class

