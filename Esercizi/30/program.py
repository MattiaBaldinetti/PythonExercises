''' 
Si implementi la funzione es30(fname1,fname2,fname3) prende in input l'indirizzo di tre file di testo.
Il primo file di testo contiene un messaggio codificato dove ogni carattere e' stato 
sostituito da un intero di tre cifre.
Tutti i caratteri non numerici devono essere trasferiti come sono.
Nel secondo file  e' possibile ritrovare le corrispondenze numeri-caratteri tra i numeri 
del testo e il rispettivo carattere. 
Piu' precisamente questo secondo file e' organizzato in righe,  in ciascuna riga sono 
presenti un carattere  e un intero  di tre cifre  che gli corrisponde nel file di testo separati da almeno uno spazio.
Numeri diversi possono far riferimento ad uno stesso carattere e non tutti i numeri che appaiono in fname1
sono necessariamente presenti nel file di decodifica.
La funzione es30 deve decodificare il messaggio presente nel primo file grazie 
alle informazioni contenute nel secondo.
I numeri non presenti nel secondo file vanno decodificati con il simbolo '?'.
Il messaggio decodificato va poi salvato nel terzo file.
La funzione infine restituisce il numero di caratteri decodificati con il valore '?' presenti nel file decodificato.
Ad esempio se 
- il file fname1 contiene il testo '991118991991345      103    091027003091103?'
- il file fname2 contiene il testo 'n   091\n   t 991\n a   103\n a 127\n n 003\n  u 118 '
il testo decodificato da registrare in file3 sara': 'tutt? a n?nna?' e la funzione restituisce il numero 2.
Potete assumere che i caratteri numerici appaiano sempre raggruppati in triplette.
'''

def es30(fname1,fname2,fname3):
    # testo solo numeri 
    f1 = open(fname1,  "r", encoding = "utf-8")
    # metto qui dentro il contenuto del file
    testo1 = f1.read()
    # lista elem x elem del testo preso in input
    lista1 = list(testo1)
    
    
    # testo con lettere
    f2 = open(fname2,  "r", encoding = "utf-8")
    # metto qui dentro il contenuto del file
    testo2 = f2.read()
    # levo gli spazzi
    testo2 = testo2.split()
    # lista con lettere e numeri
    lista2 = list(testo2)
    
    # file su cui scrivere
    f3 = open(fname3,  "w", encoding = "utf-8")
    
    
    # mi creo dizionario con {lettera:valore}
    i=0
    dizio = {}
    while(i < len(lista2)):
        dizio[lista2[i+1]] = lista2[i]
        i += 2
    
     
    # conta quante volte devo mettere '?' pk non c'è corrispondenza nel dizio
    count = 0
    
    # creo stringa finale
    str_finale = ''
    i = 0
    while(i <= len(lista1)):
        if lista1[i] == ' ':    # se c'è uno spazio
            str_finale += ' '    # aggiungo lo spazio vuoto alla stringa
            i += 1
        else:   
            j = i
            i += 3
            stringa = ''.join(lista1[j:i])      # creo la mini stringa composta da 3 numeri
            if not stringa.isdigit():           # se la stringa non è un numero
                str_finale += stringa           # aggiungo il carattere alla str_finale
            elif (stringa not in dizio.keys()): # se la stringa non è una chiave del diz
                    str_finale += '?'
                    count += 1
            # per ogni chiave controlla se è uguale alla stringa
            for key,value in dizio.items():
                if (stringa == key):
                    str_finale += value     # aggiungo il valore associato alla chiave
                
    
    
    # inserisco la stringa nel file output1.txt
    f3.write(str_finale)
    f3.close()
    
    
    return count


# ESEMPIO
#fname1 = "C:/Users/UtentePC/Desktop/30/ftesto1.txt"
#fname2 = "C:/Users/UtentePC/Desktop/30/ftesto1b.txt"
#fname3 = "C:/Users/UtentePC/Desktop/30/output1.txt"
#print(es30(fname1,fname2,fname3))





"""
SOLUZIONE DEL PROF

def es30(fname1,fname2,fname3):
    mappa = {}
    with open(fname2, encoding='utf8') as f:
        for riga in f:
            c, n = riga.split()
            mappa[n] = c
    testo =''
    with open(fname1,encoding='utf8') as f:
        testo = f.read()
    testo1 = ''
    quanti = 0
    i = 0
    while i < len(testo):
        c = testo[i]
        if c in '0123456789':
            k = testo[i:i+3]
            i += 3
            if k in mappa:
                testo1 += mappa[k]
            else:
                testo1 += '?'
                quanti += 1
        else:
            i += 1
            testo1 += c
    with open(fname3, mode='w',encoding='utf8') as f:
        f.write(testo1)
    return quanti

"""

