from app import app
from app import twitter
from flask import request


@app.route('/api/', methods=['POST'])
def index():
    user_profile = {'username': request.json['username'], 'password': request.json['password']}
    username = user_profile['username']
    password = user_profile['password']
    twitter.registration(username, password)
