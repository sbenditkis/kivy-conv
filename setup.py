import sys
import os
from os.path import join, dirname
from os import environ
from distutils.core import setup
from distutils.extension import Extension


# indicate which extensions we want to compile
extensions = [
    Extension('conv', ['conv.c'])
    #Extension('conv')
    ]

setup(
    name='conv',
    version='0.1',
    ext_modules=extensions
)
