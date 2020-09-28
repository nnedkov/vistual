# -*- coding: utf-8 -*-

import logging
import requests
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
        # TODO: fail if cannot establish connection with either InfluxDB or Grafana (or busy-wait with timeout?)
        init_db({'host': db_host,
                 'port': db_port,
                 'username': db_user,
                 'password': db_pass,
                 'database': db_name},
                recreate_db=recreate_db)
        # TODO: add annotation of intialization in Grafana?
        self._grafana_url = f'{gf_host}:{gf_port}'
        logger.info(f'View dashboard under URL: http://{self._grafana_url}/dashboard/script/vistual.js')

    def log(self, value, tag=''):
        session = VistualDB.get_session()
        logger.debug(f'Writing value `{value}` with tag `{tag}`')
        VistualVariable.write_point(session, value, tag=tag)

    def annotate(self, annotation_msg, tags=None):
        logger.debug(f'Adding annotation `{annotation_msg}` to Grafana')
        annotation = {
            'tags': ['vistual'] if tags is None else ['vistual', *tags],
            'text': annotation_msg
        }
        r = requests.post(f'http://admin:admin@{self._grafana_url}/api/annotations',
                          data=annotation)
        if r.status_code != 200:
            raise Exception('Could not add annotation due to invalid authentication')
