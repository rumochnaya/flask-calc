__author__ = 'scorpius'

from flask import Flask
from . import calc

app = Flask(__name__)

app.register_blueprint(calc.bp_app)

