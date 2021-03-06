# coding: utf-8

from __future__ import (
    print_function,
    unicode_literals,
    absolute_import
)

import sqlite3


class DatabaseGateway(object):
    """
    A gateway (http://martinfowler.com/eaaCatalog/gateway.html)
    to a database.
    """

    db_api = sqlite3

    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = DatabaseGateway.connect(self.db_name)
        self._cursor = None

    def execute(self, statement, *args):
        with self.connection:
            self.cursor.execute(statement, *args)

    def fetchone(self):
        return self.cursor.fetchone()

    @property
    def cursor(self):
        if self._cursor is None:
            self._cursor = self.connection.cursor()
        return self._cursor

    @classmethod
    def connect(cls, db_name):
        return cls.db_api.connect(db_name)
