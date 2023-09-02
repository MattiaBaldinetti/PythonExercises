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
    # se ho entrambi i nodi, richiamo la fun su entrambi i nodi e sommo 1
    if tree._sx and tree._dx:
        return 1 + es48(tree._sx) + es48(tree._dx)
    # se c'è solo nodo a sx
    if tree._sx:
        return es48(tree._sx)
    # se c'è solo nodo a dx
    if tree._dx:
        return es48(tree._dx)

