from flask import Flask
import subprocess
import hashlib
import os
import io
import re
import json
import jinja2
import pygraphviz
from networkx.drawing import nx_agraph
from util import asy_params_hash_lookup, asy_graphics_path, process_quotes_for_json
app = Flask(__name__)
app.config.from_object('default_config')

loader = jinja2.FileSystemLoader(app.config['ASY_TEMPLATE_DIR'])
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

questions_digraph = nx_agraph.from_agraph(pygraphviz.AGraph(src))
for node,data in questions_digraph.nodes(data=True):
    if 'class' in data and data['class'] == 'Question.AsyGraphicsQuestion':
        params = json.loads(process_quotes_for_json(data['params']))
        print(params)
        output_filename = asy_graphics_path(params['template'],asy_params_hash_lookup(params))
        template = jinja_env.get_template(params['template'])
        src = template.render(**params).encode('utf-8')
        try:
            result = subprocess.run(
                    ['asy','-f','svg','-o',output_filename,'-'],
                input=src,
                check=True,
                cwd=app.config['ASY_OUTPUT_DIR'],
        #        stdin=subprocess.PIPE, 
                stdout=subprocess.PIPE,
                timeout=10,
            )
        except subprocess.TimeoutExpired:
            pass
            # Handle exception
        except subprocess.CalledProcessError:
            pass
            # Handle exception

