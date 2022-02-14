# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 03:32:57 2021

@author: Christian

formato cocktail
id, nome, ricetta, id glass, id time

gestire ordine ingredienti nella visualizzazione (base, liquidi, soliti)
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

def getIngredientsByDrink(drink, table):
    id_i = "id_ingredient"
    if(table == "liquors"):
        co_in = "co_li"
        id_i = "id_liquor"
    elif(table == "ingredients_liquid"):
        co_in = "co_inl"
    elif(table == "ingredients_solid"):
        co_in = "co_ins"

    query = f"""SELECT DISTINCT i.name, ci.quantita
                FROM {table} AS i
                JOIN cocktails AS c, {co_in} AS ci
                ON i.id=ci.{id_i} AND c.id=ci.id_cocktail
                WHERE c.name='{drink}'"""
    cur.execute(query)
    
    return cur.fetchall()

def getLiquorsByDrink(drink):
    return getIngredientsByDrink(drink, "liquors")

def getLiquidsByDrink(drink):
    return getIngredientsByDrink(drink, "ingredients_liquid")

def getSolidsByDrink(drink):
    return getIngredientsByDrink(drink, "ingredients_solid")

def printResults(results):
    for record in results:
        print(record)
        print()
    
def printNames(records, title):
    print(f"\n{title}:")
    for record in records:
        print(f" - {record[0]}")
    
def getNames(table):
    query = f"SELECT name FROM {table}"
    cur.execute(query)
    records = cur.fetchall()
    
    return records
    
def showDrinks():
    records = getNames('cocktails')
    
    printNames(records, 'Drink')

def showLiquors():
    records = getNames('liquors')
    
    printNames(records, 'Liquori')

def showByLiquor():
    name = input("Liquor name: ")
    drinks = getDrinksByLiquor(name)
    
    printNames(drinks, 'Drink')

def showByTimeOfDay():
    time_of_day = input("Time of day: ")
    drinks = getDrinksByTimeOfDay(time_of_day)
    
    printNames(drinks, 'Drink')

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
    print("[4] Cerca drink per liquore")
    print("[5] Cerca drink per momento del giorno")
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
        showByLiquor()
    elif cmd==5:
        showByTimeOfDay()

conn.close()

