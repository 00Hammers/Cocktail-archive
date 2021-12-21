# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 06:54:25 2021

@author: Christian
"""


import sqlite3 as sql

# Using the connect() method, sqlite3 returns a Connection object.

conn = sql.connect('cocktails.db')

cur = conn.cursor()

# ingredienti = ['Pre dinner', 'After dinner', 'Any time']

# for x in ingredienti:
#     query = """INSERT INTO time (name)
#                 VALUES ('""" + x + """')"""
#     cur.execute(query)

# conn.commit()

def insertCocktail(name,recipe,glass,time):
    query = 'SELECT id FROM {} WHERE name="{}"'
    
    cur.execute(query.format('glasses',glass))
    id_glass = cur.fetchone()[0]
    
    cur.execute(query.format('time',time))
    id_time = cur.fetchone()[0]
    
    query = """INSERT INTO cocktails (name, recipe, id_glass, id_time)
               VALUES ('{}',"{}",{},{})"""
    
    cur.execute(query.format(name,recipe,id_glass,id_time))

conn.commit()

# query = "SELECT * FROM time"
# cur.execute(query)

# for record in cur.fetchall():
#     print(record)

# conn.close()