# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 06:54:25 2021

@author: Christian
"""


import sqlite3 as sql

# Using the connect() method, sqlite3 returns a Connection object.

conn = sql.connect('cocktails.db')

cur = conn.cursor()

glasses = ['Collins','Highball','Old fashioned','Double old fashioned',
            'Shot','Cocktail','Champagne coupe', 'Champagne flute',
            'Snifter','Wine','Hurricane','Glencairn']

for glass in glasses:
    query = """INSERT INTO glasses (name)
                VALUES ('""" + glass + """')"""
    cur.execute(query)

conn.commit()

query = "SELECT * FROM glasses"
cur.execute(query)

conn.close()