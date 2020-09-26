# -*- coding: utf-8 -*-

from influxdb import InfluxDBClient
from .models import VistualVariable

__author__ = 'nnedkov'


class VistualDB(object):

    SESSION = None
    NAME = None

    @staticmethod
    def init(settings):
        """Initializes InfluxDB client.
        """
        if VistualDB.NAME is not None and VistualDB.SESSION is not None:
            raise Exception('The VistualDB object has already been initialized')

        VistualDB.NAME = settings['database']
        VistualDB.SESSION = InfluxDBClient(**settings)

    @staticmethod
    def drop():
        """Drops InfluxDB database.
        """
        session = VistualDB.get_session()
        name = VistualDB.get_name()

        if VistualDB.database_exists():
            session.drop_database(name)

    @staticmethod
    def recreate():
        """Recreates InfluxDB database.
        """
        # drop database
        session = VistualDB.get_session()
        VistualDB.drop()

        # create database
        name = VistualDB.get_name()
        session.create_database(name)

        # create series
        VistualVariable.create_series(session)

    @staticmethod
    def database_exists():
        """Returns True if the database exists, otherwise False.
        """
        session = VistualDB.get_session()
        name = VistualDB.get_name()

        return any([db['name'] == name for db in session.get_list_database()])

    @staticmethod
    def get_session():
        """Returns InfluxDB HTTP session.
        """
        session = VistualDB.SESSION
        if session is None:
            raise Exception('The VistualDB object has not been initialized')

        return session

    @staticmethod
    def get_name():
        """Returns database name.
        """
        name = VistualDB.NAME
        if name is None:
            raise Exception('The VistualDB object has not been initialized')

        return name

    @staticmethod
    def close():
        """Closes InfluxDB HTTP session.
        """
        session = VistualDB.get_session()
        session.close()

    @staticmethod
    def is_healthy():
        """Checks connectivity to InfluxDB.
        """
        session = VistualDB.get_session()
        return session.ping() is not None


def init_db(settings, recreate_db=False):
    VistualDB.init(settings)

    if recreate_db:
        VistualDB.recreate()
