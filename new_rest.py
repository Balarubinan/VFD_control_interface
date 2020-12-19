from flask_restful import Resource, Api
from flask import Flask,request
app = Flask(__name__)
api = Api(app)
from tkinter import *
from tkinter import font
from threading import Thread
todos = {}
current_val=0

def get_cur_read():
    return current_val

class TodoSimple(Resource):
    def get(self, todo_id):
        return {"value":current_val}

    def put(self, todo_id):
        # 'data' is like a name variable
        # hence in request it must be present as
        # {'data':'<actual data>'}
        # todos[todo_id] = request.form['data']
        current_val=request.form['reading']
        print("Captured reading is ",current_val)
        print("data saved!!!")
        # return {todo_id: todos[todo_id]}
        return {"status":"success!!"}

    def linear_reading(self):
        pass

    def linear_standby(self):
        pass

    def VFD_contorl(self):
        pass

    def rotary_one(self):
        pass



api.add_resource(TodoSimple,'/','/<string:todo_id>')

# app.run(debug=True)
# print("server started!!")


# if __name__ == '__main__':
#     app.run(debug=True)
#     print("server started!!")
