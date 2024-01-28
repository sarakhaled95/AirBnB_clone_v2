#!/usr/bin/python3
"""Start web web_flasklication with two routings
"""

from models import storage
from models.state import State
from flask import Flask, render_template
web_flask = Flask(__name__)


@web_flask.route('/cities_by_states')
def states_list():
    """Render template with states
    """
    path = '8-cities_by_states.html'
    states = storage.all(State)

    # sort State object alphabetically by name
    # sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template(path, states=states)


@web_flask.teardown_web_flaskcontext
def web_flask_teardown(arg=None):
    """Clean-up session
    """
    storage.close()


if __name__ == '__main__':
    web_flask.url_map.strict_slashes = False
    web_flask.run(host='0.0.0.0', port=5000)