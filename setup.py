#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from mesures import __version__, __author__

with open('requirements.txt') as f:
    data = f.read()
reqs = data.split()

setup(
    name='mesures',
    version=__version__,
    description="Eina intercambi fitxers de mesures REE",
    provides=['mesures'],
    packages=find_packages(),
    install_requires=reqs,
    license='General Public Licence 3',
    author=__author__,
    author_email='devel@gisce.net',
)
