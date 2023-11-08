# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 14:59:58 2023

@author: matti
"""

'''
Es 3: 4 punti
Si consideri l'ordine alfabetico delle 21 lettere dell'alfabeto italiano:
A – B – C – D – E – F – G – H – I – L – M – N – O – P – Q – R – S – T – U – V – Z
definiamo valore di una lettera la posizione che occupa in quest'ordine a
partire da 1 (ad esempio il valore di A e' 1 mentre il valore di Z e' 21). 
La funzione  es20(stringa1) presa la stringa stringa1 contenente parole
sull'alfabeto italiano separate da uno spazio, restituisce la stringa 
che si ottine sostituendo a ciasuna parola presente in  stringa1 
la stringa numerica che si ottiene sommando  il valore delle lettere che
compongono la parola.
Non si distingue tra lettere maiuscole e minuscole.
Ad esempio con stringa1='Angelo Monti Andrea Sterbini e Angelo Spognardi'
la funzione restituira' 
la stringa '48 63 39 88 5 48 93'
'''

def es20(stringa1):   
    dizio = {'a':1,'b':2,'c':3,'d':4,
             'e':5,'f':6,'g':7,'h':8,
             'i':9,'l':10,'m':11,'n':12,
             'o':13,'p':14,'q':15,'r':16,
             's':17,'t':18,'u':19,'v':20,'z':21
             }
    #lista con parole separate e minuscole
    lista_parole_separate = stringa1.lower().split()
    somma = 0
    stringa = ''
    for parola in lista_parole_separate:
        for lettera in parola:
            if lettera in dizio:
                somma = somma + dizio[lettera]
        stringa = stringa + ' ' + str(somma)
        somma = 0
    return stringa

# Esempio di esecuzione
stringa1 = 'Angelo Monti Andrea Sterbini e Angelo Spognardi'
print(es20(stringa1))













































