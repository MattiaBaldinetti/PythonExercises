# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 16:05:39 2020

@author: Studente


Scrivere una funzione che prende in input due nomi di file.
Il primo lo usa per leggere tutte le righe e il secondo
lo usa per scrivere tutte le righe del primo file, ordinate
in base al numero di caratteri della riga e in caso di parità
in base all'ultima lettera della riga

"""

def ordina_file(fin, fout):
    with open(fin) as f:
        lines = f.readlines()
    lines.sort(key=lambda l: (len(l), l[-2] if len(l)>2 else l[-1]))
    with open(fout, 'w') as f:
        f.writelines(lines)
#        for line in lines:
#            f.write(line)
    