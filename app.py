from flask import Flask, request, jsonify
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

@app.route('/stories/<family_id>', methods=['GET'])
@cross_origin()
def get_stories_by_family(family_id):
    if request.method == "GET":
        stories_ref = db.reference("stories/")
        stories = stories_ref.get()
        try:
            stories_by_family = {k: v for k, v in stories.items() if v["families"][family_id] == True}
            return jsonify(stories_by_family), 200
        except:
            return jsonify({"msg": "Family not found"}), 400


@app.route('/users', methods=['POST'])
@cross_origin()
def create_user():
    if request.method == "POST":
        request_data = request.get_json()
        family_id = str(uuid.uuid4())
        families = db.reference("families/" + family_id)
        res = families.set({
            "family_name": request_data["familyName"],
            "members": {
                request_data["userId"]: True
            },
            "admins": {
                request_data["userId"]: True
            },
            "stories": {}
        })
        users = db.reference("users/" + request_data["userId"])
        res = users.set({
            "email": request_data["email"],
            "name": request_data["fullName"],
            "display_name": request_data["displayName"],
            "families": {
                family_id: True,
            }
        })

        json_family_id = jsonify({"family_id": family_id})

        return json_family_id, 201
