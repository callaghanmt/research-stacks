#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SciStack: the web app to build docker containers for reproducable science


"""
import os
import flask
import inspect
import gzip
from functools import wraps

app = flask.Flask(__name__, static_url_path='')


_PATH_HERE = os.path.dirname(
    os.path.abspath(
        inspect.getfile(inspect.currentframe()))
)
ROOT_DIR = os.path.join(_PATH_HERE, "..")
# Home of any pre-build docker files
docker_file_path = os.path.join(ROOT_DIR, "dockerfiles")

mylist = ["00_os_ubuntu_latest", "34_app_emacs", "18_lib_vtk"]

def create_Dockerfile(fragmentList):
    fragmentList.sort()

    Dockerfile = ""
    for fragment in fragmentList:
        fragmentfile = open(fragment, "r")
        Dockerfile = Dockerfile + fragmentfile.read()
        fragmentfile.close()

    return Dockerfile


@app.route("/")
def index():
    from parse_config import options_dict
    fragments = options_dict()
    return flask.render_template("main.html", os=fragments.get("os"), libs=fragments.get("lib"), apps=fragments.get("apps"), langs=fragments.get("lang"))

@app.route("/builddockerfile", methods=["POST"])
def dockerbuilder():
   from parse_config import required_files
   options = flask.request.form.to_dict()
   files = required_files(options)
   output = create_Dockerfile(files)
   return output

@app.route("/dfview/<path:fname>")
def send_dockerfile(fname):
    dockerfile = get_dockerfile_lines(os.path.join(docker_file_path, fname))
    return flask.render_template('dockerview.html', lines=dockerfile)

@app.route("/about.html")
def about():
    return flask.render_template('about.html')

@app.route("/contact.html")
def contact():
    return flask.render_template('contact.html')

def openfile(read_function):
    """Decorator to read data from files or file like instances.
       Adding the @openfile decorator to a function designed to read from a
       open file handle permits filenames to be given as arguments. If a string
       argument is given it is treated as a file name and opened prior to the 
       main read function being called. If the file name ends in .gz, the file
       is also uncompressed on the fly.
    """
    @wraps(read_function)
    def wrapped_function(f, **kwargs):
        if isinstance(f, str):
            if os.path.splitext(f)[1] == '.gz':
                with gzip.open(f, 'rt') as f:
                    return read_function(f, **kwargs)
            else:
                with open(f, 'r') as f:
                    return read_function(f, **kwargs)
        else:
            return read_function(f)

    return wrapped_function

@openfile
def get_dockerfile_lines(fh):
    """Read a dockerfile into a list of lines for rendering
    
    most of the guts of this is in openfile, which handles compressed files
    and URLs
    """
    dockerfile = []
    for line in fh:
        dockerfile.append(line.strip())
    return dockerfile
    

if __name__ == "__main__":
    app.run()

