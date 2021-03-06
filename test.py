#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from logger.client import VistualLogger
from random import randint
from time import sleep

__author__ = 'nnedkov'


if __name__ == '__main__':
    v_logger = VistualLogger('vistual-logger-test', recreate_db=False)
    v_logger.annotate('And there was light...')

    for _ in range(10):
        value = randint(0, 10)
        v_logger.log(value, tag='test0')
        sleep(1)

    v_logger.annotate('Shutdown...')
