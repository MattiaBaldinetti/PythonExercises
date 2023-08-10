# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 09:15:37 2023

@author: matti
"""


"""
Scrivere una funzione che riceve tre numeri interi g, m, a (si ipotizza che 
a sia sempre un numero dispari per evitare anni bisestili) e restituisce True o 
False a seconda se i tre numeri formano una data valida nel formato "g/m/a". 
Es: 30/2/2017 False, 1/1/1111 True.
"""
def Calendario(g,m,a):
    if (m >= 13):
        print("Mese non valido")
    else:
        if(m == 2):
            if(g <= 28):
                return True 
            else:
                return False
        elif (m == 1) or (m == 3) or (m == 5) or (m == 7) or (m == 10) or (m == 12):
            if(g <= 31):
                return True
            else:
                return False
        elif (m == 4) or (m == 6) or (m == 9) or (m == 11):
            if(g <= 30):
                return True
            else:
                return False

#print(Calendario(21,3,2021))

"""
Scrivere una funzione che prende una lista di interi e restituisce la 
somma di tutti i numeri pari meno la somma di tutti i numeri dispari che 
la compongono.
"""

def operazioneLista(lista):
    somma = 0
    sottrai = 0
    for i in range (len(lista)):
        if ((lista[i]%2 == 0)) :
            somma += lista[i]
        else:
            sottrai += lista[i]
    risultato = somma - sottrai
    return risultato 

#print(operazioneLista([1,2,3,4,5,6,7]))


"""
Scrivere una funzione che prende in input una stringa di parole 
separate da spazi e restituisce una lista con le lunghezze 
delle parole della stringa.
"""

def listaParole(stringa):
    #divido la stringa ogni volta che trova uno spazio
    stringa_nuova = stringa.split(' ') 
    nuova_lista = []
    for i in range(len(stringa_nuova)):
        #aggiunge alla nuova lista la lungh di ogni singola parola
        nuova_lista.append(len(stringa_nuova[i])) 
    return nuova_lista

#print(listaParole(stringa = "ciao io mi chiamo marco"))


"""
Scrivere una funzione che verifica se una lista è ordinata in 
modo crescente (<=) (supponiamo che la lista contenga oggetti 
ordinabili).
"""
def listaOrdinata(lista):
    #utilizzando il metodo sorted
    ordinata = sorted(lista)
    return ordinata

#print(listaOrdinata(lista = [34,466,3,23,18,66]))

# usando un ciclo si può scegliere tra i vari algortimi di ordinamento


"""
Scrivere una funzione che prende in input una lista di interi e ritorna 
la lista con i complementi a 10 degli interi della lista in input.
"""
def complementi(lista):
    nuova_lista = []
    for i in range (len(lista)):
        nuova_lista.append(str(lista[i]))
    risultato = []
    for i in range(len(nuova_lista)):
        lunghezza = len(nuova_lista[i])
        risultato.append(10**lunghezza - int(nuova_lista[i])) 
    return risultato

#print(complementi(lista = [34,45566,343,232,5,666]))






































