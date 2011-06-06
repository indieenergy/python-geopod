#!/usr/bin/env python
# encoding: utf-8
"""
__init__.py

Copyright (c) 2011 Indie Energy Systems Company, LLC.. All rights reserved.
"""

import client
from client import *


VERSION = (0, 0, 2)

def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    return version
    
    
__version__ = get_version()

