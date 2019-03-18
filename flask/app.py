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
    open_id = request.args.get('open_id')

    checkArguments(username, open_id)
        
    db = getDatabase()
    result = db.login(open_id)
    if result is None:
        db.signup(username, open_id)
        result = db.login(open_id)

    if result is None:
        abort(400)

    userID, username = result
    session['user_id'] = userID
    return jsonify(username=username), 200

@app.route('/question', methods=['GET', 'POST'])
def question():
    checkLogin()

    db = getDatabase()

    if request.method == 'GET':
        return _fetchQuestion(request, db)
    else:
        uid = session['user_id']
        return _postQuestion(request, uid, db)

def _fetchQuestion(request, db):
    start = request.args.get('start', 0)
    count = request.args.get('count', 10)

    questions = db.fetchQuestions(start, count)
    return jsonify(questions=[q.serialize() for q in questions]), 200

def _postQuestion(request, uid, db):
    text = request.args['text']
    title = request.args['title']

    if text is None or title is None:
        abort(400)
    
    db.insertQuestion(uid, title, text)
    return jsonify(msg='ask question success'), 200

@app.route('/my_answer')
def myAnswers():
    checkLogin()

    db = getDatabase()

    start = request.args.get('start', 0)
    count = request.args.get('count', 10)
    uid = session['user_id']
    answers = db.fetchMyAnswers(uid, start, count)

    return jsonify(questions=[a.serialize() for a in answers]), 200

@app.route('/answer', methods=['GET', 'POST'])
def answer():
    checkLogin()

    db = getDatabase()

    if request.method == 'GET':
        return _fetchAnswer(request, db)
    else:
        uid = session['user_id']
        return _postAnswer(request, uid, db)

def _fetchAnswer(request, db):
    q_id = request.args['q_id']
    if q_id is None:
        abort(400)

    start = request.args.get('start', 0)
    count = request.args.get('count', 10)
    
    answers = db.fetchAnswers(q_id, start, count)
    return jsonify(questions=[a.serialize() for a in answers]), 200

def _postAnswer(request, uid, db):
    q_id = request.args['q_id']
    if q_id is None:
        abort(400)
    
    text = request.args['text']
    if text is None:
        abort(400)

    db.insertAnswer(uid, q_id, text)
    return jsonify(msg='answer success'), 200

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
        g.db = Database('bucket_list')

    if g.db is None:
        abort(400)

    return g.db

@app.teardown_appcontext
def closeDatabase(exe):
    db = g.pop('db', None)

    if db is not None:
        db.close()

if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
