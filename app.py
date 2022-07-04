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
        try:
            new_story.set({
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
            return jsonify(new_story.get()), 201
        except:
            return jsonify({"msg": "Could not create story"}), 400


@app.route('/stories/<family_id>', methods=['GET'])
@cross_origin()
def get_stories_by_family(family_id):
    if request.method == "GET":
        stories_ref = db.reference("stories/")
        stories = stories_ref.get()
        try:
            stories_by_family = []
            for k, v in stories.items():
                if family_id in v["families"]:
                    stories_by_family.append({k: v})
            return jsonify(stories_by_family), 200
        except:
            return jsonify({"msg": "Family not found"}), 400


<<<<<<< HEAD
@app.route('/users', methods=['POST'])
=======
@app.route('/stories/<family_id>/<story_title>', methods=["GET"])
>>>>>>> main
@cross_origin()
def get_story(family_id, story_title):
    if request.method == "GET":
        family_stories = json.loads(get_stories_by_family(family_id).data)
        for story in family_stories:
            returnedStory = list(story.values())[0]
            if list(story.values())[0]["title"] == story_title:
                return jsonify(returnedStory), 200
            else:
                return jsonify({"msg": "Story not found"}), 404


@ app.route('/users', methods=['POST'])
@ cross_origin()
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
            },
            "invited": False,
        })

        json_family_id = jsonify({"family_id": family_id})

        return json_family_id, 201


@ app.route('/users/<user_id>', methods=['GET'])
@ cross_origin()
def get_user_by_id(user_id):
    if request.method == "GET":
        users_ref = db.reference("users/" + user_id)
        user = users_ref.get()
        if user != None:
            return jsonify(user), 200
        else:
            return jsonify({"msg": "User not found"}), 404
<<<<<<< HEAD


@app.route('/users/email/<email>', methods=['GET'])
@cross_origin()
def get_user_by_email(email):
    if request.method == "GET":
        users_ref = db.reference("users/")
        users = users_ref.get()
        for user in users:
            if users[user]["email"] == email:
                return {user: users[user]}, 200
        return jsonify({"msg": "User not found"}), 404
=======
>>>>>>> main
