import hashlib
import json
import shlex
import os

def asy_graphics_path(app, template, asy_params_hash):
    return(os.path.join(app.config['ASY_OUTPUT_DIR'],'{:s}_{:s}.svg'.format(os.path.splitext(template)[0],asy_params_hash)))

def asy_params_hash_lookup(params):
    print(json.dumps(params))
    return(hashlib.sha224(json.dumps(params).encode('utf-8')).hexdigest())

def process_quotes_for_json(s):
    lexer = shlex.shlex(s)
    out = ''
    for token in lexer:
        out += "{:s}".format(token.replace("'","\""))
    return(out)
