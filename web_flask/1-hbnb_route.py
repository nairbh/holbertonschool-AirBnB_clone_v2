#!/usr/bin/python3
"""flask import """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def dislplayHbnb():
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
