# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 15:49:55 2023

@author: UtentePC
"""

"""
Scrivere una funzione che prende una stringa contenente una serie di parole 
separate da spazi e costruisce un dizionario in cui le chiavi sono le ultime 
lettere delle parole della stringa e i valori ad esse associati sono liste
con le parole che terminano con quella lettera. Le liste devono essere 
ordinate lessicograficamente.
"""

def dizionarioOrdinato(stringa):
    ultima_lettera = []
    dictionary = {}
    strin = stringa.split()
    #creo la lista con solo l'ultima lettera di ogni parola
    for i in range(len(strin)):
        ultima_lettera.append((strin[i][-1]))

    #creo il dizionario con chiave ogni lettera finale
    for i in range(len(ultima_lettera)):
        dictionary[ultima_lettera[i]] = []


    #aggiunge le parole con ultima lettera nel dictio
    for j in range(len(ultima_lettera)):   
        if ultima_lettera[j] in dictionary:   
            dictionary[ultima_lettera[j]].append(strin[j])  

    #ordina ogni lista }{}
    for key,value in dictionary.items():
        dictionary[key] = sorted(value)
    return dictionary

    
"""
Scrivere una funzione che prende un dizionario in cui ogni chiave è una 
stringa ed il valore è un intero e restituisce la lista ordinata di 
tutte le chiavi a cui corrisponde un valore pari.
"""

def listaParole(dizionario):  
   lista = []
   for item in dizionario.items():
       if((item[1]%2) == 0):
           lista.append(item[0])
   return sorted(lista)


# VERSIONE MENO EFFICIENTE 
""" 
    #lista con solo i valori
    valori = dizionario.values()
    lista_valori = list(valori)

    #lista con solo le chiavi
    chiavi = dizionario.keys()
    lista_chiavi = list(chiavi)
    
    lista_finale = []
    
    for i in range(len(lista_valori)):
        if((lista_valori[i] % 2) == 0):
            lista_finale.append(lista_chiavi[i])
    
    return sorted(lista_finale)
"""          


"""
Scrivere una funzione che prende un dizionario del tipo 
{chiave:lista interi} e restituisce un nuovo dizionario con 
le stesse chiavi ma come valore la media degli interi nella 
lista del dizionario originale.
"""

def mediaDizionario(dizionario):
    nuovo_dizionario = {}
    
    for chiave, lista_interi in dizionario.items():
        media = sum(lista_interi) / len(lista_interi)
        nuovo_dizionario[chiave] = media
        
    return nuovo_dizionario

# Esempio di utilizzo
dizionario_originale = {
    'chiave1': [1, 2, 3, 4, 5],
    'chiave2': [10, 20, 30],
    'chiave3': [100, 200, 300, 400]
}



"""
Scrivere una funzione che prende due dizionari chiave:lista e 
ritorna un nuovo dizionario in cui sono presenti solo le chiavi 
presenti in entrambi i dizionari in input e i valori sono la lista 
data dall'unione delle due liste in input, associate alla stessa chiave
"""

def unisciDizionari(dizionario1, dizionario2):
    nuovo_dizionario = {}
    
    #mi trovo le chiavi in comune tra i due dizionari, e le metto in ordine
    chiavi_comuni = sorted(set(dizionario1.keys()) & set(dizionario2.keys()))
    print(chiavi_comuni)
    for chiave in chiavi_comuni:
        #per ogni chiave comune, concatena le liste che gli appartengono rispettivamente
        lista_unione = dizionario1[chiave] + dizionario2[chiave]
        # crea il nuovo dizionario
        nuovo_dizionario[chiave] = lista_unione
        
    return nuovo_dizionario

# Esempio di utilizzo
dizionario1 = {
    'chiave1': [1, 2, 3],
    'chiave2': [10, 20, 30],
    'chiave9': [1, 23],
    'chiave4': [30, 18],
    'chiave7': [100, 95]
}

dizionario2 = {
    'chiave1': [4, 5],
    'chiave2': [40, 50],
    'chiave4': [400, 500, 600]
}



"""
Scrivere una funzione che prende una stringa di parole separate da 
spazi e costruisce un dizionario in cui le chiavi sono le lunghezze
delle parole e i valori sono set con le parole che hanno esattamente 
quella lunghezza in numeri di caratteri.
"""
def contaLettere(stringa):
    parole = stringa.split() #crea una lista com ogni parola
    dizionario = {}

    for parola in parole:
        lunghezza = len(parola) 
        if lunghezza not in dizionario:
            dizionario[lunghezza] = set()
        dizionario[lunghezza].add(parola)
        
    return dizionario

# Esempio di utilizzo
stringa_input = "la casa di campagna di mia zia è completamente immersa nel verde casa"

        
    


































