
'''
Es 9: 3 punti
Si definisca la funzione es9(pathDir) ricorsiva (o che fa uso di funzioni o 
metodi ricorsive/i) che:
- riceve come argomento l'indirizzo di una cartella.
- restituisce una lista contenente i nomi delle sottocartelle in essa contenute a
  qualsiasi livello e per ogni sottocartella anche lo spazio  (in byte) occupato all'interno 
  della cartella da eventuali file di tipo .txt.
  La lista contiene dunque coppie, il primo elemento della coppia e' il nome di 
  una sottocartella ed il secondo e' lo spazio occupato dai file .txt presenti nella
  sottocartella.
  Le coppie devono comparire nella lista ordinate in modo decrescente rispetto 
  alla loro seconda componente e  a parita' vanno ordinate poi in modo lessicografico 
  crescente rispetto alla prima componente.
  File e cartelle il cui nome comincia  col carattere '.' non vanno considerati. 
  
  Ai fini dello svolgimento dell'esercizio possono risultare utili 
  le seguenti funzioni nel modulo os:
  os.listdir(), os.path.isfile(), os.path.isdir(), os.path.basename(), 
  os.path.getsize()

Esempio: con es9('Informatica/Software') viene restituita la lista:
[('SistemiOperativi', 287), ('Software', 10), ('BasiDati', 0)]

'''
path = "C:/Users/matti/OneDrive/Desktop/9/Informatica"
import os


def es9(pathDir):
    ls1=prova(pathDir)
    ls1+=[pathDir]
    ls_fin=[]
    for el in ls1:
        spazio=0
        for perc in os.listdir(el):
            p=el+'/'+perc
            if os.path.isfile(p):
                if p[-4:]=='.txt':
                    spazio+=os.path.getsize(p)
        ls_fin.append((os.path.basename(el),spazio))
    ls_fin=sorted(ls_fin,key=lambda x: (-x[1],x[0]))
    return ls_fin

def prova(path):
    if os.path.isfile(path):
        return []
    ls=[]
    for el in os.listdir(path):
        p=path+'/'+el
        ls=ls+prova(p)
        
        if os.path.isdir(p):
            ls+=[p]
    return ls



"""
def es9(pathDir):
    lista = []
    somma = 0
    for elemento in os.listdir(pathDir):
        if os.path.isdir(pathDir + '/' + elemento):
            return es9(pathDir + '/' + elemento)
        else:
            for file in os.listdir(pathDir):
                if os.path.isfile(file):
                    if elemento[0] == '.' and elemento[-4:] != ".txt":
                        somma = 0
                    else:
                        somma += os.stat(pathDir + '/' + elemento).st_size
            lista.append((os.path.basename(pathDir), somma))
            
    return lista
"""







                





                





                





                





                





                





