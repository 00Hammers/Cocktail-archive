# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 03:32:57 2021

@author: Christian
"""

import sqlite3 as sql

conn = sql.connect('cocktails.db')
cur = conn.cursor()

def getDrinkByName(name):
    query = """SELECT c.name, c.recipe, g.name, t.name
               FROM cocktails AS c
               JOIN glasses AS g, time AS t
               ON c.id_glass=g.id AND c.id_time=t.id
               WHERE c.name='{}'""".format(name)
    cur.execute(query)
    
    return cur.fetchone()

def getDrinksByLiquor(liquor):
    query = """SELECT c.name, c.recipe, g.name, t.name
               FROM cocktails AS c
               JOIN glasses AS g, time AS t, 
                    liquors as l, co_li as cl
               ON c.id_glass=g.id AND c.id_time=t.id AND
                  c.id=cl.id_cocktail AND l.id=cl.id_liquor
               WHERE l.name='{}'""".format(liquor)
    cur.execute(query)
    
    return cur.fetchall()


drink = getDrinkByName("Negroni")
drinks = getDrinksByLiquor("Gin")

for x in drinks:
    print(x)
    print()

conn.close()