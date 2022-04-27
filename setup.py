#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from mesures import __version__, __author__

with open('requirements.txt', 'r') as f:
    requirements = f.readlines()

setup(
    name='mesures',
    version=__version__,
    description="Eina d'intercanvi de fitxers de mesures de REE",
    provides=['mesures'],
    packages=find_packages(),
    install_requires=requirements,
    license='BSD 3-Clause License',
    author=__author__,
    author_email='devel@gisce.net',
    url='https://github.com/gisce/mesures',
)
