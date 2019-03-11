from flask import Flask
from flask import render_template, g, current_app
from flask import make_response, jsonify, request
from flask import abort, session

from model import Database

import os
import socket

app = Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def greet():
    return render_template('note.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    checkArguments(username, password)
        
    db = getDatabase()
    userID = db.userValidate(username, password)
    if userID is None:
        abort(400)

    session['user_id'] = userID
    return jsonify(msg='login success'), 200

@app.route('/list/')
def list():
    checkLogin()

    start = request.args.get('start', 0)
    count = request.args.get('count', 10)

    db = getDatabase()
    userID = session['user_id']
    cnt = db.wishlist(userID, start, count)
    return jsonify(wish_list=cnt), 200

@app.route('/post/', methods=['POST'])
def post():
    checkLogin()

    userID = session['user_id']
    title = request.args.get('title')
    cnt = request.args.get('content')
    db = getDatabase()

    checkArguments(title, cnt, db)

    postSuccess = db.post(userID, title, cnt)
    if not postSuccess:
        abort(400)

    return jsonify(msg='post success'), 200

def checkArguments(*args):
    for arg in args:
        if arg is None:
            abort(400)
            break

def checkLogin():
    if 'user_id' not in session:
        abort(400)

def getDatabase():
    if 'db' not in g:
        g.db = Database('./wish_list')

    if g.db is None:
        abort(400)

    return g.db

@app.teardown_appcontext
def closeDatabase(exec):
    db = g.pop('db', None)

    if db is not None:
        db.close()

if __name__ == '__main__':
    Database.createTable('./wish_list', 'schema.sql')

    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run(host='0.0.0.0', port=80)
