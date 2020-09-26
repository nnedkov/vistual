# -*- coding: utf-8 -*-

from .models_base import MeasurementBase

__author__ = 'nnedkov'


class VistualVariable(MeasurementBase):
    __measurement__ = 'vistual'
    __field_name__ = 'value'
    __field_type__ = int
    __tag_name__ = 'variable'

    @classmethod
    def write_point(cls, session, value, tag=None):
        """Write point to InfluxDB.
        """
        point = {
            'measurement': cls.__measurement__,
            'tags': {cls.__tag_name__: tag if tag is not None else ''},
            'fields': {cls.__field_name__: cls.__field_type__(value)}}
        session.write_points([point])
