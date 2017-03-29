#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SciStack: the web app to build docker containers for reproducable science


"""
import os
import flask
import inspect

app = flask.Flask(__name__, static_url_path='')

# Home of any pre-build docker files
docker_file_path = os.path.join(os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe()))), "..", "dockerfiles")

@app.route("/")
def index():
    return flask.render_template("main.html")

@app.route("/dfview/<path:fname>")
def send_dockerfile(fname):
    with open(os.path.join(docker_file_path, fname)) as dfile:
        return_value = dfile.read()
    return return_value

if __name__ == "__main__":
    app.run()

