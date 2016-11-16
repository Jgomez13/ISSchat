import os
import uuid
from flask import Flask, session
from flask_socketio import SocketIO, emit

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'secret!'

socketio= SocketIO(app)

messages = [{'text': 'Booting System', 'name':'Bot'},
			{'text': 'ISS Chat now Live!', 'name':'Bot'}]

users = {}

@socketio.on('connect', namespace='/iss')
def makeConnection():
	print('\nin connected\n')
	session['uuid'] = uuid.uuid1()
	session['username'] = 'New user'
	users[session['uuid']] = {'username':'New user'}
	for message in messages:
		print("loop")
		print(message)
		emit('message', message)

@socketio.on('identify', namespace='/iss')
def on_identify(message):
	# takes care of the name being passed in at Name:
	print('identify '+ message)
	users[session['uuid']] = {'useraname': message}

@app.route('/')
def mainIndex():
    print('in hello world')
    return app.send_static_file('index.html')
    


# start the server
if __name__ == '__main__':
	#print('in Main')
	socketio.run(app, host=os.getenv('IP', '0.0.0.0'), port =int(os.getenv('PORT', 8080)), debug=True)
