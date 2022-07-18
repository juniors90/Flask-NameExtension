#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of the
# Flask-NameExtension Project (https://github.com/juniors90/Flask-NameExtension/).
# Copyright (c) 2022, Ferreira Juan David
# License: MIT
# Full Text: https://github.com/juniors90/Flask-NameExtension/blob/master/LICENSE

# =============================================================================
# TESTS
# =============================================================================

import re

from flask_nameextension import NameExtension

import pytest as pt


@pt.fixture(autouse=True)
def extensionname(app):
    yield NameExtension(app)



