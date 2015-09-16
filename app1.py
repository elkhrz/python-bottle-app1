from bottle import route, run, get, post, request
import pymongo
from pymongo import MongoClient
#import guestbookDAO

connection_string = 'mongodb://localhost'
client = MongoClient(connection_string)
db = client.test
collection = db.login

@route('/hello')
def hello():
    return "Hello World!"

@route('/login')
@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''
usernames = ["username", "user"]
passwords = ["password", "pass"]
def check_login(username, password):
    if username in usernames and password in passwords:
        return True
    else:
        return False

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

run(host='localhost', port=8080, debug=True)