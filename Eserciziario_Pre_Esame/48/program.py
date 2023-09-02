import albero

'''
Si definisca la funzione es48(tree) ricorsiva (o che fa uso di funzioni o metodi ricorsive/i) che:
- riceve come argomento 'tree' un  albero  formato da nodi di tipo
  AlberoBinario definito nella libreria albero.py allegata
- calcola il numero di nodi che nell'albero hanno ESATTAMENTE due figli
- torna come risultato il numero calcolato
Esempio: se l'albero e':

         7
        /\
       1  3
      / \
    4    6
   /    /
  5    2
 /     \
9       8

Nell'albero ci sono solo due nodi con esattamente due figli (il nodo con valore 7 ed il nodo
con valore 1) cosi'  la funzione tornera' il valore 2.
'''


def es48(tree):
    # se il nodo è una foglia ritorno 0
    if not tree:
        return 0
    # se ho entrambi i nodi, incremento il count
    count = 0
    if tree.sx and tree.dx:
        count += 1
    return count + es48(tree.sx) + es48(tree.dx)

"""
SOLUZ. PROF
if tree == None:
    return 0
count = es48(tree.sx) + es48(tree.dx)
if tree.sx != None and tree.dx != None:
    count += 1
return count
"""
    
    
