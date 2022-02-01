#!/usr/bin/python3
"""
Script that starts a Flask web application listening 0.0.0.0 port 5000:
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities():
    """ Returns a list of states rendered on html """
    return render_template('8-cities_by_states.html',
                           states=storage.all(State).values())


@app.teardown_appcontext
def teardownMethod(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
