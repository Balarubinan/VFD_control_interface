from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from DBoperations import write_todo
app = Flask(__name__)
api = Api(app)
CORS(app)
todos = {}

# class TodoSimple(Resource):
#     def get(self, todo_id=1):
#         return jsonify({todo_id: todos[todo_id]})
#
#     def put(self, todo_id=1):
#         todos[todo_id] = request.form['data']
#         return {todo_id: todos[todo_id]}

# @app.route('/getty',methods=['POST','GET'])
# def get_string():
#     print(request.method)
#     print("json data is ",request.get_json(force=True))
#     return("This fucking worked!!")

class TodoSimple(Resource):
    def get(self):
        todo_id=request.get_json(force=True)['id']
        return {todo_id:todos[todo_id]}

    def post(self):
        todo_id=request.get_json(force=True)['id']
        todo_text = request.get_json(force=True)['text']
        todos[todo_id]=todo_text
        print(todos[todo_id])
        return {todo_id:todo_text}




api.add_resource(TodoSimple, '/')
# api.add_resource(say_hello_dude,'/hello')

if __name__ == '__main__':
    app.run(debug=True)