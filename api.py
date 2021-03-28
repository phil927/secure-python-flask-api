import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

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


app.run()