# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 20:02:47 2023

@author: UtentePC
"""

"""
Scrivere una funzione chiave che permetta di
ordinare una lista di stringhe in base alla lettera
finale delle stringhe, in caso di parità, la lunghezza,
in caso di parità, lessicograficamente
es: ['cane','gatto','canarino','topo', 'lupo']
-> ['cane','lupo','topo','gatto', 'canarino']
"""
def chiave (s):
    return s[-1], len(s), s
    
#lista_stringhe = ['cane','gatto','canarino','topo', 'lupo']
#print(sorted(lista_stringhe, key=chiave))


"""
Scrivere una key function che ordina una lista di
interi in base al resto della divisione per 11 e
in caso di parità, in base resto della divisione per 5, in caso di parità, in base al valore dell'intero
[23, 19, 90, 30] -> [23, 90, 30, 19]
"""
def ordina_lista(s):
    return s%11, s%5, s

#L = [23, 19, 90, 30]
#print(sorted(L,key=ordina_lista))



"""
Scrivere una funzione da usare come key
per ordinare liste di stringhe secondo
l'ultima lettera di ogni parola.
sorted(['car','bat','cup','sea','see'],key=key_function_ultima_lettera) ->
  ['sea','see','cup','car','bat']
"""
def key_function_ultima_lettera(s):
    return s[-1]

#L = ['car','bat','cup','sea','see']
#print(sorted(L,key=key_function_ultima_lettera))


"""  
Scrivere una funzione key che ordina la lista di
stringhe secondo l'ultima lettera, in caso di parità,
la lunghezza della parola, in caso di parità, l'ordine
alfabetico
['car','bat','map', cup','sea','see','rabat','butter']
['sea','see','cup','map',car','butter','bat', 'rabat']
"""
def key_function(s):
    return s[-1], len(s), s

#L = ['car','bat','map', 'cup','sea','see','rabat','butter']
#print(sorted(L,key=key_function))



"""
Scrivete una funzione che prende in input una lista
di stringhe e ritorna la lista ordinata in base
al numero di lettere di ogni stringa.
es: ordina(['cane','bue','gatto','topo','cinciallegra'])
-> ['bue', 'cane','topo','gatto','cinciallegra']
"""
def len_string(s):
    return len(s)

#L = ['cane','bue','gatto','topo','cinciallegra']
#print(sorted(L,key=len_string))

"""VERSIONE PROF"""
def ordina(lista, funzione=len):
    dic = {}
    for parola in lista:
        lunghezza = funzione(parola)
        dic[lunghezza] = dic.get(lunghezza, []) + [parola]
    nuova_lista = []
    print(dic)
    for lunghezza in sorted(dic.keys()):
        nuova_lista.extend(sorted(dic[lunghezza]))
    return nuova_lista



"""
Scrivere una funzione che permetta di
ordinare delle tuple (con almeno tre coordinate)
secondo l'ordine:
terza coordinata, prima coordinata, seconda coordinata

lista_tuple=[(1,2,3), (4,1,7), (12,76,34,53),
             (23,22,21), (2,2,2), (2,3,2)] 
--->
lista_tuple=[(2,2,2), (2,3,2), (1,2,3), 
             (4,1,7), (23,22,21), (12,76,34,53)]
"""
def ordina_tuple(s):
    return s[2], s[0], s[1]

#lista_tuple=[(1,2,3),(4,1,7),(12,76,34,53),(23,22,21),(2,2,2),(2,3,2)]
#print(sorted(lista_tuple, key=ordina_tuple))


"""
Scrivere una funzione che ritorna il numero di volte
che una sottosequenza presa come argomento compare
in una stringa

es: stringa = '0000000' e seq = '00'
la funzione ritorna 6
stringa = '00100100' e seq = '001'
la funzione ritorna 2
"""
            
def subseq_uguale(sub_string, testo):
    f=0
    for i in range(len(testo)+1-len(sub_string)):
        if sub_string==testo[i:i+len(sub_string)]:
            f+=1
    return f


def subseq_uguale(sub_string,testo):
    f=0
    lunghezza = len(sub_string)
    for i in range(len(testo)-lunghezza+1):
        confronta=''
        for j in range(lunghezza):
            confronta+=testo[i+j]
        if confronta==sub_string:
            f+=1
    return f

#print(subseq_uguale('00','0000000'))





"""
Scrivere una funzione che prende come argomento
una lista di stringhe e ritorna una nuova lista
in cui le stringhe sono ordinate in base
alla loro lunghezza
"""

























































