# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 11:31:30 2023

@author: UtentePC
"""

# ROTAZIONE RICORSIVA DI IMMAGINI


"""
Suddivisione e rotazione ricorsiva NxN
• se N==1: la matrice resta così (caso base)
• se N>1:
    ▪ divido in 4 sottomatrici (riduzione)
    ▪ le ruoto di 90° (chiamata ricorsiva)
    ▪ le scambio
    ▪ le fondo in una matrice più grande (composizione)
    • a forza di dividere per 2 arrivo sempre a 1 (convergenza)
"""


# A B
# C D
def dividiP2(matrice):
    "divido la matrice nei suoi 4 quadranti"
    # NOTA: la matrice deve avere dimensione potenza di 2
    L = len(matrice)
    assert L>1 and L%2==0 # FIXME: dovrei controllare 2^n==L
    metà = L//2
    fascia_superiore = matrice[:metà]
    fascia_inferiore = matrice[metà:]
    A = [ riga[:metà] for riga in fascia_superiore ]
    B = [ riga[metà:] for riga in fascia_superiore ]
    C = [ riga[:metà] for riga in fascia_inferiore ]
    D = [ riga[metà:] for riga in fascia_inferiore ]
    return A, B, C, D

# vediamo se funziona
M = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]

N = [[1,2],[3,4]]

#print(*dividiP2(M),sep='\n\n')


def fondiP2(A, B, C, D):
    "fondo 4 matrici in una sola"
    AB = [ rigaA+rigaB for rigaA,rigaB in zip(A,B) ]
    CD = [ rigaC+rigaD for rigaC,rigaD in zip(C,D) ]
    return AB + CD
    
# test
A = [[1,2],[5,6]]
B = [[3,4],[7,8]]
C = [[9,10],[13,14]]
D = [[11,12],[15,16]]
#print(*fondiP2(A,B,C,D), sep='\n')



# A B
# C D

# B D
# A C
def ruotaP2(M):
    "ruoto una matrice che ha lato 2^L"
    # se N==1 la ritorno tal quale
    if len(M) == 1:
        return M
    # la divido in 4
    A, B, C, D = dividiP2(M)
    # le ruoto tutte e 4
    Aruotata = ruotaP2(A)
    Bruotata = ruotaP2(B)
    Cruotata = ruotaP2(C)
    Druotata = ruotaP2(D)
    # le scambio e le fondo
    return fondiP2(Bruotata, Druotata, Aruotata, Cruotata)
    
M = [['1', '2', '3', '4'],
     ['5', '6', '7', '8'],
     ['9', 'A', 'B', 'C'],
     ['D', 'E', 'F', 'G']]
#print(*ruotaP2(M), sep='\n')



def ruota(M):
    "generico ruota applicabile a matrici != da potenza di 2"
    # allargo la matrice alla prossima potenza di 2 nelle due direzioni
    W = len(M[0])
    H = len(M)
    i = 0
    while 2**i < W:
        i +=1
    larghezza = 2**i
    i = 0
    while 2**i < H:
        i +=1
    altezza = 2**i
    for riga in M:
        riga += [(0,0,0)] * (larghezza-W)
    M += [ [(0,0,0)] * larghezza for i in range(altezza-H) ]
    # ruoto la matrice
    ruotata = ruotaP2(M)
    # elimino le righe/colonne aggiunte
    ruotata = ruotata[larghezza-W:]
    return [ riga[:H] for riga in ruotata ]
    
M = [ ['0', '1', '2', ],
      ['4', '5', '6', ],
      ['8', '9', 'A', ]]
#print(*ruota(M), sep='\n')



import images

img = images.load('3cime.png')
ruotata = ruota(img)
images.save(ruotata,'3cime-90°.png')
images.visd(img) , images.visd(ruotata) # print taglia l'immagine


















































































































































