#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job06.py
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
          os.getenv('db')]

mydb = mariadb.connect(host=config[0],
                       user=config[1],
                       password=config[2],
                       port=config[3],
                       database=config[4]
                       )
cursor = mydb.cursor()
cursor.execute("SELECT SUM(capacite) FROM salle")
res = cursor.fetchall()[0][0]
print(f"La capacité de toutes les salles est de: {res}")
cursor.close()
mydb.close()

