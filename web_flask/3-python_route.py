#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Hello"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hello():
    """HBNB"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def display_c_with_text(text):
    """C something"""
    text = text.replace('_', ' ')
    return f"C {text}"

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """Python something"""
    text = text.replace('_', ' ')
    return f"Python {text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
