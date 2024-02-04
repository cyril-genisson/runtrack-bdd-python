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
import pandas as pd
from random import randint, uniform

load_dotenv()


class Db:
    def __init__(self):
        self.__url = os.getenv('url')
        self.__user = os.getenv('user')
        self.__pw = os.getenv('pw')
        self.__port = int(os.getenv('port'))
        self.__database = os.getenv('db1')

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


class Enterprise(Db):
    def __init__(self):
        super().__init__()

    def add_service(self, nom):
        req = f"INSERT INTO service(nom) VALUES (\'{nom}\')"
        res = self.query(req, modif=True)

    def get_services(self):
        req = "SELECT * FROM service"
        res = self.query(req)
        df = pd.DataFrame(res, columns=["Id", "Service"])
        print(df)

    def update_service(self, id_serv, name):
        req = f"UPDATE service SET nom = \'{name}\' WHERE id = {id_serv}"
        res = self.query(req, modif=True)

    def rm_service(self, id_serv):
        req = f"DELETE FROM service WHERE id = {id_serv}"
        res = self.query(req, modif=True)

    def add_employe(self, nom, prenom, **kwargs):
        arg_k, arg_v = "nom,prenom,", f"\'{nom}\',\'{prenom}\',"
        for key, value in kwargs.items():
            arg_k += f"{key},"
            arg_v += f"\'{value}\',"
        arg_k = arg_k[:-1]
        arg_v = arg_v[:-1]
        req = f"INSERT INTO employe({arg_k}) VALUES ({arg_v})"
        res = self.query(req, modif=True)

    def update_employe(self, id_emp, **kwargs):
        argv = ""
        for key, value in kwargs.items():
            argv += f"{key}=\'{value}\', "
        argv = argv[:-2]
        req = f"UPDATE employe SET {argv} WHERE id = {id_emp}"
        res = self.query(req, modif=True)

    def remove_employe(self, id_emp):
        req = f"DELETE FROM employe WHERE id = {id_emp}"
        res = self.query(req, modif=True)

    def get_employes(self, min_salaire=0):
        req = "SELECT e.id, e.nom, e.prenom, e.salaire, s.nom AS 'Service', e.id_service FROM employe AS e "
        req += "JOIN service AS s "
        req += f"WHERE s.id = e.id_service AND e.salaire >= {min_salaire} "
        req += "ORDER BY e.id"
        res = self.query(req)
        df = pd.DataFrame(res, columns=['Id', 'Nom', 'Prénom', 'Salaire', 'Service', 'Id Service'])
        print(df)


if __name__ == '__main__':
    ent = Enterprise()
    for k in range(1,6):
        ent.add_service(nom=f'service{k}')
    for k in range(1, 21):
        ent.add_employe(nom=f'Nom{k}', prenom=f'Prenom{k}', salaire=f'{uniform(900,10000)}', id_service=f'{randint(1,6)}')
    ent.get_services()
    print(f"\n{'*' * 60}\n")
    ent.get_employes()
    print(f"\n{'*' * 60}\n") 
    ent.get_employes(min_salaire=5000)
    ent.rm_service(2)
    print(f"\n{'*' * 60}\n")
    ent.get_employes()

