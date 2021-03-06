# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 06:54:25 2021

@author: Christian

Valutare inserimento tabella top
Inserire foto drink
Inserire capacità drink
"""

import sqlite3 as sql

conn = sql.connect('cocktails.db')

cur = conn.cursor()

def getId(table, name):
    query = 'SELECT id FROM {} WHERE name="{}"'
    cur.execute(query.format(table,name))
    
    return cur.fetchone()[0]

def insertCocktail(name,recipe,glass,time):
    id_glass = getId('glasses', glass)
    id_time = getId('time', time)
    
    query = """INSERT INTO cocktails (name, recipe, id_glass, id_time)
               VALUES ('{}',"{}",{},{})""".format(name,recipe,id_glass,id_time)
    
    cur.execute(query)

def insertIngredient(name, table):
    query = "INSERT INTO {} (name) VALUES ('{}')".format(table,name)
    
    cur.execute(query)

# insert data into tables which relate cocktails to other tables in case of an N-N relation
# elements may reffer to liquors, liquids and solid ingredients
def insertCoRel(name, elements, table, table_rel):
    id_cock = getId('cocktails', name)
    
    id_elements = []
    for x in elements:
        id_element = getId(table, x[0])
        id_elements.append((id_element,x[1]))
    
    for x in id_elements:
        query = 'INSERT INTO {} VALUES ("{}","{}","{}")'
        cur.execute(query.format(table_rel,id_cock,x[0],x[1]))

def insertCoLi(name,liquors):
    insertCoRel(name, liquors, "liquors", "co_li")
                
def insertCoInl(name,ingredients):
    insertCoRel(name, ingredients, "ingredients_liquid", "co_inl")        

def insertCoIns(name,ingredients):
    insertCoRel(name, ingredients, "ingredients_solid", "co_ins")    

def selectAllFrom(table):
    query = "SELECT * FROM {}".format(table)
    cur.execute(query)
    
    return cur.fetchall()
    
def printAllFrom(table):
    for record in selectAllFrom(table):
        print(record)        

"""
----------------------MAIN-------------------------
"""

# insertIngredient('Acqua', 'ingredients_liquid')
# insertIngredient('Zucchero bianco', 'ingredients_solid')
# insertIngredient('Angostura', 'liquors')
insertIngredient('Whiskey', 'liquors')

name = "Old fashioned"        
liquors = [('Whiskey', '45 ml'),
           ('Angostura', 'alcune gocce')]

liquids = [('Acqua', 'splash')]

ingredients = [('Zucchero bianco', 'una zolletta')]

recipe = """Saturare la zolletta di zucchero con le gocce di angostura e l'acqua in un bicchiere old fashioned.
Pestare fino a dissolvere lo zucchero.
Riempire il bicchiere con ghiaccio, versare il whiskey.
Mescolare dolcemente.
Guarnire con fetta o scorza di arancia e una ciliegia al maraschino."""

time = "Pre dinner"
glass = "Old fashioned"

insertCocktail(name, recipe, glass, time)
insertCoLi(name, liquors)
insertCoInl(name, liquids)

conn.commit()

conn.close()