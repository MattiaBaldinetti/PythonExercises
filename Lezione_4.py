# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 16:55:40 2023

@author: matti
"""

"""
Scrivere una funzione che prende in input una lista di
stringhe e restituisce la lettera che è alla fine delle
stringhe con maggiore frequenza. In caso di parità,
prendiamo la prima in ordine lessicografico.

es ['batman', 'robin', 'thor','la cosa', 'la torcia umana', 'superman'] -> 'n'
"""
def freq_lettera_finale(lista_stringhe):
    diz = {}
    for stringa in lista_stringhe:
        lettera = stringa[-1]
        diz[lettera] = diz.get(lettera, 0) + 1
    # diz contiene le frequenze a fine stringa di tutte
    # le lettere che compaiono almeno una volta a fine
    # stringa diz={'n':2, 'r':1, 'a':1}
    freq_massima = 0
    char = 'z'
    for k in diz.keys():
        if diz[k] > freq_massima:
            freq_massima = diz[k]
            char = k
        elif diz[k] == freq_massima and char > k:
            char = k
    return char

#print(freq_lettera_finale(['thor','la cosa','batman','la torcia umana', 'robin','superman']))


"""
Scrivere una funzione che prende in ingresso una lista
di parole e crea un dizionario con la frequenza di ogni
lettera nelle parole della lista

es conta_lettere(['aaa','vaa']) -> {'a':5, 'v':1}
"""
def conta_lettere(lista_parole):
    diz = {}
    for parola in lista_parole:
        for lettera in parola:
            diz[lettera] = diz.get(lettera, 0) + 1
    return diz

#print(conta_lettere(['aada','vaa','cddas']))


"""
Scrivere una funzione che crea una lista unica
a partire da quattro liste con lo stesso numero di
elementi in cui c'è il primo elemento della prima,
il primo elemento della seconda...., il primo elenmento
della quarta, il secondo elemento della prima, il secondo
elemento della seconda....

l1, l2, l3, l4 -> l1[0],l2[0],l3[0],l4[0],l1[1],l2[1]...
"""
def unisciListe(lista1,lista2,lista3,lista4):
    n = len(lista1)
    nuova_lista = []
    for i in range(n):
        # versione più semplice e veloce
        # nuova_lista.extend([lista[i] for lista in (lista1,lista2,lista3,lista4)])    
        nuova_lista.append(lista1[i])
        nuova_lista.append(lista2[i])
        nuova_lista.append(lista3[i])
        nuova_lista.append(lista4[i])
    return nuova_lista    

#print(unisciListe([0,1,2,3,4,5], [10,11,12,13,14,15], [20,21,22,23,24,25], [30,31,32,33,34,35]))


"""
Scrivere una funzione che ritorna quali sono
le lettere presenti in una data stringa
"""
def trova_lettere(stringa):
    return set(stringa)

# versione meno efficiente 
"""    lista = []
    for lettera in stringa:
        if lettera == ' ':
            pass
        else:
            lista.append(lettera)
    return set(lista)
"""

#print(trova_lettere('ciao sono mario'))


"""
Scrivere una funzione che prende in input
una lista di stringhe e ritorna il
dizionario delle frequenze delle lettere
presenti nelle stringhe

['cane','cono','noce'] -> {'c':3, 'a':1,'n':3,
'o':3, 'e':2}
"""
def frequenzaLettere(lista_stringhe):
    dizio = {}
    for parola in lista_stringhe:
        for lettera in parola:
            dizio[lettera] = dizio.get(lettera, 0) + 1
    return dizio
    # se volessi le chiavi in ordine alfabetico
    # return dict(sorted(dizio.items()))

#print(frequenzaLettere(['cane','cono','noce']))


# ALTRI DUE MODI PER L'ESERCIZIO PRECEDENTE
def frequenza_lettere2(lista_stringhe):
    diz = {}
    for lettera in "".join(lista_stringhe):
            diz[lettera] = diz.get(lettera, 0) +1
    return diz

def frequenza_lettere3(lista_stringhe):
    stringa_unita = "".join(lista_stringhe)
    return {lettera:stringa_unita.count(lettera)
            for lettera in set(stringa_unita)}


"""
Scrivere una funzione che prende in input un dizionario
in cui i valori sono immutabili (es. NON sono liste)
e ritorna un nuovo dizionario in cui le chiavi sono
i valori del dizionario in input e i valori sono
le rispettive chiavi

{'a': 5, 'b': 1, 'v': 1, 'q': 4}
->
{1:{'v','b'}, 4:{'q'}, 5:{'a'}}
"""
def invertiDizionario2(dizio):
    inv_dizio = {}
    for key,value in dizio.items():
        x = inv_dizio.get(value,set())
        x.add(key)
        inv_dizio[value] = x
    return inv_dizio
        
def invertiDizionario(dizio):
    inv_dizio = {}
    for key,value in dizio.items():
        inv_dizio[value] = inv_dizio.get(value,set()).union(key)
    return inv_dizio

#print(invertiDizionario({'a': 5, 'b': 1, 'v': 1, 'q': 4}))






"""
Scrivere una funzioneche prende in input una lista
di parole e ritorna la lettera che è presente più
volte come ultima lettera fra le parole della lista

['capra', 'cavoli', 'capperi'] -> 'i'

"""
def ultimaLettera(lista_stringhe):
    diz = {}
    # il ciclo crea un diz con chiave 'lettera' e valore frequenza
    for stringa in lista_stringhe:
        lettera = stringa[-1]
        diz[lettera] = diz.get(lettera, 0) + 1
    # diz = {'n':2, 'r':1, 'a':1}
    freq_massima = 0
    char = 'z'
    for k in diz.keys():
        if diz[k] > freq_massima:
            freq_massima = diz[k]
            char = k
        elif diz[k] == freq_massima and char > k:
            char = k
    return char

#print(ultimaLettera(['capra', 'cavoli', 'capperi']))

def trova_finale_max(lista):
    diz = {}
    # il ciclo crea un diz con chiave 'lettera' e valore frequenza
    for parola in lista:
        lettera = parola[-1]
        diz[lettera] = diz.get(lettera, 0) + 1
    # diz = {'n':2, 'r':1, 'a':1}
    
    # ritorna il max tra i valori del dizionario
    massimo = max(diz.values())
    # il ciclo ritorna la chiave con valore max
    for k in diz.keys():
        if diz[k] == massimo:
            return k
#print(trova_finale_max(['capra', 'cavoli', 'capperi']))

        
def trova_finale_max2(lista):
    diz = {}
    massimo = 0
    for parola in lista:
        lettera = parola[-1]
        diz[lettera] = diz.get(lettera, 0) + 1
        if diz[lettera] > massimo:
            lettera_massimo = lettera
            massimo = diz[lettera]
    return lettera_massimo
#print(trova_finale_max2(['capra', 'cavoli', 'capperi']))











