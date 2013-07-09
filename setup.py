#!/usr/bin/env python


__author__ = 'Greg Albrecht <gba@onbeep.com>'
__copyright__ = 'Copyright 2013 OnBeep, Inc.'
__license__ = 'Apache License 2.0'


import distutils


distutils.core.setup(
    name='keenut',
    version='0.1.0',
    packages=[''],
    url='http://github.com/ampledata/keenut',
    license='Apache License 2.0',
    author='Greg Albrecht',
    author_email='gba@onbeep.com',
    description='Utilities for collecting metrics from NUTs using Keen.io',
    entry_points={'console_scripts': ['keenut = keenut.cli:main']},
    install_requires=['PyNUT', 'keen']
)
