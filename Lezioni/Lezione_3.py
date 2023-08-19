# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 14:57:45 2023

@author: matti
"""


"""
Scrivere una funzione che prende un intero n in input
e stampa a video n righe in cui la riga i-esima ha
esattamente i uni (1)

es: foo(4) stampa
1
11
111
1111

"""

def foo1(n):
    for i in range(1,n+1):
        print('1'*i)
        
def foo2(n):
    s = '1'
    for i in range(n):
        print(s)
        s = s + '1'
        
def foo3(n):
    counter = 1
    while counter <= n:
        print('1'*counter)
        counter += 1
        
def foo4(n):
    s = '1'
    while n>0:
        print(s)
        s = s+'1'
        n-=1
        
def foo5(n):
    for elemento in ['1'*i for i in range(1,n+1)]:
        print (elemento)

def foo6(n):
    if n == 1:
        print('1')
    else:
        foo6(n-1)
        print('1'*n)
        
        
        
'''        
############################################
'''

def somma_for(sequenza):
    accumulatore = 0
    for elemento in sequenza:
        accumulatore += elemento
    return accumulatore
    
''' somma solo gli elementi pari della sequenza'''    
def somma_pari(sequenza):
    accumulatore = 0
    for elemento in sequenza:
        if elemento % 2 == 0:
            accumulatore += elemento
    return accumulatore

''' ritorna il numero di caratteri a della sequenza '''
def conta_a(sequenza):
    count = 0
    for elemento in sequenza:
        if elemento == 'a':
            count += 1
    return count

''' somma solo gli elementi che occupano
    una posizione pari nella sequenza '''
def somma_indici_pari(sequenza):
    accumulatore = 0
    for indice in sequenza:
        if indice% 2 == 0:
            accumulatore += indice
    return accumulatore

def somma_indici_pari2(sequenza):
    accumulatore = 0
    for indice, elemento in enumerate(sequenza):
        if indice%2 == 0:
            accumulatore += elemento
    return accumulatore

if __name__ == '__main__':
    sequenza = [5,6,7,8,9]
    
    for elemento in sequenza:
        print(elemento)
        a = elemento **2 /3
        b = elemento /5
        print(a * b)
        
    
    sequenza = ['mela', 'pera', 'albicocca', 'mango']
    
    for elemento in sequenza:
        print(elemento)
        print(len(elemento))
        print(elemento.split('a'))
    
    stringa = '0.5434534,5345331,9789695,132322,688785,843,66363563,7e-6'
    
    for elemento in stringa.split(','):
        print(elemento)
        print(len(elemento))
        print(float(elemento)**2)
        
    sequenza = [54,2343,767,34,65,24576,454]
    accumulatore = 0
    for elemento in sequenza:
        accumulatore += elemento
    print(accumulatore)
    
    
