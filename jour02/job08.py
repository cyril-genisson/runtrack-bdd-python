#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job08.py
@created: 30/01/2024

@project: 
@licence: GPLv3
"""
from dotenv import load_dotenv
import os
import mariadb
import pandas as pd
from random import randint, uniform

load_dotenv()


class Db:
    def __init__(self):
        self.__url = os.getenv('url')
        self.__user = os.getenv('user')
        self.__pw = os.getenv('pw')
        self.__port = int(os.getenv('port'))
        self.__database = os.getenv('db2')

    def __connect(self):
        base = mariadb.connect(
                host=self.__url,
                user=self.__user,
                password=self.__pw,
                port=self.__port,
                database=self.__database,
                autocommit=False
                )
        cursor = base.cursor()
        return base, cursor

    def query(self, req, modif=False):
        base, cursor = self.__connect()
        cursor.execute(req)
        base.commit()
        if modif is False:
            res = cursor.fetchall()
            return res
        cursor.close()
        base.close()


class Zoo(Db):
    def __init__(self):
        super().__init__()

    def get_box(self):
        req = "SELECT * FROM box"
        res = self.query(req)
        df = pd.DataFrame(res, columns=["Id", "Aera", "Capacity"])
        print(df)

    def get_animal(self, *argv):
        req = "SELECT a.id, a.name, a.breed, a.id_box, a.birth, a.country FROM animal AS a "
        req += "JOIN box AS b "
        req += f"WHERE b.id = a.id_box "
        for k in argv:
            if isinstance(argv[k], int):
                req += f"AND a.id_box = {argv[k]} "
        req += "ORDER BY a.id"
        res = self.query(req)
        df = pd.DataFrame(res, columns=['Id', 'Name', 'Breed', 'Box', 'Birth', 'Country'])
        print(df)
    
    def remove(self, table, id_t):
        req = f"DELETE FROM {table} WHERE id = {id_t}"
        res = self.query(req, modif=True)

    def add_t(self, table, **kwargs):
        if table == "animal":
            if "name" not in kwargs and "breed" not in kwargs:
                print("Le nom et la race de l'animal sont requis")
                return 1
        arg_k, arg_v = "", ""
        for key, value in kwargs.items():
            arg_k += f"{key},"
            arg_v += f"\'{value}\',"
        arg_k = arg_k[:-1]
        arg_v = arg_v[:-1]
        req = f"INSERT INTO {table}({arg_k}) VALUES ({arg_v})"
        res = self.query(req, modif=True)

    def update_t(self, table, id_t, **kwargs):
        argv = ""
        for key, value in kwargs.items():
            argv += f"{key}=\'{value}\', "
        argv = argv[:-2]
        req = f"UPDATE {table} SET {argv} WHERE id = {id_t}"
        res = self.query(req, modif=True)

    def count_aera(self):
        req = "SELECT SUM(aera) FROM box"
        res = self.query(req)

    def count_capacity(self):
        req = "SELECT SUM(capacity) FROM box"
        res = self.query(req)


class App(Zoo):
    def __init__(self):
        super().__init__()

    def menu_box(self):
        pass

    def menu_animal(self):
        pass

    def run(self):
        pass


if __name__ == '__main__':
    app = App()
    app.run()
