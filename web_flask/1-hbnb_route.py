#!/usr/bin/python3
""" Script that starts a Flask web application listening 0.0.0.0 port 5000:
    The route of the domain / displays 'Hello HBNB!'
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def domainFunction():
    """ Responsible of the domain route, displays a message """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnbFunction():
    """ Responsible of the /hbhb route, displays a message """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
