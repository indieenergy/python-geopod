#!/usr/bin/env python
# encoding: utf-8
"""
setup.py

Copyright (c) 2011 Indie Energy Systems Company, LLC.. All rights reserved.
"""

import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
    
    
setup(
    name="python-geopod",
    version="0.0.3",
    author="Michael Yagley",
    description="A client for the Indie Energy Systems Geopod API",
    packages=["geopod",],
    long_description=read('README'),
    install_requires=[
        'oauth2',
        'simplejson',
    ]
)


