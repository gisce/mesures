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
    description="Eina d'intercanvi fitxers de mesures REE",
    provides=['mesures'],
    packages=find_packages(),
    install_requires=reqs,
    license='BSD 3-Clause License',
    author='GISCE-TI S.L.',
    author_email='devel@gisce.net',
    url = 'https://github.com/gisce/mesures',
)
