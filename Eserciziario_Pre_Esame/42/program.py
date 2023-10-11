'''
Si progetti la funzione es42(fImageIn, fcolori, fImageOut) che
modifica il colore di alcuni pixel presenti in un imagine  PNG fImageIn  e salva poi l'immagine
modificata  in un nuovo file PNG FImageOut.
La funzione inoltre ritorna il numero di pixel dell'immagine i cui colori sono stati modificati.
I colori da modificare sono specificati dal file di testo fcolori.
Il file fcolori ha tante righe quanti sono i colori da modificare.
Ogni riga di fcolori contiene  6 interi a valori tra 0 e 255.
I primi tre indicano il colore da modificare
e i secondi tre il nuovo colore
Ad esempio la presenza eventuale della riga
0 0 0  255 255 255
indica che nell'immagine tutti  i pixel di colore nero ( i.e. di colore  (0,0,0)) devono
assumere colore bianco (i.e. devono assumere colore (255,255,255)).

NOTA: i colori devono essere sostituiti contemporaneamente
(e non con una sostituzione alla volta che potrebbe modificare un pixel piu' volte)

:param fImageIn: nome del file PNG contenente l'immagine da modificare
:param fcolori: nome del file di testo in cui trovare i colori da modificare
:param fImageOut: nome del file PNG in cui salvare l'immagine modificata
:return: numero di pixel modificati
'''

import immagini
import png 
def es42(fImageIn, fcolori, fImageOut):
    
    img = immagini.load(fImageIn)
    h = len(img)
    w = len(img[0])
    conteggio = 0
    palette = {}
    
    # apro il file.txt dei colori
    with open(fcolori) as f:
        for line in f:
            r, g, b, R, G, B = map(int, line.split())
            palette[(r, g, b)] = R, G, B
            # ES: {(255, 0, 0): (0, 255, 0), (0, 255, 0): (255, 0, 0)}
                        #c       palette[c]       #c       palette[c]
    for y in range(h):
        for x in range(w):
            c = img[y][x]
            if c in palette:
                img[y][x] = palette[c]
                conteggio += 1
    immagini.save(img, fImageOut)
    return conteggio































