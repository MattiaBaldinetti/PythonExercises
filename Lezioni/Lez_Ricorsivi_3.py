# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 14:56:10 2023

@author: matti
"""


"""
Scrivere una funzione ricorsiva che
prende una lista di interi e stampa
soltanto gli elementi della lista
che sono multipli di 3
"""

def stampa_3(lista):
    n = lista[0]
    if n % 3 == 0:
            print(n)
    if len(lista) > 1:
        stampa_3(lista[1:])
        
 
"""
Scrivere una funzione ricorsiva che a partire
da una lista di interi, costruisce una nuova
lista con soltanto gli elementi multipli di 3
"""

def ric(lista):
    n = lista[0]
    if(n % 3 == 0):
        nuova_lista = [n]
    else:
        nuova_lista = []
        
    if len(lista) > 1:
        coda = ric(lista[1:])
    else:
        coda = []
    return nuova_lista + coda
        

def crea_3_iter(lista):
    return [x for x in lista if x % 3 == 0]