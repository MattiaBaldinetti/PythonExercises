'''
Definite la funzione es63(fileParole,fileTerne) che prende in input:
- il path FileParole ad un file di testo contenente parole, una parola per ogni riga,
- il path fileTerne di un file di testo da creare.
La funzione legge le parole presenti nel file di FileParole e crea
un nuovo file di testo che salva all'indirizzo fileTerne e restituisce infine il
numero totale di caratteri presenti nelle parole del file FileParole (ignorando spazi e accapi).
Il file creato ha lo stesso numero di righe del file letto (una per ogni parola)
ma le parole in ciascuna riga sono sostituite da terne di interi. Piu' precisamente in
corrispondenza della generica parola s viene prodotta la stringa con la tupla
(a,b,c) seguita da accapo,
dove a e' la lunghezza della parola s, b e' il numero di vocali presenti nella
parola s e c e' il numero di lettere maiuscole presenti nella parola s.

Ad esempio se il file delle parole contiene le due parole 'PytHon' e 'fonDAMenti'
la funzione deve creare e salvare in fileTerne un  file di due righe con le due
terne (6,1,2) e (10,4,3) e restituire poi l'intero 16.
'''

def es63(fileParole, fileTerne):
    conteggio = 0
    # apro il file in lettura
    with open(fileParole, encoding='utf8') as fin:
        # apro il file in scrittura
        with open(fileTerne, mode='w', encoding='utf8') as fout:
            # per ogni riga nel file in lettura
            for line in fin:
                # leva spazi prima e dopo la str
                parola = line.strip()
                l = len(parola)
                conteggio += l
                num_v = 0
                num_MAIU = 0
                for carattere in parola:
                    if carattere in 'aiuoeAIUOE':
                        num_v += 1
                    if carattere.isupper():
                        num_MAIU += 1
                # scrive la terna nel file
                fout.write(str((l, num_v, num_MAIU)) + '\n')
    fout.close()
    return conteggio

   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        