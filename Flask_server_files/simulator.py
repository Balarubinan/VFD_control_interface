from random import choice

from requests import get,post

import numpy as np

# data=post("http://127.0.0.1:5000/rot/start")
# print(data.json())

def get_values():
    value=get("http://127.0.0.1:5000/rot")
    print(value)
    value=value.json()['pulses']

    print(value)
    return(True,int(value))

def fake_get_values():
    return True,((choice([-1, 1])) * np.random.random())



# # get_values()
# from socketio import Client
# sio=Client()
#
#
# sio.connect("http://127.0.0.1:5000",namespaces=['/test'])
# print("After connect")
# print(sio.namespaces)
# # print("my sio id ",sio.sid)
# sio.emit('my message',{"fuck ":"this"})
# print("After emit")
#
# @sio.on('77',namespace='/test')
# def ddd(data):
#     print("server reponded yaay",data)

