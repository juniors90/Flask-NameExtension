# -*- coding: utf-8 -*-
import os
import pathlib
import sys

from flask import Flask, render_template_string


# this path is pointing to project/docs/source
CURRENT_PATH = pathlib.Path(os.path.abspath(os.path.dirname(__file__)))
FLASK_EXTENSIONNAME_PATH = CURRENT_PATH.parent

sys.path.insert(0, str(FLASK_EXTENSIONNAME_PATH))

from flask_nameextension import NameExtension  # noqa

app = Flask(__name__)

extension_name = NameExtension(app)

@app.route("/")
def index():
    world = extension_name.hello(world="Juniors90")
    ctx = {
        "hello": world,
    }
    return render_template_string("Extension name say: {{ hello }}", **ctx)


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)