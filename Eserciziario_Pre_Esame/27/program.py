
''' 
    Un modo comune di memorizzare tabelle e' come liste di dizionari. 
    Ogni riga della tabella corrisponde ad un dizionario le cui chiavi sono i nomi delle colonne della tabella.
    Questa collezione di dizionari e' poi memorizzata in una lista.
    Ad esempio la tabella
    
    nome  | anno | tel
  --------|------|---------
   Sofia  | 1973 | 5553546 
   Bruno  | 1981 | 5558432

puo' essere memorizzata come 
[{'nome': 'Sofia', 'anno': 1973 ,'tel': 5553546},{'nome': 'Bruno', 'anno': 1981 ,'tel': 5558432}]

'''


''' 
Si implementi la funzione es27(tabella, colonna, valore) che presi in input
- una tabella rappresentata tramite lista di dizionari
- una stringa con il nome di una delle colonne della tabella
- un valore
modifica distruttivamente la tabella eliminando  la colonna indicata e 
le righe che in quella colonna avevano valori diversi da valore.
La funzione deve poi restituire il numero di righe eliminate.
Ad esempio con  tabella = [{'nome': 'Sofia', 'anno': 1973 ,'tel': 5553546},
                            {'nome': 'Bruno', 'anno': 1981 ,'tel': 5558432}]
al termine di es27(dati, 'anno', 1981)  verra' restituito il numero 1 e la tabella 
risultera'  modificata  in [{'nome': 'Bruno','tel': 5558432}]

'''
def es27(tabella, colonna, valore):
    # mia soluzione 
    L_iniziale = len(tabella)
    

    # elimina la riga che ha valore diverso da quello in input
    for lista in tabella.copy():    # ciclo su una copia della tabella, 
                                    # ma modifico la tabella originale
        for key,value in lista.items():
            if (key == colonna and value != valore):
                tabella.remove(lista)
                break
        
    
    # elimina tutte le colonne con valore 'colonna'
    for lista in tabella:
        for key in lista.keys():
            if key == colonna:
                del lista[colonna]
                break
    
    L_finale = len(tabella)
    return L_iniziale - L_finale
    
"""
# soluzione del prof
tabella2 = [
    {
        c: v for c, v in riga.items() if c != colonna
    } for riga in tabella if riga[colonna] == valore
]
diff = len(tabella) - len(tabella2)
tabella[:] = tabella2
return diff
"""
    



# ESEMPIO
#tabella = [{'nome': 'Sofia', 'anno': 1973 ,'tel': 5553546},{'nome': 'Bruno', 'anno': 1981 ,'tel': 5558432}]
#print(es27(tabella, 'anno', 1981))










