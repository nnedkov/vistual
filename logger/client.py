# -*- coding: utf-8 -*-

import logging
from logger.tms_data.database import VistualDB, init_db
from logger.tms_data.models import VistualVariable

__author__ = 'nnedkov'


logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s: %(message)s',)
logger = logging.getLogger('VistualLogger')
logger.setLevel(logging.DEBUG)


class VistualLogger(object):

    def __init__(self, name, db_host='127.0.0.1', db_port=8086,
                 db_user='influxdb', db_pass='admin', db_name='vistual',
                 gf_host='127.0.0.1', gf_port=3000,
                 gf_user='admin', gf_pass='admin', recreate_db=True):
        """Initializes the VistualLogger object.
        """
        init_db({'host': db_host,
                 'port': db_port,
                 'username': db_user,
                 'password': db_pass,
                 'database': db_name},
                recreate_db=recreate_db)
        # TODO: add annotation of intialization in Grafana
        logger.info(f'View dashboard under URL: http://{gf_host}:{gf_port}')

    def log(self, value, tag=''):
        session = VistualDB.get_session()
        logger.debug(f'Writing value `{value}` with tag `{tag}`')
        VistualVariable.write_point(session, value, tag=tag)

    def annotate(self, annotation_msg):
        # TODO: write annotation message to Grafana
        logger.debug(f'Writing annotation `{annotation_msg}`')
