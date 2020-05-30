from app import app
from app import twitter

@app.route('/api/')
def index():
    twitter.registration()