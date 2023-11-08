
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
Si implementi la funzione es28(tabella, colonna, valore) che presi in input
- una tabella rappresentata tramite lista di dizionari
- una stringa con il nome di una delle colonne della tabella
- un valore
restituisce la  sottotabella che si ottiene eliminando dalla tabella la colonna 
indicata e le righe che in quella colonna avevano valori diversi da valore.
La tabella originaria non deve essere modificata e nella nuova tabella 
le righe devono conservare il vecchio ordinamento.
Ad esempio con  tabella = [{'nome': 'Sofia', 'anno': 1973 ,'tel': 5553546},
                  {'nome': 'Bruno', 'anno': 1981 ,'tel': 5558432}]
al termine di es28(dati, 'anno', 1981) verra' restituita la tabella
[{'nome': 'Bruno','tel': 5558432}]
'''
def es28(tabella, colonna, valore):
    # creo la nuova lista    
    tabella2 = []
    
    # Itera attraverso le righe nella tabella
    for riga in tabella:
        # Verifica se il valore nella colonna specificata corrisponde al valore desiderato
        if riga[colonna] == valore:
            #creo il nuovo dizionario
            riga_modificata = {}
            # per ogni coppia chiave,valore, se la chiave non è la colonna da eliminare
            # allora aggiungi al dizio la coppia chiave, valore
            for c, v in riga.items():
                if c != colonna:
                    riga_modificata[c] = v
            # aggiungi il dizio alla lista
            tabella2.append(riga_modificata)
        
    return tabella2
    














