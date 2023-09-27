'''
 Es 5: 3 punti
 progettare la funzione es16(s,k) che: 
 - riceve  in input una stringa s di caratteri  ed un intero k 
 - costruisce la lista con  le diverse sottostringhe  di s  in cui compaiono 
   esattamente k caratteri distinti
 - restituisce la lista delle sottostringhe dopo averla ordinata  per
   lunghezze decrescenti e, a parita' di lunghezza, in ordine lessicografico
Nota che la lista non deve contenere duplicati.
Si ricorda che una sottostringa di s e' quello che si ottiene da s eliminando 0 o piu' 
caratteri iniziali  e 0 o piu' caratteri finali.
ESEMPI: 
con  s='aabbb' e k=1 la funzione restituisce la lista ['bbb', 'aa', 'bb', 'a', 'b']
cons s='bcafedg' e k=3 la funzione restituisce la lista ['afe', 'bca', 'caf', 'edg', 'fed']
cons s='ccaabbdd' e k=3 la funzione restituisce la lista 
     ['aabbdd', 'ccaabb', 'aabbd', 'abbdd', 'caabb', 'ccaab', 'abbd', 'caab']
'''



s1 = 'ccaabbdd'

k1 = 3
"""
x = 0
i = 0
j = 1
s = ''
lista = []

while (x < len(stringa)):
    print('X',x)
    while (j <= k):
        print(i)
        if (i == len(stringa)-1):
            s += stringa[i]
            j += 1
        elif (stringa[i] == stringa[i+1]):
            s += stringa[i]
            i += 1    
        else:
            s += stringa[i]
            j += 1
            i += 1  
    x += 1
    i = x
    j = 1
    lista.append(s)
    s = ''
    
"""    
    
    
def es16(s, k):
    # Inizializziamo una lista per le sottostringhe risultanti
    result = []
    
    # Iteriamo attraverso tutte le possibili lunghezze di sottostringhe
    for length in range(1, len(s) + 1):
        # Iteriamo attraverso tutte le posizioni di inizio delle sottostringhe
        for start in range(len(s) - length + 1):
            
            # Estraiamo la sottostringa
            sub_str = s[start:start + length]
            
            # Contiamo i caratteri distinti nella sottostringa
            distinct_chars = set(sub_str)
            
            # Se il numero di caratteri distinti è uguale a k, aggiungiamo la sottostringa alla lista risultante
            if len(distinct_chars) == k:
                result.append(sub_str)
    
    # Rimuoviamo i duplicati dalla lista
    result = list(set(result))
    
    # Ordiniamo la lista risultante per lunghezza decrescente e poi in ordine lessicografico
    result.sort(key=lambda x: (-len(x), x))
    
    return result
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    