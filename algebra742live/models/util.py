import hashlib
import json
import shlex
import os

def graphics_path(app, engine, template, asy_params_hash):
    return(os.path.join(app.config['GRAPHICS_OUTPUT_DIR'],engine,'{:s}_{:s}.svg'.format(os.path.splitext(template)[0],asy_params_hash)))

def params_hash_lookup(params_json):
    print(params_json)
    return(hashlib.sha224(params_json.encode('utf-8')).hexdigest())

def process_quotes_for_json(s):
    lexer = shlex.shlex(s)
    out = ''
    for token in lexer:
        out += "{:s}".format(token.replace("'","\""))
    return(out)
