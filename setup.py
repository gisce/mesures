#!/usr/bin/env python
from setuptools import setup, find_packages
from mesures import __version__, __author__

with open('requirements.txt') as f:
    data = f.read()
reqs = data.split()

setup(
    name='mesures',
    version=__version__,
    packages=find_packages(),
    install_requires=reqs,
    license='GNU GPL3',
    author=__author__,
    author_email='devel@gisce.net',
    description='Mesures'
)