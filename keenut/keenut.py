#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'Greg Albrecht <gba@onbeep.com>'
__copyright__ = 'Copyright 2013 OnBeep, Inc.'
__license__ = 'Apache License 2.0'


import PyNUT
import keen


class KeeNUT(object):

    def __init__(self, project_id, write_key, ups_name,
                 collection_name='ups_stats'):
        self.project_id = project_id
        self.write_key = write_key
        self.ups_name = ups_name
        self.collection_name = collection_name

    def _set_ups_client(self):
        return PyNUT.PyNUTClient()

    def _get_ups_stats(self):
        return self._set_ups_client().GetUPSVars(self.ups_name)

    def _clean_ups_stats(self, dirty_stats):
        clean_stats = {}

        for skey in dirty_stats.keys():
            try:
                clean_stat = float(dirty_stats[skey])
            except ValueError:
                try:
                    clean_stat = int(dirty_stats[skey])
                except ValueError:
                    clean_stat = dirty_stats[skey]
            clean_key = skey.replace('.', '_')
            clean_stats[clean_key] = clean_stat

    def _set_keen_client(selfself):
        return keen.KeenClient(project_id=self.project_id,
                               write_key=self.write_key)

    def send(self):
        self._set_keen_client().add_event(
            self.collection_name,
            self._clean_ups_stats(self._get_ups_stats()))