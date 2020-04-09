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
    print(out)
    return(out)

class SerializableGenerator(list):
    """Generator that is serializable by JSON

    It is useful for serializing huge data by JSON
    >>> json.dumps(SerializableGenerator(iter([1, 2])))
    "[1, 2]"
    >>> json.dumps(SerializableGenerator(iter([])))
    "[]"

    It can be used in a generator of json chunks used e.g. for a stream
    >>> iter_json = ison.JSONEncoder().iterencode(SerializableGenerator(iter([])))
    >>> tuple(iter_json)
    ('[1', ']')
    # >>> for chunk in iter_json:
    # ...     stream.write(chunk)
    # >>> SerializableGenerator((x for x in range(3)))
    # [<generator object <genexpr> at 0x7f858b5180f8>]
    """

    def __init__(self, iterable):
        tmp_body = iter(iterable)
        try:
            self._head = iter([next(tmp_body)])
            self.append(tmp_body)
        except StopIteration:
            self._head = []

    def __iter__(self):
        return itertools.chain(self._head, *self[:1])
