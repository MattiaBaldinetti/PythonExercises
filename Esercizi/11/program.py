'''
Es 11: 3 punti
progettare la funzione es11(ftesto) che, preso in input 
l'indirizzo di un file di testo restituisce un dizionario avente per chiavi delle stringhe 
ed attributo liste di  stringhe.
Il file di testo contiene stringhe distinte di caratteri, si guardi 
ad esempio il file f9.txt. 
Le chiavi del dizionario si ottengono dalle stringhe presenti nel file dopo aver 
eliminato da queste le vocali ed aver riordinato lessicograficamente i caratteri rimanenti 
(ad esempio dalla stringa 'angelo' si ottine la chiave 'gln').
Attributo della chiave e' la lista contenente le stringhe del file che l'hanno generata. 
Nota che  stringhe diverse possono generare una stessa chiave come nel caso 
di  'casa', 'caso' e 'cose'
Le stringhe nella lista devono comparire  ordinate per lunghezza decrescente, a parita' 
di lunghezza, lessicograficamente.

Ad Esempio, per il file di testo f10.txt  la funzione restituisce  il dizionario:
{'prt': ['parto', 'porta'], 
'r': ['era', 'ora'], 
'pr': ['arpia', 'arpa'], 
'cs': ['casa', 'cosa'], 
'fll': ['follia', 'fallo', 'folla'], 
'rt': ['otre', 'tre'], 
'lp': ['piolo', 'polo']
}
'''

def es11(ftesto):
    # apro il testo
    file = open(ftesto)
    # creo la lista con tutte le parle
    lista_parole = file.read().split()
    # inizializzo una lista dove andranno le parole senza vocali
    lista_parole_consonanti = []
    #inizializzo dizionario
    dizio ={}
    vocali = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ""
    """
    Per ogni parola, se una lettera è una consonante, 
    allora creo la nuova stringa senza vocali
    """
    for stringa in lista_parole:
        for i in range(len(stringa)):
            if stringa[i] not in vocali:
                result += stringa[i]
        # ordino la stringa risultante fatta di sole consonanti
        result = ''.join(sorted(result)) #ordina la stringa 
        # crea una lista di valori per ogni chiave, che è la parola senza vocali, 
        # e ci mette dentro la stringa
        dizio.setdefault(result,[]).append(stringa) 
        
        
        # ordino le liste di valori per ogni chiave
        for key,values in dizio.items():
            # ordina in base alla lunghezza decrescente e in caso di parità alfabeticamente         
            values.sort(key=lambda x: (-len(x), x))
        
        # rinizializza la stringa vuota
        result = ''
        
    return dizio


#print(es11(path))

































































