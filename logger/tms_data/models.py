# -*- coding: utf-8 -*-

from .models_base import MeasurementBase

__author__ = 'nnedkov'


class VistualVariable(MeasurementBase):
    __measurement__ = 'env_intelligence'
    __fields__ = ['value']
    __fields_type__ = int
    __tags__ = ['variable']

    @classmethod
    def write_point(cls, session, value, tags, start_time, end_time):
        # TODO: write point to InfluxDB
        pass
