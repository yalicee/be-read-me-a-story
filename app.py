from flask import Flask
from flask import request
from firebase_admin import db
from flask_cors import cross_origin
from db.connection import app
import uuid
import time
import json

app = Flask(__name__)


@app.route("/")
@cross_origin()
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/stories', methods=['POST'])
@cross_origin()
def create_story():
    story = json.loads(request.data)
    if request.method == "POST":
        new_story = db.reference("stories/" + str(uuid.uuid4()))
        res = new_story.set({
            "title": story["title"],
            "created_by": story["userId"],
            "created_at": int(time.time()),
            "cover": "gs:/path/to/firebase/image.jpg",
            "chapters": [
                {
                    "created_by": story["userId"],
                    "chapter_src": story["chapterSource"],
                    "played": False
                }
            ],
            "families": {
                story["familyId"]: True
            }
        })
        response = app.response_class(
            response=json.dumps(new_story.get()), status=201, mimetype="application/json")
        return response
