from flask import Flask
from flask import session, abort, g
from flask import make_response, jsonify, request

from .database import Database

import uuid
import os

app = Flask(__name__)
app.secret_key = '74125e09659a2249325d4200be9ee88d'

pwd = d8dd9fe2214c40ed4a8bfb6bb3e48a20

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'gif', 'png', 'bmp'])

def _checkArguments(*args):
    for arg in args:
        if arg is None:
            abort(400)
            break

def _assertLogin():
    login_status = session['is_logged_in']
    if login_status is None or login_status == false:
        abort(400)
    return True

def _allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/login', methods=['POST'])
def login():
    username = request.args.get('username')
    password = request.args.get('')

    self._checkArguments(username, password)

    if password != pwd:
        abort(502)

    session['is_logged_in'] = true
           
@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['file']

    self._checkArguments(uploaded_file)

    if not _allowed_file(uploaded_file.filename):
        abort(400)

    folder = 'images'
    filename = str(uuid.uuid4().hex) + '_' + str(int(time.time()))
    uploaded_file.save(os.path.join(folder, filename))

    db = getDatabase()
    db.upload_image(filename)

    return jsonify(msg='success'), 200


def getDatabase():
    if 'db' not in g:
        g.db = Database('suns')

    if g.db is None:
        abort(400)
    
    return g.db

@app.teardown_appcontext
def closeDatabase(exe):
    db = g.pop('db', None)

    if db is not None:
        db.close()