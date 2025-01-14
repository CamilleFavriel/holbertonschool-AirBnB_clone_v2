#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """return: "Hello HBTN!"."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return: "HBTN!"."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c_with_text(text):
    """display "C" followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return f"C {text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
