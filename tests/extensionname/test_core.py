#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of the
# Flask-NameExtension Project (https://github.com/juniors90/Flask-NameExtension/).
# Copyright (c) 2022, Ferreira Juan David
# License: MIT
# Full Text: https://github.com/juniors90/Flask-NameExtension/blob/master/LICENSE

def test_hello(extensionname):
    say = extensionname.hello("World")
    assert say == "Hello World!!"