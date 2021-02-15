import flask
from flask import request, jsonify
from hashlib import sha512

app = flask.Flask(__name__)
login_page = open('login.html', 'rb').read()
login_success = open('login-success.html', 'rb').read()
login_failed = open('login-failed.html', 'rb').read()

@app.route('/', methods=['GET'])
def home():
    return login_page

@app.route('/login', methods=['GET', 'POST'])
def login():
    database = open('database.json', 'rb').read()
    database = eval(database)

    username = request.form['username']
    password = request.form['password']
    password = sha512(password.encode()).hexdigest()

    for i in database[0]['data']:
        if i['username'] == username:
            if i['password'] == password:
                return login_success, 200
            
    return login_failed, 403

app.run(host="0.0.0.0", debug=True)