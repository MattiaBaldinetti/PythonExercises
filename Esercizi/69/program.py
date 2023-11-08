"""
Si definisca la funzione  ricorsiva (o che usa una vostra funzione ricorsiva) es69(dir, profondita, estensioni),
che deve eliminare tutti i file che appartengono ad una delle estensioni indicate,
solo se si trovano alla profondita' indicata, e che riceve come argomenti:
    dir: la directory in cui cercare (i file in questa directory si trovano a profondita 0)
    profondita: la profondita' in cui dobbiamo cancellare i file, contando da 0 per la directory 
                radice passata come argomento
    estensioni: una lista di stringhe "estensioni" (le ultime lettere del nome dei files che cerchiamo)
La funzione deve tornare il numero totale di files presenti nelle directories di profondita' minore 
o uguali a 'profondita', che NON sono stati cancellati

NOTA: ignorate tutti i file e directory che iniziano con '.'

NOTA: per eliminare un file usate la funzione os.remove

Tests: date alcune directories contenenti file con estensioni diverse a diverse profondita', 
        si chiama la funzione e si controlla che i file contenuti nelle directories esistano/non 
        esistano a seconda del caso (senza usare una soluzione ricorsiva ma testando direttamente 
                                     i path dei files relativi alla dir iniziale)
Test: che la funzione sia ricorsiva
"""


import os
import os.path


def es69(dir, profondita, estensioni):
    count = 0
    # per ogni elemento nella dir
    for entry in os.listdir(dir):
        # verifica se inizia con il '.'
        if entry.startswith('.'):
            continue
        else:
            # aggiunge alla dir il nuovo path
            new_name = os.path.join(dir, entry)
            if profondita > 0:
                # verifica che il nuovo path completo sia una dir
                if os.path.isdir(new_name):
                    # richiama la funziome e incrementa il count
                    count += es69(new_name, profondita-1, estensioni)
                else: 
                    # incrementa solo il count
                    count += 1
            else:
                # se il path non è una dir
                if not os.path.isdir(new_name):
                    # verifica se l'estensione è presente nella lista
                    if new_name.endswith(tuple(estensioni)):
                        # rimuove il file
                        os.remove(new_name)
                    else:
                        # incrementa il count
                        count += 1
                
    return count




                









































