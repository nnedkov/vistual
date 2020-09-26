# -*- coding: utf-8 -*-

from os.path import isfile
from time import gmtime, mktime
from datetime import datetime, time
from storage.app.aux.conf_parser import read_conf

__author__ = 'nnedkov'


def read_settings(conf_path):
    if not isfile(conf_path):
        raise IOError('{f} is not a conf file'.format(f=conf_path))

    settings = read_conf(conf_path)

    return settings


def get_secs_since_epoch():
    # now (in secs since epoch)
    now = mktime(gmtime())

    return now


def get_secs_since_epoch_interval(time_window):
    # now (in secs since epoch)
    now = get_secs_since_epoch()
    # now - time_window (in secs since epoch)
    start_time = mktime((datetime.fromtimestamp(now) - time_window).timetuple())

    return start_time, now


def convert_str_to_time(time_str):
    return time(*[int(i) for i in time_str.split(':')])

