# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 22:31:59 2021

@author: Christian
"""

class Cocktail:
    nome = ""
    ingredienti = []
    bicchiere = ""
    periodo = []
    preparazione = ""
    decorazione = ""
    
    def __init__(self, nome: str, ingredienti, bicchiere: str, periodo: str, preparazione: str, decorazione: str):
        self.nome = nome
        self.ingredienti = ingredienti
        self.bicchiere = bicchiere
        self.periodo = periodo
        self.preparazione = preparazione
        self.decorazione = decorazione
    
    def stampaCocktail(self):
        print(self.nome)
        print("Ingredienti:")
        for item in self.ingredienti:
            print("  - ", item)
        print("Bicchiere: ", self.bicchiere)
        print("Periodo: ", self.periodo)
        print("Preparazione: \n", self.preparazione)
        print("Decorazione: ", self.decorazione)