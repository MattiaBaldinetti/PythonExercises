"""
Si definisca la funzione ricorsiva (o che usa una vostra funzione ricorsiva) es68(dir, estensioni),
che deve contare quanti file di certi tipi si trovano in una directory o in una delle sue sottodirectories,
e che riceve come argomenti
    dir: il path della directory in cui cercare
    estensioni: una lista di stringhe "estensioni" (le ultime lettere del nome dei files che cerchiamo)
La funzione deve tornare un dizionario che ha come chiavi le estensioni passate come argomento
e come valori il numero di file il cui nome termina in quel modo, solo se > 0
(ovvero, se nessun file con una data estensione appare nella directory o nelle sottodirectories
la chiave non deve apparire nel dizionario tornato dalla funzione).

Tests: date alcune directory contenenti file di tipo (ext) diverso, si chiama la funzione per contare alcuni 
        dei tipi di file nelle diverse directory
Test: che la funzione sia ricorsiva
"""

import os
import os.path

def es68(dir, estensioni):
    count = {ext: 0 for ext in estensioni}
    # viene utilizzato per ottenere l'elenco di tutti i file e le directory nella directory specificata
    for f in os.listdir(dir):
        fn = "{}/{}".format(dir, f)
        # viene utilizzato per verificare se il percorso specificato è una directory esistente o meno
        if os.path.isdir(fn):
            diz = es68(fn, estensioni)
            for k, v in diz.items():
                count[k] += v
        else:
            for ext in estensioni:
                if fn.endswith(ext):
                    count[ext] += 1
    for k in list(count.keys()):
        if count[k] == 0:
            del count[k]
    return count
    






# SOLUZIONE ITERATIVA
"""
Produce una tupla 3 (dirpath, dirnames, filenames) per tutto ciò che è 
raggiungibile dalla directory specificata, dove dirpath è il percorso della 
directory, dirnames è un elenco dei nomi delle sottodirectory in dirpath, 
e filenames è un elenco dei nomi dei file non di directory in dirpath.
"""
"""
dizio = {}
lista = []
# crea una lista con tutti i file delle sottodir
for root, dirs, files in os.walk(dir):
    for file in files:
        lista.append(os.path.join(root, file))

lista_extensions = []
# ritorna solo l'estensione del file senza il punto
for elemento in lista:
    file_name, file_extensions = os.path.splitext(elemento)
    lista_extensions.append(file_extensions.replace(".","")) 

#crea il dizionario in base allle estensoni dichiarate in iNput
for extension in lista_extensions:
    if extension in estensioni:
        dizio[extension] = dizio.get(extension,0) + 1
    
return dizio                                   
"""                                
                                 
                         