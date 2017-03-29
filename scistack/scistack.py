#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SciStack: the web app to build docker containers for reproducable science


"""
import os
import flask

app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "Choose a domain!"

if __name__ == "__main__":
    app.run()

