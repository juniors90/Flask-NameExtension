#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of the
# Flask-NameExtension Project (https://github.com/juniors90/Flask-NameExtension/).
# Copyright (c) 2022, Ferreira Juan David
# License: MIT
# Full Text: https://github.com/juniors90/Flask-NameExtension/blob/master/LICENSE

# =============================================================================
# DOCS
# =============================================================================

import typing as t

import flask
from flask import render_template_string

import pytest

if t.TYPE_CHECKING:
    from flask.testing import FlaskClient


@pytest.fixture(autouse=True)
def app() -> "flask.Flask":
    app = flask.Flask(__name__)
    app.testing = True
    app.secret_key = "for test"
    app.debug = False

    @app.route("/")
    def index():
        ctx = {
            'extension': "Flask ExtensionName"
        }
        return render_template_string("Hello {{ extension}}!!", **ctx)

    yield app


@pytest.fixture
def client(app: "flask.Flask") -> "FlaskClient":
    context = app.test_request_context()
    context.push()

    with app.test_client() as client:
        yield client

    context.pop()