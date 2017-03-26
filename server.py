#!/usr/bin/python
import os
import psycopg2
import psycopg2.extras
from flask import Flask, session, request, render_template
from flask_socketio import SocketIO, emit
import string

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)

@socketio.on('connect', namespace='/')
def loadUpcomingGames():
	conn = connectToDB()
	cur = conn.cursor()
	
	query = "SELECT * FROM games;"

@app.route('/')
def mainIndex():
	return app.send_static_file('index.html')

# start the server
if __name__ == '__main__':
	socketio.run(app, host-os.getenv('IP', '0.0.0.0'),
	port = int(os.getenv('PORT', 8080)), debug=True)
print "Starting server"
