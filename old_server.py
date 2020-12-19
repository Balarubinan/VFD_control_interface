
# # A very simple Flask Hello World app for you to get started with...

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello from Flask!'

from flask_restful import Resource, Api
from flask import Flask,request

app = Flask(__name__)
api = Api(app)
from tkinter import *
from tkinter import font
from threading import Thread
todos = {}
current_val=0
a=[]

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

api.add_resource(TodoSimple,'/<string:todo_id>')
# api.add_resource(TodoSimple,'/')

# @app.route('/')
# def entry(r):
#     return {'this':'okay messge'}

# graph code to be added here

# app.run(debug=True)
print("server started!!")


# if __name__ == '__main__':
#     app.run(debug=True)
#     print("server started!!")
