# SciStacks
Reproducible software stacks for research

## Overview
* New PhD students and post-docs often join a group and need to get up and running with a core set of libraries, languages and applications
* More experienced researchers need to be able to select a set of libraries and applications and not have to be concerned about dependencies or versions.
* We want our research stacks to facilitate reproducible research to build once and deploy anywhere.
  
## Installation

A working Python 3 install with [Flask](http://flask.pocoo.org/) installed is required.  The easiest way to achieve this is to install [Anaconda Python](https://www.continuum.io/downloads) and then:


```
conda install flask
```

Start the service by running
```
python scistack/scistack.py
```
and go to http://127.0.0.1:5000 to use the service

