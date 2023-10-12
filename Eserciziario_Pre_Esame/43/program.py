'''
Si progetti la funzione es43(ftesto) che, preso in input l'indirizzo di un file di testo
contenente righe contenenti interi separati da spazi, restituisce una lista  di interi.
La lunghezza della lista e' data dal numero massimo di interi che compaiono nelle righe
del file. E nella generica posizione i della lista c'e' l'intero corrispondente alla somma di tutti
gli interi presenti in posizione  i  nelle varie righe che contengono almeno i interi.
Ad esempio per il file contenente le  3 righe:
' 0 2  4
  6 8 10
  4 0  1'
la funzione restituisce la lista [10,10,15] cioe' le somme in colonna
Per il file contenente le  4 righe (nota, di lunghezza diversa):
' 1 2 3
  4 5 6 7 3 6
  1
  1 2'
la funzione restituisce la lista [7,9,9,7,3,6] cioe' le somme in colonna
'''
def es43(ftesto):
    file = open(ftesto)
    lista = []
    
    # una lista in cui ogni sottolista ha i numeri di ogni riga
    for riga in file.readlines():
        lista.append(riga.split())

    # calcolo la sottolista più lungha
    max_len = 0
    for elemento in lista:
        if len(elemento) > max_len:
            max_len = len(elemento)
     
    # inizializzo un dizionario {chiave: []}
    dizio = {new_list: [] for new_list in range(max_len)}

    # per ogni sottolista con indice i, assegno alla chiave i 
    # tutti i rispettivi valori dello stesso indice i-esimo
    for elemento in lista:
        for i in range(len(elemento)):
            dizio[i].append(int(elemento[i]))   #trasformo i valori da str a int
    
    lista_finale = []
    somma = 0
    
    # per ogni chiave calcolo la somma e la aggiungo alla lista finale
    for valori in dizio.values():
        for v in valori:
            somma += v
        lista_finale.append(somma)
        somma = 0
    
    return lista_finale
    



        
        








































