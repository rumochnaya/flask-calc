#!/usr/bin/env python

__author__ = 'scorpius'

import os
from flask.ext.script import Manager
from flask.ext.script import Server

from flask_calc import app




manager = Manager(app)
manager.add_command("debug", Server(use_debugger=True))

manager.add_command("runserver", Server(host="0.0.0.0"))


@manager.command
def test(coverage=False):
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == "__main__":
    manager.run()
