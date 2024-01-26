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


@web_flask.route("/python/<text>", strict_slashes=False)
def python_route(text=None):
    """ python method """
    if text is None:
        text = 'is cool'
    else:
        text = text.relace('_', ' ')
    return ('python' + ' ' + text)


@web_flask.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """ number method """
    return ("{:d} is a number".format(n))


@web_flask.route("/number_template/<int:n>", strict_slashes=False)
def number_template_route(n):
    """ number template method """
    return render_template('5-number.html', n=n)


@web_flask.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_even_route(n):
    """ number template method """
    path = '6-number_odd_or_even.html'
    return render_template(path, n=n)


if __name__ == "__main__":
    web_flask.run(host='0.0.0.0', port=5000)
