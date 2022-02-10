# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 03:32:57 2021

@author: Christian

fomrato cocktail
id, nome, ricetta, id glass, id time
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

def getFullDrinkInfo(name):
    cocktail = getDrinkByName(name)
    liquors = getLiquorsByDrink(name)
    liquids = getLiquidsByDrink(name)
    solids = getSolidsByDrink(name)
    
    return cocktail, [*liquors, *liquids, *solids]
    
def getLiquorsByDrink(drink):
    query = """SELECT DISTINCT l.name, cl.quantita
               FROM liquors AS l
               JOIN cocktails AS c, co_li AS cl
               ON l.id=cl.id_liquor AND c.id=cl.id_cocktail
               WHERE c.name='{}'""".format(drink)
    cur.execute(query)
    
    return cur.fetchall()

def getLiquidsByDrink(drink):
    query = """SELECT DISTINCT l.name, cl.quantita
               FROM ingredients_liquid AS l
               JOIN cocktails AS c, co_inl AS cl
               ON l.id=cl.id_ingredient AND c.id=cl.id_cocktail
               WHERE c.name='{}'""".format(drink)
    cur.execute(query)
    
    return cur.fetchall()

def getSolidsByDrink(drink):
    query = """SELECT DISTINCT s.name, cs.quantita
               FROM ingredients_solid AS s
               JOIN cocktails AS c, co_ins AS cs
               ON s.id=cs.id_ingredient AND c.id=cs.id_cocktail
               WHERE c.name='{}'""".format(drink)
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

def showRicetta():
    print("\n===================")
    drink = input("Nome drink: ")
    cocktail, ingredients = getFullDrinkInfo(drink)   
    cocktail = cocktail[0]
  
    ricetta = cocktail[1]
    glass = cocktail[2]
    time = cocktail[3]
    
    # print("Nome: {}".format(drink))
    print("\nRicetta:\n{}".format(ricetta))
    
    print("\nIngredienti:")
    for x in ingredients:
        print("- {}: {}".format(x[0],x[1]))
    
    print("\nBicchiere: {}".format(glass))
    print("\nPeriodo: {}".format(time))
    
    print("\n===================")
    

# ////////// MAIN /////////////

conn = sql.connect('cocktails.db')
cur = conn.cursor()

cmd = 1
while(cmd):
    print("\nMenu:")
    print("[1] Mostra drink")
    print("[2] Mostra ricetta drink")
    print("[3] Mostra liquori")
    print("[4] Cerca drink per nome")
    print("[5] Cerca drink per liquore")
    print("[6] Cerca drink per momento del giorno")
    print("[0] Esci")
    try:
        cmd = int(input("Scelta: "))
    except:
        cmd = -1
        print("Inserimento non consentito oh")
        
    if cmd==1:
        showDrinks()
    elif cmd==2:
        showRicetta()
    elif cmd==3:
        showLiquors()
    elif cmd==4:
        showByName()
    elif cmd==7:
        showByLiquor()
    elif cmd==6:
        showByTimeOfDay()

conn.close()

