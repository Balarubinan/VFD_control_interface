
# # A very simple Flask Hello World app for you to get started with...

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello from Flask!'

from flask_restful import Resource, Api
from flask import Flask,request
from Flask_server_files.DBoperations import *
from Flask_server_files.exposed_values import *
# from Flask_server_files.handler_thread import standby_tracker
from threading import Thread
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)
CORS(app)

def get_cur_read():
    return current_val

def get_cur_rot():
    return pulse_read

class TodoSimple(Resource):
    def get(self, todo_id):
        global current_val
        return {"value":current_val,"a array":a}

    def post(self, todo_id):
        # 'data' is like a name variable
        # hence in request it must be present as
        # {'data':'<actual data>'}
        # todos[todo_id] = request.form['data']
        global a,current_val
        current_val=request.form['reading']
        print("Captured reading is ",current_val)
        a.append(current_val)
        print("data saved!!!")
        # return {todo_id: todos[todo_id]}
        return {"status":a}

class Linear(Resource):
    # def __init__(self):
    #
    #     super(Linear, self).__init__()

    def get(self,reading):
        global last_val,captured_values,stand_by_value,captured_values
        return {"reading":last_val,"captured":captured_values}

    def post(self,reading):
        global last_val, captured_values, stand_by_value, captured_values,cnt
        # reading -> if a number use as value  if "reset" clear all values in self.captured values

        # current_val = request.form['reading']
        current_val = reading
        print("current value")

        if current_val=="reset":
            print("reset in linear triggered!")
            captured_values=[]
            stand_by_value=fetch_from_linear()
            last_val=stand_by_value

        current_val=float(current_val)
        print("linear reading is ",current_val)

        if(last_val==current_val):
            cnt+=1
        #
        # if self.cnt==30:
        #     print("last standy value updated to",self.last_val)
        # write_to_linear(self.last_val)


        last_val=current_val
        captured_values.append(last_val)
        if len(captured_values)>100:
            captured_values.pop(0)

        # call update graph value herec
        # debug purpose
        return {"captured":captured_values}


# @app.route('/lin_stand')
# def linear_standby():
#     pass

class VFD_control(Resource):
    # def __init__(self):
    #
    #     super(VFD_control, self).__init__()


    def get(self):
        global current,freq,voltage
        return {"cur":current,"freq":freq,"vol":voltage}

    def post(self,mode,value):
        global current, freq, voltage
        # mode=request.form['mode']
        if mode=="control":
            self.control_module()
            return {"vfd feed":f"control updated {mode}"}

        # value = request.form['value']
        value=float(value)
        if mode=="freq":
            freq=value
        if mode=="current":
            current=value
        if mode=="voltage":
            voltage=value

        write_to_vfd(current,voltage,freq)
        # update graph here
        print("Values written")
        return {"vfd stat":f"{mode}:{value}"}

    def control_module(self):
        pass
        #write code for control value passing

class Rotary(Resource):

    def get(self,time):
        global pulse_values,pulse_read
        print(pulse_values[-1])
        return {"pulses":pulse_values[-1]}

    # def post(self,type):
    #     global pulse_read,pulse_values,standing_by
    #     # val=request.form['pulses']
    #     if type=="start":
    #         t=Thread(target=standby_tracker,args=[app])
    #         t.start()
    #         return {'status':'timer started'}
    #     else:
    #         pulse_read=True
    #         if standing_by:
    #             standing_by=False
    #         # time.sleep(0.95)
    #         return {'status':'updated'}
    def post(self,time):
        # the post request is to be given in the format of time encoded as a string
        # such a post request indicates that there has been a pulse at that instant of time
        # simple add the a 1 to the graph at that time....converting it to seconds from the start time
        # time format -> <seconds from the start>
        global pulse_values
        pulse_values.append(time)
        if len(pulse_values)>100:
            # write_to_rotary(pulse_values)
            pulse_values=[]











# Resource to serve client with data from database
class DataServer(Resource):
    def get(self):
        pass

    def post(self):
        pass

# this function also works without problems!!
# check how to use both get and post at once in this
# @app.route('/124',methods=["GET","POST"])
# def return_hello():
#     if request.form is not []:
#         return {"you gave the value":request.form['data']}
#     else:
#         return {"POst method called":"adasdsf"}
# write a standalone function to return all the results gathered by the ML algo as
# a simple JSON data

api.add_resource(TodoSimple,'/<string:todo_id>')
api.add_resource(VFD_control,'/vfd/<string:mode>/<string:value>')
# use lin/<any number> to get the value
# use lin/<reading> to put the value
api.add_resource(Linear,'/lin/<string:type>')
api.add_resource(Rotary,'/rot/<string:time>')
# api.add_resource(TodoSimple,'/')

print("server started!!")


if __name__ == '__main__':
    app.run(debug=True)
    print("server started!!")
