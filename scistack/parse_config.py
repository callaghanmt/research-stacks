"""
read the ./config folder (contains fragments of Dockerfiles)
and create a structure for populating
"""
import glob
import os

from scistack import ROOT_DIR

CONFIG_DIR = os.path.join(ROOT_DIR, 'config')

def config_files():
    """
    return a list of config files
    based on listing the path
    """
    cfg_start = '[0-9]*'
    poss_cfgs = os.path.join(CONFIG_DIR, cfg_start)
    paths = glob.glob(poss_cfgs)
    files = [os.path.basename(p) for p in paths]
    return files

def options_dict():
    """
    return mapping of options with headline as Keys
    e.g.
    {'os':['ubuntu'], 'langs': ['r', 'python3']}
    """
    files = config_files()
    keys = set([f.split('_')[1] for f in files])
    options = {k:[] for k in keys}
    for file_ in files:
        head_opt, val = file_.split('_')[1:3]
        options[head_opt].append(val)
    return options


def required_files(opts_dict):
    """
    build list of Dockerfile-fragments
    based on a flask.request.form. This is a
    ImmutableMultiDict (see 
    http://werkzeug.pocoo.org/docs/0.11/datastructures/)
    which is like a dict, but can have multiple keys with
    the same value and has a getlist method to group values
    of such keys.
    """
    matcher = '[0-9]*_{0}_{1}*'
    file_list = []
    for key in opts_dict.keys():
        for value in opts_dict.getlist(key):
            poss_file = matcher.format(key, value)
            poss_path = os.path.join(CONFIG_DIR, poss_file)
            matches = glob.glob(poss_path)
            if matches:
                file_list.append(matches[0])
    return file_list


if __name__ == '__main__':
    OPTS = {'os': ['ubuntu'], 'lang': ['R', 'python2', 'haskel']}
    print()
    print('######## search for files matching dict of lists ####')
    print(required_files(OPTS))
    print()
    print()
    print('######## populate dict of poss lists from files found ####')
    print(options_dict())



