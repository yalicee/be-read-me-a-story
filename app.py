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


@app.route("/stories", methods=["POST"])
@cross_origin()
def create_story():
    story = json.loads(request.data)
    if request.method == "POST":
        new_story = db.reference("stories/" + str(uuid.uuid4()))
        try:
            new_story.set(
                {
                    "title": story["title"],
                    "created_by": story["userId"],
                    "created_at": int(time.time()),
                    "cover": "gs:/path/to/firebase/image.jpg",
                    "chapters": [
                        {
                            "created_by": story["userId"],
                            "chapter_src": story["chapterSource"],
                            "played": False,
                        }
                    ],
                    "families": {story["familyId"]: True},
                }
            )
            return jsonify(new_story.get()), 201
        except:
            return jsonify({"msg": "Could not create story"}), 400


@app.route("/stories/<family_id>", methods=["GET"])
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


@app.route('/stories/story/<story_id>', methods=['GET', 'PATCH'])
@cross_origin()
def story(story_id):
    if request.method == "GET":
        try:
            story_ref = db.reference("stories/" + story_id)
            story = story_ref.get()
            return jsonify(story), 200
        except:
            return jsonify({"msg": "Story not found"}), 404
    if request.method == "PATCH":
        try:
            story_ref = db.reference("/stories/" + story_id + "/chapters")
            chapters = story_ref.get()
            request_data = request.get_json()
            chapters.append({
                "created_by": request_data["userId"],
                "chapter_src": request_data["chapterSource"],
                "played": False
            })
            res = story_ref.set(chapters)
            return jsonify({"msg": "Chapter added"}), 201
        except:
            return jsonify({"msg": "Could not update story"}), 400


@app.route("/users", methods=["POST"])
@cross_origin()
def create_user():
    if request.method == "POST":
        request_data = request.get_json()
        family_id = str(uuid.uuid4())
        families = db.reference("families/" + family_id)
        res = families.set(
            {
                "family_name": request_data["familyName"],
                "members": {request_data["userId"]: True},
                "admins": {request_data["userId"]: True},
                "stories": {},
            }
        )
        users = db.reference("users/" + request_data["userId"])
        res = users.set(
            {
                "email": request_data["email"],
                "name": request_data["fullName"],
                "display_name": request_data["displayName"],
                "families": {
                    family_id: True,
                },
                "invited": False,
            }
        )

        json_family_id = jsonify({"family_id": family_id})

        return json_family_id, 201


@ app.route('/users/invites/<family_id>', methods=['POST'])
@ cross_origin()
def create_invited_user_in_family(family_id):
    if request.method == "POST":
        request_data = request.get_json()

        try:
            family_ref = db.reference("families/" + family_id)

            family = family_ref.get()

            family["members"][request_data["userId"]] = True
            family_ref.set(family)
        except:
            return jsonify({"msg": "Family could not be updated"}), 400

        try:
            users = db.reference("users/" + request_data["userId"])
            users.set(
                {
                    "email": request_data["email"],
                    "name": request_data["fullName"],
                    "display_name": request_data["displayName"],
                    "families": {
                        family_id: True,
                    },
                    "invited": False,
                }
            )
            invite_ref = db.reference("invites/" + request_data["userId"])
            invite_ref.delete()

            json_family_id = jsonify({"family_id": family_id})

            return json_family_id, 201
        except:
            return jsonify({"msg": "User could not be created"}), 400


@ app.route('/users/<user_id>', methods=['GET', 'PATCH'])
@ cross_origin()
def get_user_by_id(user_id):
    if request.method == "GET":
        users_ref = db.reference("users/" + user_id)
        user = users_ref.get()
        if user != None:
            return jsonify(user), 200
        else:
            return jsonify({"msg": "User not found"}), 404

    if request.method == "PATCH":
        users_ref = db.reference("users/" + user_id)
        user = users_ref.get()
        request_data = request.get_json()
        user["display_name"] = request_data["displayName"]
        user["name"] = request_data["fullName"]
        user["invited"] = False
        res = users_ref.set(user)
        return jsonify(users_ref.get()), 202


@app.route('/users/email/<email>', methods=['GET'])
@cross_origin()
def get_user_by_email(email):
    if request.method == "GET":
        try:
            invites_ref = db.reference("invites/")
            invited_users = invites_ref.get()
            for invited_user in invited_users:
                if invited_users[invited_user]["email"] == email:
                    return {invited_user: invited_users[invited_user]}, 200
        except:
            return jsonify({"new_user": True}), 204


@app.route("/users/invited", methods=["POST"])
@cross_origin()
def create_invited_user():
    if request.method == "POST":
        request_data = request.get_json()

        invite_ref = db.reference("invites/")
        invite_ref.push(
            {
                "email": request_data["email"],
                "invited": True,
                "families": {request_data["familyId"]: True},
            }
        )

        return jsonify({"msg": "user created"}), 201
