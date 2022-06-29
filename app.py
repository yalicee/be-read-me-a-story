from flask import Flask
from firebase_admin import db
from db.connection import app

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/json', methods=['POST', 'GET'])
def test_json():
    return '{"code": 1, "message": "Hello, World!" }'

@app.route('/stories', methods=['GET'])
def get_stories():
    stories = db.reference("/stories")
    return stories.get()
