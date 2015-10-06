#!/usr/bin/env python
# coding: utf-8
from setuptools import setup

from replay_parser import VERSION


setup(
    name="rocket-league-replay-parser",
    version='.'.join(VERSION),
    url="https://github.com/danielsamuels/rocket-league-replay-parser",
    author="Daniel Samuels",
    author_email="daniel.samuels1@gmail.com",
    license="BSD",
    include_package_data=True,
    zip_safe=False,
    description='Parser for Rocket League replay files.',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',

    ],
)
