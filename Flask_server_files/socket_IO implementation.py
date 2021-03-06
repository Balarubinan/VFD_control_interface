# from flask import Flask, render_template, session, copy_current_request_context
# from flask_socketio import SocketIO, emit, disconnect
# from threading import Lock
# from flask_restful import Api
#
#
# async_mode = None
# app = Flask(__name__)
# api=Api(app)
# app.config['SECRET_KEY'] = 'secret!'
# socket_ = SocketIO(app, async_mode=async_mode)
# thread = None
# thread_lock = Lock()
#
#
# @app.route('/')
# def index():
#     # return render_template('index.html', async_mode=socket_.async_mode)
#     return {"hello":"Bala"}
#
#
# @socket_.on('my message', namespace='/test')
# def test_message(message):
#     session['receive_count'] = session.get('receive_count', 0) + 1
#     print("O responed!!")
#     emit('77',
#          {'data': message['data'], 'count': session['receive_count']})
#     return {"hsdd":"asfaf"}
#
#
# @socket_.on('my_broadcast_event', namespace='/test')
# def test_broadcast_message(message):
#     session['receive_count'] = session.get('receive_count', 0) + 1
#     emit('my_response',
#          {'data': message['data'], 'count': session['receive_count']},
#          broadcast=True)
#
#
# @socket_.on('disconnect_request', namespace='/test')
# def disconnect_request():
#     @copy_current_request_context
#     def can_disconnect():
#         disconnect()
#
#     session['receive_count'] = session.get('receive_count', 0) + 1
#     emit('my_response',
#          {'data': 'Disconnected!', 'count': session['receive_count']},
#          callback=can_disconnect)
#
#
# if __name__ == '__main__':
#     socket_.run(app, debug=True)
import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        print(message)
        await websocket.send(message)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 8765))
asyncio.get_event_loop().run_forever()