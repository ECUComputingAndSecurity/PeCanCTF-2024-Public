#!/usr/bin/env python3
from flask import *
from typing import *
import random
import json
import os

class User:
    def __init__(self, uid: int, name: str, files: Dict[str, str]):
        self.uid: int = uid
        self.name: str = name
        self.email: str = name.replace(" ", ".").lower() + "@optimum.com.au"
        self.phone: str = "0" + "".join([random.choice("0123456789") for _ in range(9)])
        self.files: Dict[str, str] = files

    def file_url(self, file: str):
        if file not in self.files:
            value: Set[str] = {i for i in self.files if self.files[i] == file}
            if not value:
                raise ValueError("File not found.")
            file = value.pop()
        return f"/files/{self.uid}/{file}"

    def dictify(self):
        return {
            "uid": self.uid,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "files": [self.file_url(file) for file in self.files]
        }

FLAG_NAME: str = "Flag McFlagface"
USERS: List[User] = []

names: List[str] = [
    FLAG_NAME,
    "Ruby Jackson",
    "Linwood Benson",
    "Dominique Ray",
    "Candy Morris",
    "Aline Adkins",
    "Sebastian Hebert",
    "Amelia Carroll",
    "Janice Moody",
    "Ellsworth Lynn",
    "Jefferey Mclaughlin",
    "Della Warren",
    "Wesley Valentine",
    "Aurora Olson",
    "Jerrod Mccall",
    "Yesenia Alvarez",
    "Harriett Lutz",
    "Dudley Potts",
    "Minh Bauer",
    "Lydia Ford",
    "Howard Bush",
    "Kristina Li",
    "Bryon Gillespie",
    "Julian Meyer",
    "Forrest Pena",
    "Leroy Poole",
    "Wanda Nguyen",
    "Matthew Whitaker",
    "Larry Cordova",
    "Cecilia Odonnell",
    "Noel Mathews",
    "Marylou Valenzuela",
]
while names.index(FLAG_NAME) < 8:
    random.shuffle(names)

for i in range(len(names)):
    name: str = names[i]
    files: Dict[str, str] = {}
    if name == FLAG_NAME:
        files["meme.png"] = "meme.png"
        files["flag.txt"] = "flag.txt"
    USERS.append(User(i, name, files))


app = Flask(__name__)

def get_user_by_str(string_id: str) -> User | Response:
    try:
        uid: int = int(string_id)
        if uid < 0:
            raise ValueError("User ID must be >= 0")
        return USERS[uid]
    except ValueError as e:
        return jsonify({"error": str(e)}, 400)
    except IndexError:
        return jsonify({"error": "That user does not exist."}, 404)

@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/user/<string_id>/')
def get_user(string_id: str):
    user = get_user_by_str(string_id)
    if type(user) == Response:
        return user
    return jsonify(user.dictify())

@app.route('/api/user/<string_id>/change_name/')
@app.route('/api/user/<string_id>/change_email/')
@app.route('/api/user/<string_id>/change_phone/')
@app.route('/api/user/<string_id>/add_file/')
@app.route('/api/user/<string_id>/remove_file/')
def no_permissions(string_id: str):
    return jsonify({"error": "Insufficient permissions"}, 401)

@app.route('/api/<path:path>/')
def api_not_found(path):
    return jsonify({"error": f"API path '{path}' not found."}, 404)

@app.route('/files/<string_id>/<file>')
def get_file(string_id: str, file: str):
    user = get_user_by_str(string_id)
    if type(user) == Response:
        return user
    if file not in user.files:
        return jsonify({"error": "That file does not exist."}, 404)
    print("files", user.files[file])
    return send_from_directory("files", user.files[file])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
