''' 
la funzione es54(lista) che presa in input una lista contenente interi e stringhe, modifica 
la lista distruttivamente e restituisce un dizionario.
Al termine della funzione dalla lista devono risultare  cancellate tutte le stringhe e il dizionario 
restituito deve contenere come chiavi le stringhe cancellate ciascuna con attributo il numero di volte 
in cui occorrevano nella lista.
Ad esempio per lista=[1,'a',2,'b','a',8,'d',8] la funzione al termine restituisce il dizionario 
{'a':2,'b':1,'d':1} e la lista diviene [1,2,8,8]
'''


import copy

def es54(lista):
    dizio = {}
    
    # creo il dizionario
    for elemento in lista:
        if type(elemento) == str:
            dizio[elemento] = dizio.get(elemento, 0) + 1
            
    # creo la nuova lista eliminado le stringhe       
    for elemento in lista.copy():
        if type(elemento) == str:
            lista.remove(elemento)
    
    return dizio



        