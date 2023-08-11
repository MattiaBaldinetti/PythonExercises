# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 10:56:04 2023

@author: UtentePC
"""

from math import *

"""
dati in ingresso 2 numeri, l'algoritmo stampa a video la loro somma
"""
def somma(a,b):
    return a+b


"""
dati in ingresso il valore del raggio di un cerchio, 
l'algoritmo calcola e stampa a video la circonferenza e l'area del cerchio
"""
def cerchio(r):
    circonferenza = 2*pi*r
    area = pi*r**2
    print ('La circonferenza è: ' + str(circonferenza))
    print('L\'area è: ' + str(area)) 
    return
    
    
"""
dati in ingresso 3 valori, l'algoritmo calcola e stampa la media
"""
def media(a,b,c):
    somma = a+b+c
    media = somma / 3
    return media


"""
dati in ingresso la base e l'altezza di un rettangolo, 
l'algoritmo calcola e stampa a video l'area e il perimetro
"""
def rettangolo(b,h):
    area = b*h
    perimetro = b*2+h*2
    return area , perimetro


"""
Scrivere uno script python che prende in input un numero float, 
ne calcola la radice cubica e la stampa a video
"""
def radice(r):
    radiceCubica = pow(r,1/3)
    return radiceCubica
    

"""
Scrivere uno script python che prende in input un nome di persona (nome) 
e il nome di un frutto (frutto) e stampa: "(nome) adora mangiare (frutto)
"""
def nomeFrutto(nome,frutto):
    print(nome + ' adora mangiare ' + frutto)
    return
    
 
"""
Scrivere uno script python che prende in input due float a e b e 
calcola e stampa c, corrispondente all'ipotenusa del triangolo rettangolo 
avente per cateti due lati di lunghezza a e b, rispettivamente
"""
def triangolo(a,b):
    ipotenusa = sqrt((a**2 + b**2))
    return ipotenusa


"""
Scrivere uno script python che prende in input tre float a, b, c, e 
calcola e stampa l'espressione: a^2 + ((b^3 * c^4) / 3a) - b + a*c
"""
def espressione(a,b,c):
    calcola = a**2 + ((b**3 * c**4)/3*a) - b + a*c
    return calcola


"""
Scrivere uno script python che prende in input tre float a, b, c, e 
calcola e stampa le due radici x dell'equazione: ax^2 + bx + c = 0
"""
def equazione(a,b,c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        x1 = (-b + sqrt(discriminant)) / (2*a)
        x2 = (-b - sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2*a)
        return x, x
    else:
        print ('None')  # No real roots


"""
Nel Kernel chiede in input all'utente due valori
"""
def prova():
    base = input('inserisci la base del rettangolo ')
    altezza = input('inserisci l\'altezza del rettangolo ')
    area = int(base)*int(altezza)
    print(area)
    
    
"""
somma numeri di una lista
"""
def sumList(numeri):
    somma = sum(numeri)
    print('La lunghezza della lista è', len(numeri))
    return somma

























