# -*- coding: utf-8 -*-

import logging
from logger.tms_data.database import VistualDB, init_db
from logger.tms_data.models import VistualVariable

__author__ = 'nnedkov'


logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s: %(message)s',)
logger = logging.getLogger('VistualLogger')
logger.setLevel(logging.INFO)


class VistualLogger(object):

    def __init__(self, name, db_host='127.0.0.1', db_port=8086,
                 db_user='influxdb', db_pass='admin', db_name='vistual',
                 grafana_host='127.0.0.1', grafana_port=3000,
                 grafana_user='admin', grafana_pass='admin', recreate_db=True):
        """ Initializes the VistualLogger object.

        :param name:
        :param db_host:
        :param db_port:
        :param db_user:
        :param db_pass:
        :param db_name:
        :param grafana_host:
        :param grafana_port:
        :param grafana_user:
        :param grafana_pass:
        :param recreate_db:
        """
        init_db({'host': db_host,
                 'port': db_port,
                 'username': db_user,
                 'password': db_pass,
                 'database': db_name},
                recreate_db=recreate_db)
        # TODO: add annotation of intialization in Grafana
        logger.info(f'View visualization under URL: http://{grafana_host}:{grafana_port}')

    def log(self, value, tag=''):
        session = VistualDB.get_session()
        # TODO: write point to VistualDB

    def annotate(self, annotation_message):
        # TODO: write annotation message to Grafana
        pass
