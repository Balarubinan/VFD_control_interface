from flask_restful import Resource, Api
from flask import Flask,request
# from Flask_server_files.DBoperations import *
# from Flask_server_files.exposed_values import *
import socket
from threading import Thread
app = Flask(__name__)
api = Api(app)

# use the ip of the pythonanywhere site instead of '127.0.0.1'

# @app.route('/124',methods=["GET","POST"])
# def rotary_socket_connection():
#     x=socket.socket()
#     print(socket.gethostname())
#     x.bind((socket.gethostname(),5002))
#     x.listen(1)
#     con,addr=x.accept()
#     print("This is working!")
#     while(True):
#         con.sendall(b'this is shitty value')

@app.route('/init_connection/<string:type>',methods=["GET","POST"])
def init_connection(type):
    if type=="rot":
        port_no=5001
        t=Thread(target=start_rotary_socket)
        t.start()
    elif type=="lin":
        port_no=5002
        t = Thread(target=start_rotary_socket)
        t.start()
    else:
        port_no=5003
        t = Thread(target=start_rotary_socket)
        t.start()
    return {"hostname":socket.gethostname(),"status":"connection available","port":port_no}

def start_rotary_socket():
    # print("Entered start function")
    app.logger.error("print inside the thread funnction")
    x=socket.socket()
    x.bind((socket.gethostname(),5001))
    app.logger.error("after finacsdvdv")
    x.listen()
    app.logger.error("after finisj")
    con,addr=x.accept()
    app.logger.error("after finisj befo loop")
    while(True):
        con.sendall(b'fucking worked')
        time.sleep(1)
        # print(str(data))






if __name__ == '__main__':
    app.run(debug=True)
    print("server started!!")
