# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 03:32:57 2021

@author: Christian
"""

import sqlite3 as sql

def getDrinkByName(name):
    query = """SELECT c.name, c.recipe, g.name, t.name
               FROM cocktails AS c
               JOIN glasses AS g, time AS t
               ON c.id_glass=g.id AND c.id_time=t.id
               WHERE c.name='{}'""".format(name)
    cur.execute(query)
    
    return cur.fetchall()

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

def getDrinksByTimeOfDay(time_of_day):
    query = """SELECT DISTINCT c.name, c.recipe, g.name, t.name
               FROM cocktails AS c
               JOIN glasses AS g, time AS t, 
                    liquors as l, co_li as cl
               ON c.id_glass=g.id AND c.id_time=t.id AND
                  c.id=cl.id_cocktail AND l.id=cl.id_liquor
               WHERE t.name='Any time' OR t.name='{}'""".format(time_of_day)
    cur.execute(query)
    
    return cur.fetchall()

def printResults(results):
    for record in results:
        print(record)
        print()
    
def showDrinks():
    query = """SELECT c.name, c.recipe, g.name, t.name
               FROM cocktails AS c
               JOIN glasses AS g, time AS t
               ON c.id_glass=g.id AND c.id_time=t.id"""
    cur.execute(query)
    records = cur.fetchall()
    printResults(records)

def showLiquors():
    query = "SELECT name FROM liquors"
    cur.execute(query)
    liquors = cur.fetchall()
    printResults(liquors)

def showByName():
    name = input("Drink name: ")
    drink = getDrinkByName(name)
    printResults(drink)

def showByLiquor():
    name = input("Liquor name: ")
    drinks = getDrinksByLiquor(name)
    printResults(drinks)

def showByTimeOfDay():
    time_of_day = input("Time of day: ")
    drinks = getDrinksByTimeOfDay(time_of_day)
    printResults(drinks)

# ////////// MAIN /////////////

conn = sql.connect('cocktails.db')
cur = conn.cursor()

cmd = 1
while(cmd):
    print("Menu:")
    print("[1] Mostra drink")
    print("[2] Mostra liquori")
    print("[3] Cerca drink per nome")
    print("[4] Cerca drink per liquore")
    print("[5] Cerca drink per momento del giorno")
    print("[0] Esci")
    cmd = int(input("Scelta: "))

    if cmd==1:
        showDrinks()
    elif cmd==2:
        showLiquors()
    elif cmd==3:
        showByName()
    elif cmd==4:
        showByLiquor()
    elif cmd==5:
        showByTimeOfDay()

conn.close()









