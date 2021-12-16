# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 22:18:02 2021

@author: Christian

drink
    - nome
    - ingredienti
    - bicchiere
    - periodo
    - preparazione
    - decorazione
"""
from cocktail import Cocktail

def stampaCocktails(cocktails):
    for item in cocktails:
        item.stampaCocktail()

fp = open("archivio.txt","r")
cocktails = []
for line in fp:
    tmp = line.split(",")
    tmp[1] = tmp[1].split("-")
    cocktails.append(Cocktail(tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5]))

stampaCocktails(cocktails)



