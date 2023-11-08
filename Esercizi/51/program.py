'''
progettare la funzione es51(ls,c) che: 
- riceve  in input una lista di parole ls ed un carattere c
- cancella da ls le parole che contengono il carattere c (sia in maiuscolo che in minuscolo)
- restituisce il numero di parole cancellate da ls. 
Nota che al termine della funzione la lista passata come parametro deve risultare modificata
(ricorda che le liste sono mutabili). 
 ESEMPI:
 Se ls=[ 'Angelo', 'Andrea', 'Fabio', 'Francesco', 'Lucio','Luca', 'Ugo'] e c='a'
 la funzione restituisce 5 e la lista ls diventa ['Lucio','Ugo']  
 Se ls=[ 'Angelo', 'Andrea', 'Fabio', 'Francesco', 'Lucio', 'Luca','Ugo'] e c='G'
 la funzione restituisce 2 e la lista ls diventa ['Andrea', 'Fabio', 'Francesco', 'Lucio','Luca']
'''

def es51(ls, c):
    count = 0
    # per ogni nome presente in una copia della lista
    for nome in ls.copy():
        # se la lettere min/maius è presente
        if c.upper() in nome or c.lower() in nome:
            # cancella il nome dalla lista reale
            ls.remove(nome)
            # incrementa il count delle parole cancellate
            count += 1
    return count

 

