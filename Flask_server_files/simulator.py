from requests import get,post

# data=post("http://127.0.0.1:5000/rot/start")
# print(data.json())

def get_values():
    value=get("http://127.0.0.1:5000/rot/sdvsdv")
    print(value)
    value=value.json()['pulses']

    print(value)
    return(True,int(value))

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

