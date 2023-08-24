# -*- coding: utf-8 -*-
"""
immagine = []
for _ in range(1000):
    riga = []
    for _ in range(1000):
        riga.append(rosso)
    immagine.append(riga)
save(immagine, 'quadratorosso.png')
for riga in range(len(immagine)):
    immagine[riga][0]=verde
    immagine[riga][-1]=verde
for colonna in range(len(immagine[0])):
    immagine[0][colonna]=verde
    immagine[-1][colonna]=verde
save(immagine, 'quadratorosso_bordoverde.png')
for indice in range(len(immagine)):
    immagine[indice][indice] = verde
    immagine[-indice][indice] = verde
save(immagine, 'quadratorosso_bordoverde_sbarrato.png')
Created on Wed Nov 11 12:14:49 2020

@author: Studente

Scrivere una funzione che prende una immagine
come lista di liste,  tre interi x, y, l e un colore
e crea nell'immagine un quadrato di lato l a
partire dal punto x,y, che si sviluppa verso
destra e verso il basso

"""

def crea_quadrato(immagine, x,y,l, colore):
    for i in range(l):
        for j in range(l):
            if y+i < len(immagine) and x+j < len(immagine[0]):
                immagine[y+i][x+j] = colore

    
    
    

