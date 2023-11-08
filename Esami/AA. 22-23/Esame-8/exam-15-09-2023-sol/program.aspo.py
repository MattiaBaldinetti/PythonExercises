#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
 1) Salvare il file come program.py
 2) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Per superare l'esame e' necessario:
    - risolvere almeno 3 esercizi di tipo func AND;
    - risolvere almeno 1 esercizio di tipo ex (problema ricorsivo) AND;
    - ottenere un punteggio maggiore o uguale a 18

Il voto finale e' la somma dei punteggi dei problemi risolti.

Attenzione! DEBUG=True nel grade.py per migliorare il debugging.
Per testare correttamente la ricorsione è, però, necessario DEBUG=False.

"""

nome       = "Giulio"
cognome    = "Gigli"
matricola  = "3433"


# %% ----------------------------------- FUNC1 ------------------------- #
'''func1: 2 punti

Si definisca la funzione func1(int_list, keys) che prende in ingresso una
lista 'int_list' e un set 'keys' contenenti interi. La funzione restituisce
un dizionario in cui le chiavi sono gli interi in keys e i valori sono
liste con gli interi presenti in int_list divisibili per l'intero della
chiave corrispondente.
Le liste sono ordinate in ordine decrescente.


Esempio: se int_list=[4, 6, 10, 13] e keys={2, 3, 5}
  l'invocazione di func1(int_list, keys) deve restituire il dizionario
  {2:[10, 6, 4], 3:[6], 5:[10]}
'''
def func1(int_list, keys):
    d = {k:[i for i in int_list if i%k==0] for k in keys}
    for v in d.values():
        v.sort(reverse=True)
    return d


int_list=[4, 6, 10, 13]
keys={2, 3, 5}

print(func1(int_list, keys))

# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 punti

Si definisca una funzione func2(a_string, char) che prende in ingresso due
stringhe 'a_string' e 'char' e restituisce un'altra stringa. La stringa
'char' è composta da un solo carattere.
La nuova stringa ha tutte i caratteri della stringa a_string con un valore
unicode strettamente maggiore del valore del carattere in 'char'. I caratteri
nella stringa in output sono ripetute una volta sola e in ordine alfabetico
inverso.
Si suggerisce di usare la funzione ord per determinare il valore unicode di
un carattere.

Esempio: se a_string='impossible' l'invocazione di func2(a_string, 'i') dovrà
         restituire la stringa 'spoml'
'''

def func2(a_string, char):
    new_l = [a for a in set(a_string) if ord(a)>ord(char)]
    new_l.sort(reverse=True)
    return ''.join(new_l)

print(func2('impossible', 'i'))


# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 punti

Si definisca una funzione func3(string_list1, string_list2) che prende
in ingresso due liste di stringhe e restituisce una nuova lista di stringhe.
La nuova lista è costituita da tutte quelle stringhe presenti in una delle
due liste in ingresso che contengono come una sottostringa almeno una stringa
o un inverso dell'altra lista.
La lista risultante deve essere ordinata per numero di caratteri
decrescente, in caso di parità, in ordine alfabetico.

Esempio: se string_list1=['shop', 'park', 'elichopter', 'cat', 'elephant']  e
            string_list2=['ark', 'contact', 'hop', 'mark']
         l'invocazione di func3(string_list1, string_list2) dovrà restituire
         la lista ['elichopter','contact','park', 'shop']

         Infatti:
             'elichopter' contiene 'hop',
             'contact' contiene l'inverso di 'cat'
             'park' contiene 'ark'
             'shop' contiene 'hop'
'''

def func3(string_list1, string_list2):
    l = []
    for s in string_list1:
        for j in string_list2:
            if s in j or s[::-1] in j:
                l.append(j)
            if j in s or j[::-1] in s:
                l.append(s)
    return sorted(l, key = lambda x: (-len(x), x))


string_list1=['shop', 'park', 'elichopter', 'cat', 'elephant']
string_list2=['ark', 'contact', 'hop', 'mark']
print(func3(string_list1, string_list2))

# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 punti

Si scriva una funzione func4(input_file, output_file) che prende in
ingresso due stringhe, 'input_file' e 'output_file' che rappresentano
i percorsi a due file.
Per ogni riga del file indicato da 'input_file' bisogna creare una
riga all'interno di un nuovo file indicato da 'output_file'.
In ogni riga del file indicato da 'input_file' sono presenti una serie
di parole composte da caratteri numerici e alfabetici, separate da spazi
e tabulazioni. Per ogni parola, la funzione individua i caratteri numerici,
li trasforma in interi e li somma inseme. In seguito, la funzione calcola il
prodotto di tutti i valori ottenuti per quella riga, scrivendo il risultato
sotto forma di stringa in una nuova riga del file 'output_file'.
Ogni parola ha almeno un carattere numerico.

La funzione deve restituire la somma di tutti i prodotti calcolati.

Esempio: se il contenuto del file 'input_file' è il seguente
car13 5park5 spike2
no1ne rebel44 ni4ce

l'invocazione di func4('input_file', 'output_file') dovrà scrivere nel
file 'output_file' le due righe
80
32

e ritornare il valore 112.
"""
def get_value(word):
    return sum([int(c) for c in word if c.isdigit()])
    # return sum(map(int, filter(str.isdigit, word)))

def func4(input_file, output_file):
    with open(input_file) as f:
        l = []
        for line in f:
            words = line.split()
            s = 1
            for w in words:
                s*=get_value(w)
            l.append(s)
    with open(output_file, 'w', encoding='utf8') as f:
        for n in l:
            print(n, file=f)
    return sum(l)

print(func4('func4/func4_test1.txt','func4/func4_out1.txt'))
print(func4('func4/func4_test2.txt','func4/func4_out2.txt'))
print(func4('func4/func4_test3.txt','func4/func4_out3.txt'))


# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 8 punti

Si definisca una funzione func5(input_pngfile) che prende in ingresso
una stringa che contiene il percorso ad un file con un'immagine in
formato PNG.
L'immagine indicata da 'input_pngfile' contiene dei segmenti orizzontali di
colore uniforme su uno sfondo nero. La funzione deve individuare tutti i segmenti
presenti nell'immagine e ritornare un lista di triple rappresentanti
i colori dei segmenti individuati, ordinati per lunghezza. In caso di
segmenti di uguale lunghezza, i colori vanno ordinati considerando l'ordine
prima della terza componente, poi della seconda e infine della prima.
In caso di segmenti di uguale colore, si deve considerare quello con la
lunghezza maggiore.

Esempio: nell'immagine del file func5/image01.png sono presenti quattro segmenti
         uno di lunghezza 50 con colore (0, 128, 200)
         uno di lunghezza 30 con colore (200, 128, 200)
         uno di lunghezza 30 con colore (200, 200, 128)
         uno di lunghezza 29 con colore (0, 128, 200),
         per cui func5('func5/image01.png') deve restituire la lista
         [(0, 128, 200), (200, 200, 128), (200, 128, 200)]
"""
import images

def follow_segment(im, row, col):
    color = im[row][col]
    r = row
    c = col
    while c < len(im[r]) and im[r][c] == color:
        c+=1
    return color, c-col


def func5(input_pngfile):
    im = images.load(input_pngfile)
    d = {}
    for row in range(len(im)):
        col = 0
        while col < len(im[0]):
            if im[row][col] != (0,0,0):
                color, length = follow_segment(im, row, col)
                # print (length)
                d[color] = max(length, d.get(color, 0))
                col += length
            else:
                col+=1
    return sorted(d.keys(), key = lambda k: (-d[k], k[2], k[1], k[0]))





print(func5('func5/image01.png'))
print(func5('func5/image02.png'))
print(func5('func5/image03.png'))
print(func5('func5/image04.png'))


# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 punti

Si scriva una funzione ricorsiva ex1(a_set, n), o che al suo interno
usi una funzione ricorsiva, che prende in ingresso un set di stringhe 'a_set'
e un intero n e restituisca un nuovo set. Il set deve contenere tutte le
possibili stringhe ottenute con la concatenazione di n elementi appartenenti
ad da a_set, senza ripetizione.
Se n è maggiore del numero di elementi presenti in a_set, la funzione
restituisce un set vuoto.

Esempio:
    la funzione ex1({'a','b','c'}, 2) deve restituire l'insieme
    {'ab', 'ba', 'ac', 'ca', 'bc', 'cb'}
"""

def ex1(a_set, n):
    if len(a_set) < n:
        return set()
    if n == 1:
        return a_set

    full = set()
    for i in a_set:
        partial = ex1(a_set-{i}, n-1)
        for j in partial:
            full.add(i+j)
    return full

# print(ex1({'a','b','c','d'}, 3))
# print(ex1('ex1/B'))
# print(ex1('ex1'))


# %% ----------------------------------- EX.2 ------------------------- #
"""
Ex2: 6 punti

Si definisca la funzione ex2(root, m, n, k) ricorsiva (o che al suo interno
usa una funzione ricorsiva) che riceve in ingresso la radice di
un albero binario di interi, come definito nella classe `BinaryTree` del modulo
tree.py e tre interi m, n e k. La funzione ritorna il numero di nodi
dell'albero presenti ad un livello compreso fra m ed n, inclusi, con un
valore multiplo di k.
Si assume che la radice sia al livello 0.

Esempio:
        root
    ______5______           livello 0
   |             |
   8__        ___2___       livello 1
      |      |       |
     _3_     9       1      livello 2
    |   |
    6   12                  livello 3

    la chiamata a ex2(root, 1, 2, 3)  deve restituire il valore 2
  """



def ex2(root, m, n, k, level=0):
    # Inserire qui il proprio codice
    if not root:
        return 0
    if level<m:
        return ex2(root.left, m, n, k, level+1) + ex2(root.right, m, n, k, level+1)
    if level <=n:
        return (root.value % k == 0) + ex2(root.left, m, n, k, level+1) + ex2(root.right, m, n, k, level+1)
    if level > n:
        return 0



from tree import BinaryTree
root = BinaryTree.fromList([5, [8, None, [3, [6, None, None], [12, None, None]]], [2, [9, None, None],[1, None, None]]])
print(ex2(root, 1,2,3))

###################################################################################
from random import randint
def draw_seg(im, length=None):
    h, w = len(im), len(im[0])
    color = tuple(randint(0,255) for _ in (1,2,3))
    if not length:
        length = randint(1,w-1)
    row = randint(0,h-1)
    col = randint(0,w-length-1)
    im[row][col:col+length+1] = [color]*(length+1)
    print(row, col, length)

if __name__ == '__main__':
    # Place your tests here
    print('*'*50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenii puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)
