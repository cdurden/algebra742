import sys
from flask import Flask
import subprocess32 as subprocess
#from subprocess import subprocess
import hashlib
import os
import io
import re
import json
import jinja2
import pygraphviz
from networkx.drawing import nx_agraph
import shlex
#from models.util import params_hash_lookup, graphics_path, process_quotes_for_json

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
    print(out)
    return(out)
app = Flask(__name__)
app.config.from_object('default_config')

loader = jinja2.FileSystemLoader(app.config['GRAPHICS_TEMPLATE_DIR'])
jinja_env = jinja2.Environment(loader=loader)
#def process_quotes(string):
#    """Generate parenthesized contents in string as pairs (level, contents)."""
#    stack = []
#    for i, c in enumerate(string):
#        if c == "'":
#            stack.append(i)
#        elif c == "'" and stack:
#            start = stack.pop()
#            yield (len(stack), string[start + 1: i])

#def process_quotes(s):
#    for quoted_part in re.findall(r"'(.+?)'", s):
#        # For each part that is within quotes replace the spaces with the pattern *#*#*#* or whatever you want
#        s = s.replace(quoted_part, quoted_part.replace("\"", "\\\""))
#    s = s.replace("'","\"")
#    return(s)
#def process_quotes(s):
#    for quoted_part in re.findall(r"\"(.+?)\"", s):
#        # For each part that is within quotes replace the spaces with the pattern *#*#*#* or whatever you want
#        s = s.replace(quoted_part, quoted_part.replace("'", "\\\""))
#    return(s)

with open(os.path.join(app.config["QUESTION_DIGRAPHS_DIR"],"ch5.dot"),"r") as f:
    src = f.read()
#print(process_quotes(src))

#def asy_params_hash_lookup(params):
#    return(hashlib.sha224(json.dumps(params).encode('utf-8')).hexdigest())

engines = {'Question.AsyGraphicsQuestion': ('asy',['asy','-f','svg','-o','{{ output_filename }}','-']),
'Question.DotGraphicsQuestion': ('dot',['dot','-Tsvg','-o','{{ output_filename }}'])}

questions_digraph = nx_agraph.from_agraph(pygraphviz.AGraph(src))
for node,data in questions_digraph.nodes(data=True):
    #print(data)
    if 'class' in data and data['class'].endswith('GraphicsQuestion'):
        params_json = process_quotes_for_json(data['params'])
        print(params_json)
        params = json.loads(params_json)
        #print(params)
        engine = engines[data['class']][0]
        output_filename = graphics_path(app,engine,params['template'],params_hash_lookup(params_json))
        print(output_filename)
        args = [jinja2.Template(arg).render(output_filename=output_filename) for arg in engines[data['class']][1]]
        template = jinja_env.get_template(os.path.join(engine,params['template']))
        src = template.render(**params).encode('utf-8')
        try:
            result = subprocess.run(
                    args,
                input=src,
                check=True,
                cwd="/tmp",
        #        stdin=subprocess.PIPE, 
                stdout=subprocess.PIPE,
                timeout=10,
            )
        #except subprocess.TimeoutExpired:
        #    pass
            # Handle exception
        except subprocess.CalledProcessError:
            pass
            # Handle exception
