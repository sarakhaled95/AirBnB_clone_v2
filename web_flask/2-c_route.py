#!/usr/bin/python3
""" starts a Flask web application """

from flask import Flask

web_flask = Flask(__name__)

@web_flask.route("/", strict_slashes=False)
def hello_route():
    """ hello method """
    return ("Hello HBNB!")

@web_flask.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """ hbnb method """
    return ("HBNB")

@web_flask.route("/c/<text>", strict_slashes=False)
def C_route(text):
    """ c method """
    text = text.relace('_', ' ')
    return ('C' + ' ' + text)

if __name__ == "__main__":
    web_flask.run(host='0.0.0.0', port=5000)