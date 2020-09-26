# -*- coding: utf-8 -*-

import logging
from abc import ABCMeta

__author__ = 'nnedkov'


logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s: %(message)s',)
logger = logging.getLogger('ModelsBase')
logger.setLevel(logging.INFO)


class MeasurementBase(object):
    __metaclass__ = ABCMeta

    @classmethod
    def create_series(cls, session):
        mock_point = {
            'measurement': cls.__measurement__,
            'tags': {cls.__tag_name__: ''},
            'fields': {cls.__field_name__: cls.__field_type__(0)}
        }
        session.write_points([mock_point])

    @classmethod
    def get_field_name(cls):
        return cls.__field_name__

    @classmethod
    def get_tag_values(cls, session, tag):
        query_params = {
            'measurement': cls.__measurement__,
            'tag': tag
        }
        query = '''SHOW TAG VALUES
                   FROM {measurement}
                   WITH key = {tag};'''.format(**query_params)

        rs = session.query(query)
        tag_values = [i['value'] for i in rs.get_points()]

        return tag_values
