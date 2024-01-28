#!/usr/bin/python3
"""Start web web_flasklication with two routings
"""

from models import storage
from models.state import State
from flask import Flask, render_template
web_flask = Flask(__name__)


@web_flask.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_by_id():
    """ render template of states"""
    all_states = storage.all(State)
    if id:
        states = all_states.get('State.{}'.format(id))
    else:
        states = all_states.values()
    # ^ fetches states data from storage engine, then in line below,
    # those states are passed into the template
    return render_template('9-states.html', states=states)


@app.teardown_appcontext
def remove_SQLalc_session(exception):
    """ close storage when tear down is called """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
