
# # A very simple Flask Hello World app for you to get started with...

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello from Flask!'

from flask_restful import Resource, Api
from flask import Flask,request
from src.DBoperations import *

app = Flask(__name__)
api = Api(app)

def get_cur_read():
    return current_val

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
            # reset not working !!
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

    def post(self):
        global current, freq, voltage
        mode=request.form['mode']
        if mode=="control":
            self.control_module()
            return {"vfd feed":f"control updated {mode}"}

        value = request.form['value']
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
    # def __init__(self):

    def get(self):
        global pulse_values,pulse_read
        return {"pulses":pulse_read}

    def post(self):
        # modify this function to read 1's and 0's for every instant
        global pulse_read,pulse_values
        val=request.form['pulses']
        pulse_read+=val
        write_to_rotary(val)
        pulse_values.append(val)
        if len(pulse_values)==100:
            # remove one value
            pulse_values.pop(0)
        # add update graph function here

api.add_resource(TodoSimple,'/<string:todo_id>')
api.add_resource(VFD_control,'/vfd')
# use lin/<any number> to get the value
# use lin/<reading> to put the value
api.add_resource(Linear,'/lin/<string:reading>')
api.add_resource(Rotary,'/rot')
# api.add_resource(TodoSimple,'/')

# @app.route('/')
# def entry(r):
#     return {'this':'okay messge'}

# graph code to be added here

# app.run(debug=True)
print("server started!!")


if __name__ == '__main__':
    app.run(debug=True)
    print("server started!!")
