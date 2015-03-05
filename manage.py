#!/usr/bin/env python

__author__ = 'scorpius'


from flask.ext.script import Manager
from flask.ext.script import Server

from flask_calc import app


manager = Manager(app)
manager.add_command("runserver", Server(use_debugger=True))


if __name__ == "__main__":
    manager.run()
