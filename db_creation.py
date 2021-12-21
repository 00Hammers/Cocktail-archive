# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 06:54:25 2021

@author: Christian
"""

import sqlite3 as sql

# Using the connect() method, sqlite3 returns a Connection object.

conn = sql.connect('cocktails.db')

cur = conn.cursor()

def insertCocktail(name,recipe,glass,time):
    query = 'SELECT id FROM {} WHERE name="{}"'
    
    cur.execute(query.format('glasses',glass))
    id_glass = cur.fetchone()[0]
    
    cur.execute(query.format('time',time))
    id_time = cur.fetchone()[0]
    
    query = """INSERT INTO cocktails (name, recipe, id_glass, id_time)
               VALUES ('{}',"{}",{},{})""".format(name,recipe,id_glass,id_time)
    
    cur.execute(query)

def insertCoLi(name,liquors):
    query = "SELECT id FROM {} WHERE name='{}'"
    cur.execute(query.format('cocktails', name))
    id_cock = cur.fetchone()[0]
    
    id_liquors = []
    for x in liquors:
        cur.execute(query.format('liquors', x[0]))
        id_liquor = cur.fetchone()[0]
        id_liquors.append((id_liquor,x[1]))
    
    for x in id_liquors:
        query = 'INSERT INTO co_li VALUES ("{}","{}","{}")'
        cur.execute(query.format(id_cock,x[0],x[1]))
        
liquors = [('Vermuth rosso', '30 ml'),
           ('Campari', '30 ml'),
           ('Gin', '30 ml')]

insertCoLi('Negroni', liquors)

conn.commit()

# query = "SELECT * FROM cocktails"
# cur.execute(query)

# for record in cur.fetchall():
#     print(record)

conn.close()