# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


"""
FILES 
    • with open(<filename>, mode=<mode>, encoding='utf8') as F:
     ...
    • F.read() legge tutto il contenuto
    • F.readline() legge UNA riga (compreso '\n' )
    • F.readlines() legge TUTTE le righe (compresi '\n' )
    • F.write(<string>) scrive un testo nel file (dovete aggiungere voi '\n')
    • print( ..., file=F) stampa nel file (molto comodo)
    • F.seek(0) torna alla posizione 0 (inizio)
"""



files = {
'C:/Users/UtentePC/Desktop/UNI/PRIMO ANNO (2020-2021)/PRIMO SEMESTRE-PRIMO ANNO/FONDAMENTI DI PROGRAMMAZIONE (Andrea Sterbini)/Esercizi_Attuali/files/holmes.txt' : 'utf-8-sig',
'C:/Users/UtentePC/Desktop/UNI/PRIMO ANNO (2020-2021)/PRIMO SEMESTRE-PRIMO ANNO/FONDAMENTI DI PROGRAMMAZIONE (Andrea Sterbini)/Esercizi_Attuali/files/alice.txt' : 'utf-8-sig',
'C:/Users/UtentePC/Desktop/UNI/PRIMO ANNO (2020-2021)/PRIMO SEMESTRE-PRIMO ANNO/FONDAMENTI DI PROGRAMMAZIONE (Andrea Sterbini)/Esercizi_Attuali/files/frankenstein.txt' : 'utf-8-sig',
'C:/Users/UtentePC/Desktop/UNI/PRIMO ANNO (2020-2021)/PRIMO SEMESTRE-PRIMO ANNO/FONDAMENTI DI PROGRAMMAZIONE (Andrea Sterbini)/Esercizi_Attuali/files/alice_it.txt' : 'latin',
'C:/Users/UtentePC/Desktop/UNI/PRIMO ANNO (2020-2021)/PRIMO SEMESTRE-PRIMO ANNO/FONDAMENTI DI PROGRAMMAZIONE (Andrea Sterbini)/Esercizi_Attuali/files/prince.txt' : 'utf-8-sig'
 }

# PER ESTRARRE LE PAROLE DA UN FILE CHE CONTIENE ANCHE SEGNI DI INTERRUZIONE 
def estrai_parole(filename, encoding): # apro il file e ne leggo il contenuto
    with open(filename, encoding=encoding) as FILE:
        text = FILE.read()
    # se voglio lo converto in lowercase (ma potrei preferire di no)
    text = text.lower()
    # calcolo l'insieme dei caratteri presenti nel testo
    caratteri = set(text)
    # ne estraggo solo i caratteri non-alpha
    nonalfa = [ c for c in caratteri if not c.isalpha() ]
    # li rimpiazzo con spazio
    for c in nonalfa:
        text = text.replace(c, ' ')
    # uso split sul testo in cui ho eliminato tutti i non-apha
    return text.split()
   
# esempio: parole del libro Alice nel paese delle meraviglie
parole = estrai_parole('C:/Users/UtentePC/Desktop/UNI/PRIMO ANNO (2020-2021)/PRIMO SEMESTRE-PRIMO ANNO/FONDAMENTI DI PROGRAMMAZIONE (Andrea Sterbini)/Esercizi_Attuali/files/alice_it.txt', 'latin')
#print(parole[:30])



# PER CONTARE QUANTE SONO LE PAROLE
def conta_parole(parole):
    # trovo le parole uniche usando un insieme
    parole_uniche = set(parole)
    # e costruisco il dizionario parola:conteggio usando count ### INEFFICIENTE!!!
    N = len(parole)
    return { parola: parole.count(parola)/N for parola in parole_uniche }

# rifaccio i conti sulle parole di Alice
conteggi = conta_parole(parole)
#print(list(conteggi.items())[:20])
# le 50 parole più presenti in Alice sono:
più_presenti = sorted(conteggi, reverse=True, key=lambda K: conteggi[K])[:50]
#(list(più_presenti))



# FREQUENZA DELLE PAROLE NEL FILE IESIMO
# - tf_i = # presenze / # parole del file
# per tutti i file costruiamo il dizionario del numero di files in cui appaiono
frequenze = {} # conteggio delle parole nei file: frequenze[name][parola] -> % di p
# conto le frequenze file per file
for filename, encoding in files.items():
#    print(filename)
    parole = estrai_parole(filename, encoding)
    conteggio = conta_parole(parole)
    frequenze[filename] = conteggio
#print(frequenze)



# CONTO I FILE CHE CONTENGONO UNA PAROLA
# presenze[parola] -> # di file che la contengono
presenze = {}
for filename in files:
    for parola in frequenze[filename]:
        presenze[parola] = presenze.get(parola, 0) + 1
# divido per il numero di file per avere la presenza %
Nfile = len(files) #5
for parola in presenze:
    presenze[parola] /= Nfile
list(presenze.items())[:30]



from math import log
# log dell'inverso della frequenza nei documenti
# - idf = log( # di file / # di file che contengono la parola )
idf = { parola : log(1/quante) for parola,quante in presenze.items() }
list(idf.items())[:30]
# NOTA: ogni parola appare in almeno UN file quindi 1/N è sempre calcolabile


# E FINALMENTE POSSO VEDERE QUALE FILE "PESA DI PIÙ" RISPETTO ALLE PAROLE DELLA QUERY
# date le parole di una query
# per ciascun file
    # ne conto la frequenza nel file
    # la moltiplico per idf
    # sommando ottendo il "peso" del file per quella query
query = ['turtle', 'alice']
pesi = {}
for file in frequenze:
    peso = 0
    for p in query:
        # aggiungo il peso della parola (0 se non presente)
        peso += frequenze[file].get(p,0) * idf[p]
    pesi[file] = peso
    #print(f"{file:30} {peso:00.3}")

# ordino i file per peso decrescente
sorted(pesi.items(), reverse=True, key=lambda coppia: coppia[1])



"""
FILE JSON

File di testo con sintassi semplificata per rappresentare:
    • dizionari
    • liste
    • interi, stringhe, float, bool, None
Molto usati nelle applicazioni WEB

Attenzione:
    • NON si possono inserire commenti
    • NO virgola aggiuntiva in fondo a lista o dizionario
    • SOLO chiavi semplici (NO tuple, SI int, float, str, none, bool)
    • SOLO doppi apici " (NO singoli apici)

Abbastanza facili da usare in python
Conversione automatica per alcuni tipi di dati
    • json.load(<file>) -> dict | list | tipo_base
    • json.dump(<obj>, <file>)
"""


## Esempio
import json

"""with open('api.github.com.json') as F:
    api = json.load(F)
!cat api.github.com.json"""


# posso anche leggere da una stringa in formato JSON
XX = json.loads('''
[{"nome": "Minnie", "cognome": "Mouse", "telefono": "555-54321",
 "indirizzo": "via di M.me Curie 1", "città": "Topolinia"},
{"nome": "Pippo", "cognome": "de' Pippis", "telefono": "555-33333",
 "indirizzo": "via dei Pioppi 1", "città": "Topolinia"}]
''')
#print(XX)
# oppure produrre la stringa in formato JSON da una struttura Python
#print(json.dumps(XX))



# Un file json può contenere valori semplici (int, float, str, True=true, False=false, Nprint(json.dumps(None))
#print(json.dumps([False, True]))
## NOTA: le stringhe DEVONO essere racchiuse da doppi apici
#print(json.dumps('Pape"rino'))


# Esempio: data una tabella come lista di dizionari
agenda = [
 {'nome': 'Paperino','cognome':'Paolino', 'telefono':'555-1313'}, 
 {'nome': 'Gastone', 'cognome':'Paperone', 'telefono':'555-1717'}, 
 {'nome': 'Paperon', 'cognome':"de' Paperoni", 'telefono':'555-99999'}, 
 {'nome': 'Archimede','cognome':'Pitagorico', 'telefono':'555-11235'}, 
 {'nome': 'Pietro', 'cognome':'Gambadilegno', 'telefono':'555-66666'},
 {'nome': 'Trudy', 'cognome':'Gambadilegno', 'telefono':'555-66666'},
 {'nome': 'Topolino','cognome':'Mouse', 'telefono':'555-12345'}, 
 {'nome': 'Minnie', 'cognome':'Mouse', 'telefono':'555-54321'}, 
 {'nome': 'Pippo', 'cognome':"de' Pippis", 'telefono':'555-33333'}
 ]

# prima la salvo nel file
"""with open('agenda.json', encoding='utf8', mode='w') as F:
    json.dump(agenda, F)
!cat agenda.json"""


# poi la ricarico
with open('agenda.json', encoding='utf8') as F:
    L1 = json.load(F)
L1[:2] # e ne mostro i primi 2 elementi



"""
FILE YAML

• dizionari (una chiave : valore per ciascuna riga)
• liste ( valori su righe diverse, preceduti da - )
• dati semplici (str senza apici se possibile, True, False, null=None, interi, float)
• documenti multipli
• generici oggetti Python (advanced)

Per annidare le strutture si usa l'indentazione
"""


import yaml
 
"""with open('agenda.yaml', mode='w', encoding='utf8') as F:
    yaml.dump(agenda[:2], F)
!cat agenda.yaml"""


"""
Leggere/scrivere file YAML
    • yaml.dump(<oggetto>, FILE) salva l'oggetto nel file aperto con open
    • yaml.safe_load(FILE) -> <oggetto> legge l'oggetto dal file aperto con open
"""

testo = """
 none: [~, null]
 bool: [true, false, on, off]
 int: 42
 float: 3.14159
 list:
 - LITE
 - RES_ACID
 - SUS_DEXT
 dict:
 hp: 13
 sp: 5
"""
yaml.safe_load(testo)


"""
LEGGERE PAGINE O FILE DA INTERNET

Ci sono molte librerie, la più comune è requests (https://requests.readthedocs.io/en/latest/user/quickstart/)
    • permette di eseguire sia GET che POST
    • con parametri
    • torna un codice di errore/OK
    • e decodifica il testo della pagina html o json
Molto potente, permette anche streaming, sessioni, ...
"""

# importo la libreria
import requests

# leggo la pagina di python.org
pagina = requests.get('https://python.org')

# lo status code ci dice se tutto è andato bene
status = pagina.status_code

# se è un testo nell'attributo text trovo il testo decodificato
contenuto = pagina.text
status, pagina.encoding, contenuto[:100]


"""
Le pagine JSON vengono automaticamente decodificate
"""
# leggo da internet una pagina JSON
pagina_json = requests.get('https://api.github.com')

# la decodifica avviene automaticamente col metodo json()
risultato = pagina_json.json()
risultato



"""
SCARICARE FILE BINARI
    • il contenuto "raw" è nell'attributo content della risposta
"""
## possiamo anche scaricare file binari
logo = requests.get('https://www.python.org/static/img/python-logo@2x.png')

# posso estrarre dagli headers le dimensioni e il tipo del file ()
print(logo.headers['Content-Type'], logo.headers['Content-Length'])

# se si tratta di un file di dati (immagine/audio/film ...)
# il contenuto lo trovo nell'attributo content
dati = logo.content

# per salvarlo devo aprire il file in scrittura ('w') e in modo binario ('b')
with open('logo.png', mode='wb') as F:
    F.write(dati)


"""
Passare parametri ad una GET
Si usa l'argomento params
    • parametri={ chiave: valore, ...}
    • requests.get( <URL>, params=parametri )
"""
# Search GitHub's repositories for requests
response = requests.get(
    #'https://api.github.com/search/repositories',
    'https://google.com',
    params={'q': 'requests+language:python'},
)
# response.json()
response.text[:1000]



"""
PASSARE PARAMETRI AD ALTRI METODI HTTP

Si usa l'argomento data=<dizionario>
    requests.post( 'https://httpbin.org/post', data={'key':'value'})
    
    requests.put( 'https://httpbin.org/put', data={'key':'value'})
    
    requests.delete( 'https://httpbin.org/delete')
    
    requests.head( 'https://httpbin.org/get')
    
    requests.patch( 'https://httpbin.org/patch', data={'key':'value'})
    
    requests.options('https://httpbin.org/get')

"""
















