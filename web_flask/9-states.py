#!/usr/bin/python3
"""
Script that starts a Flask web application listening 0.0.0.0 port 5000:
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def statesOrCitiesListMethod(id=None):
    """Returns a list of states or cities renderd on html"""
    states_list = storage.all(State)
    if id:
        key = "State." + id
        if key in states_list:
            state = states_list[key]
        else:
            state = None
    else:
        state = storage.all(State).values()
    return render_template('9-states.html', states=state, id=id)


@app.teardown_appcontext
def teardownMethod(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
