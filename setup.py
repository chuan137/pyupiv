#!/usr/bin/env python
import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name = 'Pyutils',
      version = '0.1',
      author = 'Chuan Miao',
      author_mail = 'chuan137@gmail.com', 
      description = 'simple helper functions', 
      keyword = 'helper functions',
      packages = ['pyutils'],
      license = 'GNU'
)
