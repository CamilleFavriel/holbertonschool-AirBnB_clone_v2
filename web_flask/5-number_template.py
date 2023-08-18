#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, abort, render_template


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
def C_is_fun(text):
    """display "C" followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    """display “n is a number” only if n is an integer"""
    if type(n) is int:
        return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """return n to html if it's an integer"""
    if isinstance(n, int):
        return render_template('5-number.html', n=n)
    else:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
