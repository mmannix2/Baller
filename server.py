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

def connectToDB():
    connectString = 'dbname=basket user=jeff password=hack host=localhost'
    try:
        print("Connected to the database!")
        return psycopg2.connect(connectString)
    except:
        print("Can't connect to the database!")

def addPlayer(info):
    conn = connectToDB()
    cur = conn.cursor()

    phone=info['phone']
    zipCode=info['zip']
    zipRange=info['zipR']
    name = info['name']
    intensity = info['intensity']
    fun = info['fun']
    intense = info['intense']
    hardcore = info['hardcore']
    
    command = cur.mogrify("INSERT INTO players (phone, name, zipcode, ziprange, fun, intense, hardcore) VALUES (%s,%s,%s,%s,%s,%s,%s)",(phone, name, zipCode, zipRange, fun, intense, hardcore) )
    
    try:
        cur.execute(command)
    except Exception as e:
        print "Failed to add player"
        print e

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
	socketio.run(app, host=os.getenv('IP', '0.0.0.0'),
	port = int(os.getenv('PORT', 8080)), debug=True)

print "Starting server"
