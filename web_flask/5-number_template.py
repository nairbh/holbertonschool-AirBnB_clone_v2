#!/usr/bin/python3
''' script that starts a Flask web application '''

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    ''' Function that display Hello HBNB! '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' Function that display HBNB '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def variable(text):
    ''' Function that display C + <text> '''
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    ''' Function that display Python + <text> '''
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    ''' Function that display <n> '''
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n):
    ''' Function that display template '''
    return render_template('5-number.html', num=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
