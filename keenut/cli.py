#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""CLI Utilities for keenut."""


__author__ = 'Greg Albrecht <gba@onbeep.com>'
__copyright__ = 'Copyright 2013 OnBeep, Inc.'
__license__ = 'Apache License 2.0'


import optparse
import keenut


def main():
    optp = optparse.OptionParser()

    optp.add_option('-p', '--project_id', dest='project_id',
                    help='Keen.io Project ID.')
    optp.add_option('-w', '--write_key', dest='write_key',
                    help='Keen.io Write Key.')
    optp.add_option('-u', '--ups_name', dest='ups_name',
                    help='Name of UPS to query.')

    opts, args = optp.parse_args()

    kn = keenut.KeenNUT(project_id=opts.project_id, write_key=opts.write_key,
                        ups_name=opts.ups_name)
    return kn.send()