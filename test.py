#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from logger.client import VistualLogger
from random import randint

__author__ = 'nnedkov'


if __name__ == '__main__':
    v_logger = VistualLogger('vistual-logger-test')
    v_logger.annotate('And there was light...')

    for _ in range(10):
        value = randint(0, 10)
        v_logger.log(value)

    v_logger.annotate('Shutdown...')
