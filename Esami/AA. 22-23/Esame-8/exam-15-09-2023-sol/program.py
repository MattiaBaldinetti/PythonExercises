#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
 1) Salvare il file come program.py
 2) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Per superare l'esame è necessario:
    - risolvere almeno 3 esercizi di tipo func AND;
    - risolvere almeno 1 esercizio di tipo ex (problema ricorsivo) AND;
    - ottenere un punteggio maggiore o uguale a 18

Il voto finale è dato dalla somma dei punteggi degli esercizi risolti.

Attenzione! DEBUG=True nel grade.py per migliorare il debugging.
Per testare correttamente la ricorsione è, però, necessario DEBUG=False.

"""

nome       = "MATTIA"
cognome    = "BALDINETTI"
matricola  = "1935153"


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
    dizio = {}
    lista = []
    for numero in keys:
        for elemento in int_list:
            if (elemento % numero) == 0:
                lista.append(elemento) 
                
        dizio[numero] = sorted(lista,reverse=True)
        lista = []
    
    
    return dizio

#int_list=[4, 6, 10, 13]
#keys={2, 3, 5}

#print(func1(int_list, keys))


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
    stringa = ''
    
    for x in a_string:
        if x > char:
            stringa += x
            
    singola = set(stringa)
    singola = sorted(singola, reverse = True)
    stringa = ''
    
    for x in singola:
        stringa += x
        
    
    return stringa

#print(func2('impossible', 'i'))


# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 punti

Define a function func3(string_list1, string_list2) that takes
as input two lists of strings and returns a new list of strings.
The new list consists of all those strings in one of the
two input lists that contain as a substring at least one string
or an inverted string from the other list.
The resulting list must be sorted by number of characters
descending, in case of equality, in alphabetical order.

Example: if string_list1=['shop', 'park', 'elichopter', 'cat', 'elephant'] and
            string_list2=['ark', 'contact', 'hop', 'mark']
         the invocation of func3(string_list1, string_list2) shall return
         the list ['elichopter','contact','park', 'shop']

         In fact:
             'elichopter' contains 'hop',
             'contact' contains the inverted string of 'cat'
             'park' contains 'ark'
             'shop' contains 'hop'
'''

def func3(string_list1, string_list2):
    result = []
     
    for str1 in string_list1:
        for str2 in string_list2:
            if str2 in str1 or str2[::-1] in str1:
                result.append(str1)
                break
            
    for str2 in string_list2:
        for str1 in string_list1:
            if str1 in str2 or str1[::-1] in str2:
                result.append(str2)
                break

    result.sort(key = lambda x: (-len(x), x))
    
    return result

#string_list1=['shop', 'park', 'elichopter', 'cat', 'elephant']
#string_list2=['ark', 'contact', 'hop', 'mark']
#print(func3(string_list1, string_list2))

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
li trasforma in interi e li somma insieme. In seguito, la funzione calcola il
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
def func4(input_file, output_file):
    file_input = open(input_file)
    file_output = open(output_file, 'w')
    
    # creo una lista che rappresenta la riga
    # che contiene sottoliste che contengono ogni parola di quella riga
    lista = []
    for parola in file_input.readlines():
        lista.append(parola.split())
        
        
    # creo una lista di interi con i numeri estratti 
    lista_interi = [] 
    lista_count = [] #contiene la molt per ogni riga
    intero = 0
    molt = 1
    for parola in lista:
        for stringa in parola:
            for char in stringa:
                # somma tra loro numeri della stessa parola
                if char in '0123456789':
                    intero += int(char)
            lista_interi.append(intero)
            intero = 0
        
        # moltiplica tra loro i numeri estratti dalla stessa riga
        for i in range(len(parola)):
            molt = molt * lista_interi[i]
    
        lista_count.append(molt)
        molt = 1
        lista_interi = []
        
        
    # aggiungere al file in output la molt di ogni riga    
    for i in range(len(lista)):
        file_output.writelines(str(lista_count[i]) + '\n')
    
    file_output.close()
    
    
    molt = 1
    int_finale = 0
    for numero in  lista_count:
        int_finale += numero
    
    return int_finale

#print(func4('func4/func4_test1.txt','func4/func4_out1.txt'))
#print(func4('func4/func4_test2.txt','func4/func4_out2.txt'))
#print(func4('func4/func4_test3.txt','func4/func4_out3.txt'))


# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 8 punti

Si definisca una funzione func5(input_pngfile) che prende in ingresso
una stringa che contiene il percorso ad un file con un'immagine in
formato PNG.
L'immagine indicata da 'input_pngfile' contiene dei segmenti
orizzontali di colore uniforme su uno sfondo nero. Su una riga ci
possono essere piu segmenti di colore diverso, anche attaccati fra
loro.  La funzione deve individuare tutti i segmenti presenti
nell'immagine e ritornare un lista di triple rappresentanti i colori
dei segmenti individuati, ordinati dal piu lungo al piu corto. In caso
di segmenti di uguale lunghezza, i colori vanno ordinati considerando
l'ordine prima della terza componente, poi della seconda e infine
della prima. Le componenti seguono un ordine crescente.  In caso di
segmenti di uguale colore, si deve considerare quello con la lunghezza
maggiore.

Esempio: nell'immagine del file func5/image01.png sono presenti quattro segmenti
         uno di lunghezza 50 con colore (0, 128, 200)
         uno di lunghezza 30 con colore (200, 128, 200)
         uno di lunghezza 30 con colore (200, 200, 128)
         uno di lunghezza 29 con colore (0, 128, 200),
         per cui func5('func5/image01.png') deve restituire la lista
         [(0, 128, 200), (200, 200, 128), (200, 128, 200)]
"""
import images

def func5(input_pngfile):
    linee = {}
    img = images.load(input_pngfile)
    for row in img:
        lunghezza = 0
        colore = None
        for pixel in row:
            if pixel == (0,0,0):
                continue
            if pixel == colore:
                lunghezza += 1
            else:
                if colore is not None:
                    linee[colore] = max(linee.get(colore, 0), lunghezza)
                colore = pixel
                lunghezza = 1
        if colore is not None:
            linee[colore] = max(linee.get(colore, 0), lunghezza)
    return [x[0] for x in sorted(linee.items(), reverse=True, key=lambda x: (x[1], -x[0][2], -x[0][1], x[0][0]))]

# print(func5('func5/image01.png'))
# print(func5('func5/image02.png'))
# print(func5('func5/image03.png'))
# print(func5('func5/image04.png'))


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
    if n>len(a_set):
        return set()
    return _ex1(a_set, n)

def _ex1(a_set, n):
    if n==1:
        return a_set
    return {x+y for x in a_set for y in _ex1(a_set-{x}, n-1)}
    
    
#print(ex1({'a','b','c'}, 2))


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
    if root is None:
        return 0
    if m<=level<=n and root.value%k==0:
        return 1 + ex2(root.left, m, n, k, level+1) + ex2(root.right, m, n, k, level+1)
    else:
        return ex2(root.left, m, n, k, level+1) + ex2(root.right, m, n, k, level+1)


# from tree import BinaryTree
# root = BinaryTree.fromList([5, [8, None, [3, [6, None, None], [12, None, None]]], [2, [9, None, None],[1, None, None]]])
# print(ex2(root, 1,2,3))

###################################################################################

if __name__ == '__main__':
    # Place your tests here
    print('*'*50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenti puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)
