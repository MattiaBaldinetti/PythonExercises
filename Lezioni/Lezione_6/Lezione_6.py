# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 12:30:30 2023

@author: matti
"""
nero = 0, 0, 0
bianco = 255, 255, 255
rosso = 255, 0, 0
verde = 0, 255, 0
blu = 0, 0, 255
cyan = 0, 255, 255
giallo = 255, 255, 0
viola = 255, 0, 255
grigio = 128, 128, 128


import images
import png



def crea_quadrato(larghezza, altezza, colore):
    quadrato = []
    #creo il quadrato di un unico colore
    for i in range(altezza):
        quadrato.append([colore] * larghezza)
    images.save(quadrato,'quadrato_blu.png')
    
    L = len(quadrato[0])
    H = len(quadrato)
    # bordo dx e sx di verde
    for x in range(H):
        quadrato[x][0] = verde
        quadrato[x][H-1] = verde
    images.save(quadrato,'quadrato_2Lati_colorati.png')
    
    # bordo sopra e sotto di rosso
    for x in range(L):
        quadrato[0][x] = rosso
        quadrato[L-1][x] = rosso
    images.save(quadrato,'quadrato_4Lati_colorati.png')
    
    # disegno di una linea diagonale dal altoSx al bassoDx
    i = 0
    while(i < H):
        quadrato[i][i] = nero
        i += 1
    images.save(quadrato,'quadrato_4Lati_1Diagonale.png')
    
    # disegno di una linea diagonale dal altoDx al bassoSx       
    i = 0
    while(H > 0):
        quadrato[H-1][i] = nero
        H -= 1 
        i +=1
    images.save(quadrato,'quadrato_4Lati_2Diagonali.png')
    return quadrato

img = crea_quadrato(300, 300, blu)
#images.visd(img)



"""
Scrivere una funzione che prende una immagine
come lista di liste,  tre interi x, y, l e un colore
e crea nell'immagine un quadrato di lato l a
partire dal punto x,y, che si sviluppa verso
destra e verso il basso
"""

def crea_quadrato_dentro_quadrato(immagine, x,y,l, colore):
    for i in range(l):
        for j in range(l):
            if y+i < len(immagine) and x+j < len(immagine[0]):
                immagine[y+i][x+j] = colore
    images.save(immagine,'quadrato_dentro_quadrato.png')
    return immagine

immagine = crea_quadrato_dentro_quadrato(img,50,50,50, nero)
images.visd(immagine)









"""
Scrivere una funzione che verifica se una lista
di liste può rappresentare una matrice

HINTS: verificare che le liste hanno tutte la
       stessa lunghezza e che tutti gli elementi siano
       dei numeri
"""
def verifica_matrici(lista_di_liste):
    # il cilo verifica che ogni sotto lista sia uguale di lunghezza
    i = 0
    while(i < len(lista_di_liste) - 1 ):
        if len(lista_di_liste[i]) != len(lista_di_liste[i+1]):
            return False    
        i += 1 
    # il ciclo verifica che ogni sotto lista sia composta da soli numeri
    for lista in lista_di_liste:
        if (all([isinstance(item, int) for item in lista])) == False:
            return False
    return True

#lista_di_liste = [ [1,2,3], [1,4,9] , [56,876,6] , [45,1,4] ]
#print(verifica_lista(lista_di_liste))

def get_row(m, n_riga):
    ''' Funzione che ritorna la riga "n_riga" della matrice '''
    return m[n_riga]


def get_column(m, n_colonna):
    ''' Funzione che ritorna la colonna "n_colonna" di m '''
    colonna = []
    for i in range(len(m)):
        colonna.append(m[i][n_colonna])
    return colonna
# return [riga[n_colonna] for riga in m]


def somma_matrici(a, b):
    ''' Funzione che ritorna una nuova matrice in cui gli
        elementi sono dati dalla somma degli elementi di
        a e b
    '''
    #if not all((check_matrix(a), check_matrix(b), len(a) == len(b), len(a[0]) == len(b[0]))):
    if not (verifica_matrici(a) and verifica_matrici(b) and len(a) == len(b) and len(a[0]) == len(b[0])): 
        return None
    c = [riga.copy() for riga in a]
    
    for n_riga, riga in enumerate(b):
        for n_colonna, colonna in enumerate(riga):
            c[n_riga][n_colonna] += colonna
            
    return c
    
#a = [[1,4,7,9], [5,8,9,0], [4,8,4,3], [5,6,7,9]]
#b = [[2,6,7,9], [9,8,9,550], [4,8456,4,35], [54,6,745,9]]
#print(somma_matrici(a, b))

def verifica_matrice_quadrata(m):
    ''' restituisce True se la matrice è quadrata, ovvero
        ha tante righe quante colonne '''
    return verifica_matrici(m) and len(m[0]) == len(m)


def prendi_diagonale(m, direzione=1):
    ''' restituisce la diagonale se la matrice è quadrata
        genera errore se la matrice non è quadrata '''
    if not verifica_matrice_quadrata(m):
        raise ValueError ('la matrice passata non è quadrata')
    diagonale = [m[i][i] for i in range(len(m))]
    return diagonale







"""
Scrivere una funzione che prende in input due nomi di file.
Il primo lo usa per leggere tutte le righe e il secondo
lo usa per scrivere tutte le righe del primo file, ordinate
in base al numero di caratteri della riga e in caso di parità
in base all'ultima lettera della riga
"""
def ordina_file(fin,fout):
    with open(fin) as f:
        lines = f.readlines()
    lines.sort(key=lambda l: (len(l), l[-2] if len(l)>2 else l[-1]))
    #print(lines)
    with open(fout, 'w') as f:
        f.writelines(lines)
    f.close()


#fin = "C:/Users/UtentePC/Desktop/Lezione_6/testo.txt"
#fout = "C:/Users/UtentePC/Desktop/Lezione_6/testoordinato.txt"
#print(ordina_file(fin,fout))



