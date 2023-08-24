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


#import images
#import png

"""

immagine = []
for _ in range(1000):
    riga = []
    for _ in range(1000):
        riga.append(rosso)
    immagine.append(riga)
images.visd(immagine)
images.save(immagine, 'quadratorosso.png')
for riga in range(len(immagine)):
    immagine[riga][0]=verde
    immagine[riga][-1]=verde
for colonna in range(len(immagine[0])):
    immagine[0][colonna]=verde
    immagine[-1][colonna]=verde
images.save(immagine, 'quadratorosso_bordoverde.png')
for indice in range(len(immagine)):
    immagine[indice][indice] = verde
    immagine[-indice][indice] = verde
images.save(immagine, 'quadratorosso_bordoverde_sbarrato.png')

"""



"""
Scrivere una funzione che prende una immagine
come lista di liste,  tre interi x, y, l e un colore
e crea nell'immagine un quadrato di lato l a
partire dal punto x,y, che si sviluppa verso
destra e verso il basso
"""


"""
Scrivere una funzione che verifica se una lista
di liste può rappresentare una matrice

HINTS: verificare che le liste hanno tutte la
       stessa lunghezza e che tutti gli elementi siano
       dei numeri
"""

"""
Scrivere una funzione che prende in input due nomi di file.
Il primo lo usa per leggere tutte le righe e il secondo
lo usa per scrivere tutte le righe del primo file, ordinate
in base al numero di caratteri della riga e in caso di parità
in base all'ultima lettera della riga
"""
def ordina_file(file1, file2):
    with open("C:/Users/matti/OneDrive/Desktop/Lezione_6/testo.txt", 'r', encoding = 'utf-8') as file1:
        return file1.read()




F = open("C:/Users/matti/OneDrive/Desktop/Lezione_6/testo.txt", mode = 'r', encoding = 'utf-8')
lista_F = F.readlines()
lunghezza = len(lista_F) #25
dizio = {}
for riga in lista_F:
    dizio[riga] = dizio.get(riga, 0) + len(riga)
print(dizio)


















