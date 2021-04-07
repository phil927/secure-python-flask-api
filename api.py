import flask
from flask import request, jsonify, abort
from argon2 import PasswordHasher
from database import *
import timeit

app = flask.Flask(__name__)
app.config["DEBUG"] = False

# https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
# Add weather data for our catalog
weather = [
    {"city": "Denver", "state": "Colorado", "date": "03/27/2021", "temperature": 58},
    {"city": "Denver", "state": "Colorado", "date": "03/28/2021", "temperature": 67},
    {"city": "Golden", "state": "Colorado", "date": "03/27/2021", "temperature": 46},
    {"city": "Golden", "state": "Colorado", "date": "03/28/2021", "temperature": 63},
]


@app.route("/", methods=["GET"])
def home():
    return "<h1>Phillip's Home Page</h1>"


@app.route("/api/v1/resources/weather/all", methods=["GET"])
def api_all():
    return jsonify(weather)


@app.route("/api/v1/resources/weather", methods=["GET"])
def api_id():
    # Retrieves all temperatures for city/state

    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if "city" in request.args and "state" in request.args:
        city = request.args["city"]
        state = request.args["state"]
    else:
        return "Error: no city/state provided. Please specify city/state"

    results = []
    for row in weather:
        if row["city"] == city and row["state"] == state:
            results.append(row)

    return jsonify(results)


@app.route("/api/v1/auth/register", methods=["POST"])
def api_register():
    # Calls on the DB method to register a user
    if "username" in request.args and "password" in request.args:
        username = request.args["username"]
        password = request.args["password"]
    else:
        abort(400, description="Error: either username or password not provided")

    if does_user_exist(username):
        abort(400, description="Error: User already exists")
    else:
        password_hash = PasswordHasher(hash_len=32).hash(password)
        print("Password Hash computed in User Registration: {0}".format(password_hash))
        registration_success = register_user(username, password_hash)
        if not registration_success:
            abort(500)
        else:
            return "User Registered!"


@app.route("/api/v1/upload", methods=["POST"])
def upload_file():
    uploaded_file = request.files["file"]
    if uploaded_file.filename != "":
        uploaded_file.save(uploaded_file.filename)
    return "File Saved"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)