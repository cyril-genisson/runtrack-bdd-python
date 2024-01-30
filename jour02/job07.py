#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job07.py
@created: 30/01/2024

@project: 
@licence: GPLv3
"""
from dotenv import load_dotenv
import os
import mariadb

load_dotenv()

config = [os.getenv('url'),
          os.getenv('user'),
          os.getenv('pw'),
          int(os.getenv('port')),
          os.getenv('db1')]


class Enterprise:
    def __init__(self):
        self.__db = None
        self.__cursor = None

    def __connect(self):
        self.__db = mariadb.connect(host=config[0], user=config[1], password=config[2],
                               port=config[3], database=config[4], autocommit=True)
        self.__cursor = self.__db.cursor()

    def __close(self):
        self.__cursor.close()
        self.__db.close()
    
    def __describe_table(self, table):
        self.__cursor.execute(f"DESCRIBE {table};")
        res, fields = self.__cursor.fetchall(), []
        for k in res:
            fields.append(k[0])
        return fields


    def get_table(self, table):
        self.__connect()
        self.__cursor.execute(f"SELECT * FROM {table}")
        res = self.__cursor.fetchall()
        for k in res:
            print(k)
        self.__close()

    def add_service(self, name):
        self.__connect()
        self.__cursor.execute(f"INSERT INTO service(nom) VALUES ({nom});")
        self.__close()

    def rm_service(self, **argv):
        self.__connect()
        self.__close()

    def add_employe(self, **argv):
        self.__connect()
        self.__close()

    def update_service(self, id_service, nom):
        self.__connect()
        self.__close()

    def update_employe(self, **argv):
        self.__connect()
        self.__close()

    def remove_employe(self, **argv):
        self.__connect()
        self.__close()

    def get_employes(self):
        self.__connect()
        self.__cursor.execute("SELECT * FROM employe")
        res = self.__cursor.fetchall()
        for k in res:
            print(k)
        self.__close()


if __name__ == '__main__':
    soc1 = Enterprise()
    soc1.get_table("service")
    soc1.get_table("employe")
