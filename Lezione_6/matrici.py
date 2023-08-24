# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 10:27:42 2020

@author: Studente

Scrivere una funzione che verifica se una lista
di liste può rappresentare una matrice

HINTS: verificare che le liste hanno tutte la
       stessa lunghezza e che tutti gli elementi siano
       dei numeri
"""

def check_matrix(m):
    ''' La funzione ritorna True o False '''
    print('Controllo matrice')
    for riga in m:
        if len(riga) != len(m[0]):
            return False
        for valore in riga:
            if type(valore) != int and type(valore) != float:
                return False
    return True


def get_row(m, n_riga):
    ''' Funzione che ritorna la riga "n_riga" della matrice '''
    return m[n_riga]


def get_column(m, n_colonna):
    ''' Funzione che ritorna la colonna "n_colonna" di m '''
    colonna = []
    for i in range(len(m)):
        colonna.append(m[i][n_colonna])
    return colonna
# return [riga[n_colonna] for riga in m]


def somma_matrici(a, b):
    ''' Funzione che ritorna una nuova matrice in cui gli
        elementi sono dati dalla somma degli elementi di
        a e b
    '''
    #if not all((check_matrix(a), check_matrix(b), len(a) == len(b), len(a[0]) == len(b[0]))):
    if not (check_matrix(a) and check_matrix(b) and len(a) == len(b) and len(a[0]) == len(b[0])): 
        return None
    c = [riga.copy() for riga in a]
    for n_riga, riga in enumerate(b):
        for n_colonna, colonna in enumerate(riga):
            c[n_riga][n_colonna] += colonna
    return c
        
        #c[n_riga] = [c[n_riga][n_colonna] + riga[n_colonna] for n_colonna in range(len(b[0]))]
        

        
# 1 4 7 9
# 5 8 9 0
# 4 8 4 3
# 5 6 7 9
# 
# [[1,4,7,9], [5,8,9,0], [4,8,4,3], [5,6,7,9]]