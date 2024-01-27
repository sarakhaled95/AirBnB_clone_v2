#!/usr/bin/python3
""" starts a Flask web application """
from models import *
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
from flask import Flask, render_template
web_flask = Flask(__name__)
classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


@web_flask.route('/states_list', strict_slashes=False)
def states_list():
    """ display HTML page with list of states """
    states = storage.all(classes["State"]).values()
    # ^ fetches States data from storage engine, then in line below,
    # those states are passed into the template
    return render_template('7-states_list.html', states=states)


@web_flask.teardown_appcontext
def remove_SQLalc_session(exception):
    """ close storage when tear down is executed """
    storage.close()

if __name__ == '__main__':
    web_flask.run(host='0.0.0.0', port=5000)