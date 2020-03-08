from flask import current_app as app
import hashlib
import json
import shlex
import os

def asy_graphics_path(template, asy_params_hash):
    return('{:s}_{:s}.svg'.format(os.path.splitext(template)[0],asy_params_hash))

def asy_params_hash_lookup(params):
    return(hashlib.sha224(json.dumps(params).encode('utf-8')).hexdigest())

def process_quotes_for_json(s):
    lexer = shlex.shlex(s)
    out = ''
    for token in lexer:
        out += "{:s}".format(token.replace("'","\"").replace('\\\"',"\""))
    return(out)
