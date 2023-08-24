# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 17:51:23 2020

@author: Studente
"""

def verifica_matrice(m):
    ''' restituisce True se m può essere considerata una
        matrice
    '''
    for riga in m:
        if len(riga) != len(m[0]):
            return False
#        if not all([type(el)==int or type(el)==float for el in riga]):
        for el in riga:
#            if type(el)!=int and type(el)!=float:
            if not isinstance(el, (int, float)):
                return False
    return True


def prendi_riga(i, m):
    ''' restituisce la riga i-esima della matrice m '''
    return m[i]


def prendi_colonna(j, m):
    ''' restituisce la colonna j-esima della matrice m '''
    return [riga[j] for riga in m]
        

def verifica_matrice_quadrata(m):
    ''' restituisce True se la matrice è quadrata, ovvero
        ha tante righe quante colonne '''
    return verifica_matrice(m) and len(m[0]) == len(m)


def prendi_diagonale(m, direzione=1):
    ''' restituisce la diagonale se la matrice è quadrata
        genera errore se la matrice non è quadrata '''
    if not verifica_matrice_quadrata(m):
        raise ValueError ('la matrice passata non è quadrata')
    diagonale = [m[i][i] for i in range(len(m))]
    return diagonale
