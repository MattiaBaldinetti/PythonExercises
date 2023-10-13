'''
progettare la funzione es50(s,k) che: 
- riceve  in input una stringa s di caratteri che sono le cifre da  '0' a '9'  ed un intero k 
- costruisce la lista con  le diverse sottostringhe  di s  i cui caratteri sono in 
  ordine strattamente crescente.
- restituisce la lista dopo averne ordinato gli elementi in ordine decrescente
Nota che la lista non deve contenere duplicati. 
Si ricorda che una sottostringa di s e' quello che si ottiene da s eliminando 0 o piu' 
caratteri iniziali  e 0 o piu' caratteri finali.
ESEMPI: 
con  s='9135918246556' e k=3 la funzione restituisce la lista ['359','246', 135']
con  s='1234123412341234' e k=3 la funzione restituisce la lista ['234',123']
con  s='987654321' e k=3 la funzione restituisce la lista []
'''


def es50(s, k):
    # Inizializza un insieme per evitare duplicati
    result_set = set()

    # Itera su tutti gli possibili indici iniziali
    for i in range(len(s)):
        # Inizializza una sottostringa
        sub_str = s[i]
        
        # Itera sui successivi caratteri 
        # (scorre per tutta la len(s) ma tanto si ferma a 3 con il controllo sotto)
        for j in range(i + 1, len(s)):
            # Se il carattere corrente è maggiore del precedente, aggiungilo alla sottostringa
            if s[j] > s[j - 1]:
                sub_str += s[j]
            else:
                break  # Interrompi il ciclo se il carattere non è in ordine crescente
            # Se la sottostringa ha almeno lunghezza k, aggiungila all'insieme
            if len(sub_str) == k:
                result_set.add(sub_str)

    # Converti l'insieme in una lista e ordina gli elementi in ordine decrescente
    result_list = sorted(list(result_set), reverse=True)

    return result_list








              