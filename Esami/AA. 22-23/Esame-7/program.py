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
    - !!!riempire le informazioni personali nelle variabili qui sotto!!!
    - AND risolvere almeno 1 esercizio di tipo ex (problema ricorsivo)
    - AND risolvere almeno 3 esercizi di tipo func
    - AND ottenere un punteggio maggiore o uguale a 18

Il punteggio finale è la somma dei punteggi dei problemi risolti.
"""
nome       = "MATTIA"
cognome    = "BALDINETTI"
matricola  = "1935153"

################################################################################
################################################################################
################################################################################
# ---------------------------- DEBUG SUGGESTIONS ----------------------------- #
# To run only some of the tests, you can comment the entries with which the
# 'tests' list is assigned at the end of grade.py
#
# To debug recursive functions you can turn off the recursive test setting
# DEBUG=True in the file grade.py
#
# DEBUG=True turns on also the STACK TRACE that allows you to know which
# line number in program.py generated the error.
################################################################################

#%% ---------------------------- FUNC 1 ---------------------------- #

'''
Func 1: 2 punti
Si definisca la funzione func1(diz1, diz2) che riceve come argomenti
due dizionari che hanno chiavi intere e valori liste di stringhe.  La
funzione deve tornare il dizionario che contiene le sole chiavi in
comune ad entrambi i dizionari.  I valori associati a ciascuna chiave
sono quelli che appaiono in una sola delle due liste associate a
quella chiave nei due dizionari.  Questi valori, senza ripetizioni,
vanno ordinati in ordine di lunghezza decrescente ed in caso di parità
in ordine alfabetico crescente.

Esempio:
diz1 = { 1: ['a', 'bc', 'a'], 2: ['b', 'cr', 'e'], 3: ['a', 'qrt', 'st'] }
diz2 = { 1: ['a', 'cd', 'f'], 5: ['b', 'cr', 'e'], 3: ['a', 'bn', 'c'] }
il risultato sarà  { 1: ['bc', 'cd', 'f'], 3: ['qrt', 'bn', 'st', 'c'] }
'''

def func1(diz1, diz2):
    diz3 = {}
    lista = []
    for k1,v1 in diz1.items():
        for k2,v2 in diz2.items():
            if k1 == k2:
                for x in v1:
                    if x not in v2:
                        lista.append(x)
                for x in v2:
                    if x not in v1:
                        lista.append(x)
                lista.sort(key=lambda x: (-len(x),x))
                diz3[k1] = lista
            lista = []
    
    return diz3



#diz1 = { 1: ['a', 'bc', 'a'], 2: ['b', 'cr', 'e'], 3: ['a', 'qrt', 'st'] }
#diz2 = { 1: ['a', 'cd', 'f'], 5: ['b', 'cr', 'e'], 3: ['a', 'bn', 'c'] }

#print(func1(diz1,diz2))

#%% ---------------------------- FUNC 2 ---------------------------- #

'''
Func 2: 2 punti

Si definisca la funzione func2(text) che riceve come argomento:
- text: una stringa formata da parole separate da spazi
e che ritorna un dizionario che ha:
  - come chiavi la lettera iniziale delle parole presenti, minuscola
  - come valore il numero di parole che contengono quella lettera
    ignorando la differenza tra minuscole e maiuscole

Esempio:
text = 'sOtto lA panca La caPra Canta Sopra LA Panca La CaPra crepa'
expected   = { 's':2, 'l':4, 'p':6, 'c':6}
'''

def func2(text):
    dizio = {}
    lista = text.split()
    count = 0
 
    for stringa in lista:
        dizio[stringa[0].lower()] = 0
    
    for k in dizio.keys():
        for stringa in lista:
            if k in stringa.lower():
                count += 1
        dizio[k] = count
        count = 0
    return dizio

# text = 'Nel Mezzo del caMmin Di nostra vita mi ritrovai in una selva oscura che la diritta via era smarrita'      
# print(func2(text))

#%% ---------------------------- FUNC 3 ---------------------------- #
'''
Func 3: 4 punti
Definite la funzione func3(textfile_in, textfile_out) che riceve come argomento:
- textfile_in:  il percorso di un file di testo da leggere
- textfile_out: il percorso di un file di testo da creare

Il file indicato da textfile_in contiene dei numeri
float oppure interi, positivi o negativi, separati da spazi.

La funzione deve leggere i numeri, ordinarli in ordine decrescente di
di caratteri numerici presenti e in caso di parità in ordine crescente di valore.

Quindi deve scrivere questi numeri ordinati nel file textfile_out,
separati da virgola e spazio. Infine la funzione restituisce la
quantità di numeri letti da textfile_in.

Esempio:
se il file textfile_in contiene la riga

-23.5 17 -141 +322.7 -3227

Nel file textfile_out la funzione deve scrivere la riga

-3227, +322.7, -141, -23.5, 17

e tornare il valore 5
'''

def func3(textfile_in, textfile_out):
    def criterio(elemento):
        cifre = elemento.replace('.','')
        cifre = cifre.replace('-', '')
        cifre = cifre.replace('+', '')
        return -len(cifre), float(elemento)
    with open(textfile_in) as FIN:
        numeri = FIN.read().split()
    numeri.sort(key = criterio)
    with open(textfile_out, mode='w') as FOUT:
        print(*numeri, sep=', ', file=FOUT)
    return len(numeri)




#print(lista_ordinata)
#print(func3('func3/in_1.txt', 'func3/out_1.txt'))

#%% ---------------------------- FUNC 4 ---------------------------- #

'''
Func 4: 4 punti
Si definisca la funzione func5(filein) che riceve come argomento
- filein: un file di testo contenente una matrice di interi NxM
  separati da spazi

e che ritorna la matrice trasposta rispetto alla diagonale secondaria,
ovvero quella che va dall'elemento in alto a destra a quello in basso
a sinistra. La matrice da restituire e' rappresentata come lista di liste.

Esempio:
se il file filein contiene la matrice
1   2   3   4
5   6   7   8
9   10  11  12

la funzione dovrà tornare la matrice riflessa rispetto alla diagonale 4-9,
come lista di liste
[[12, 8, 4],
 [11, 7, 3],
 [10, 6, 2],
 [ 9, 5, 1]]
'''


def func4(input_filename):
    file = open(input_filename, 'r')
    l =[]
    # crea sottoliste di numeri in formato str
    for linea in file.readlines():
        l.append(linea.split())
    
    ll = []
    matrice = []
    # trasfromo i numeri nelle sottoliste in int
    for lista in l:
        for num in lista:
            ll.append(int(num))
        matrice.append(ll)
        ll = []
    

    lista = []
    output = []
    # creo la matrice finale
    for w in range(len(matrice[0])-1, -1,-1):
        for h in range(len(matrice)-1, -1,-1): #altezza
            lista.append(matrice[h][w])
        output.append(lista)
        lista = []

    return output


#print(func4('func4/in_1.txt'))

#%% ---------------------------- FUNC 5 ---------------------------- #

'''
Func 5: 8 punti
Si definisca la funzione func5(txt_input, width, height, png_output) che riceve come argomenti

- txt_input:  il percorso di un file che contiene un elenco di figure da disegnare
- width:      larghezza in pixel dell'immagine da creare
- height:     altezza in pixel dell'immagine da creare
- png_output: il percorso di una immagine PNG che dovete creare, contenente le figure

La funzione deve creare una immagine a sfondo nero e disegnarci sopra
tutte le figure indicate nel file 'txt_input', nell'ordine in cui
appaiono nel file.

Il file txt_file contiene, una per riga, separate da spazi:
- una parola che indica il tipo di figura da disegnare
- le tre componenti R G B del colore da usare
- le coordinate e gli altri parametri necessari a definire la figura

Possono essre presenti 2 tipi di figura:
- diagonale discendente di un quadrato (in direzione -45°)
    diagonalDOWN R G B x y L
    La diagonale inizia nel punto (x,y), si dirige in BASSO a destra, ed è lunga L pixel
- diagonale ascendente di un quadrato (in direzione +45°)
    diagonalUP R G B x y L
    La diagonale inizia nel punto (x,y), si dirige in ALTO a destra, ed è lunga L pixel

Quindi deve salvare l'immagine ottenuta nel file 'png_output' usando la funzione images.save.
Inoltre deve ritornare il numero di diagonali disegnate dei due tipi
come tupla dei due valori (DIAGUP,DIAGDOWN)

NOTA: va gestito correttamente lo sbordare delle figure dalla
immagine, infatti sono ammesse anche coordinate negative, e dimensioni
o parametro L tali da far sbordare la figura dalla immagine

Esempio: se il file func5/in_1.txt contiene le 3 righe
diagonalDOWN 0 255 0 -30 -40 110
diagonalUP 255 0 0 20 100 200
diagonalUP 0 0 255 10 120 50

l'esecuzione della funzione func5('func5/in_1.txt', 50, 100, 'func5/your_image_1.png')
produrrà una figura uguale al file 'func5/expected_1.png'
e tornerà la coppia (2, 1)
'''


import images

def func5(txt_input, width, height, png_output):
    count_up = 0
    count_down = 0
    
    # creo la matrice a sfondo nero
    img = [[(0,0,0) for _ in range(width)] for _ in range(height)]
    
    # apro il file in input
    file = open(txt_input, 'r')
    file = file.readlines()
    # ottengo i valori per ogni figura da creare
    for riga in file:
        figura, r, g, b, x, y, L = riga.split()
        r,g,b,x,y,L = int(r),int(g),int(b),int(x),int(y),int(L)
        colore = (r,g,b)

        if figura == "diagonalDOWN":
            count_down += 1
            draw_diagonalDown(img, width, height, x, y, L, colore)
        else:   
            count_up += 1
            draw_diagonalUP(img, width, height, x, y, L, colore)

    images.save(img, png_output)
    return count_up, count_down


def draw_diagonalUP(img, W, H, x, y, L, colore):
    i = 0
    while(i<L):
        if 0 <= x < W and 0 <= y < H:
            img[y][x] = colore
        x += 1
        y -= 1
        i += 1
    
    
def draw_diagonalDown(img, W, H, x, y, L, colore):
    i = 0
    while(i<L):
        if 0 <= x < W and 0 <= y < H:
            img[y][x] = colore
        y += 1
        x += 1
        i += 1
            
            

# print(func5('func5/in_2.txt', 50, 100, 'func5/out_2.png'))



#%% ----------------------------------- EX 1 ----------------------------------- #

'''
Esercizio 1 ricorsivo (6 punti):

Si definisca la funzione es1(root, valori), ricorsiva o che usa funzioni ricorsive,
che riceve in input:
- la radice 'root' di un albero n-ario definito da nodi nary_tree.NaryTree
- una lista di interi 'valori'
che modifica distruttivamente l'albero 'root' sommando a tutti i nodi
che sono a profondità P il valore che nella lista 'valori' si trova
all'indice P, se esiste, altrimenti restano come sono. Si assuma che
la radice si trovi a profondità 0.

La funzione deve restituire la somma 'total' di tutti i nodi
dell'albero risultante.

ATTENZIONE: definite la funzione ricorsiva a livello esterno,
ovvero con la parola chiave 'def' appoggiata all'inizio della riga.

Esempio:
    values: [-42, -80, 68, 2, 81, 75, 54, 48, -4, 5]        da sommare
    root:                        -7                         | -42
                    /      |      |      |    \             |
                  -10      -3     -8    -10    -5           | -80
                /   \      |       |     |                  |
               6    -2     9       7     -9                 | +68

    expected:                    -49                         |
                    /      |       |      |     \            |
                  -90     -83     -88    -90    -85          |
                /   \      |       |      |                  |
               74    66   77       75     59                 |
    total = -134

'''

from nary_tree import NaryTree


def ex1(root : NaryTree, valori : list[int]):
    if root is None:
        return 0
    else:
        root.value += valori[0] 
    tot = root.value
    if len(root.sons) > 0:
        for son in root.sons:
            tot += ex1(son, valori[1:])
    return tot

    
#%% ----------------------------------- EX.2 ----------------------------------- #


'''
Ex2: 3 + 3 points
Definite la funzione ex2(dirin, words), ricorsiva o che usa funzioni o metodi ricorsivi,
che riceve come argomenti:
  - dirin: il path di una directory
  - words: una lista di parole

La funzione esplora dirin e tutte le sue sottodirectory (a tutti i
livelli) e conta il numero di occorrenze delle words nei file di testo
(quelli che hanno '.txt' come estensione) a tutti i livelli.  Una
parola appare in un file se è separata dalla precedente o dalla
seguente da almeno uno spazio, tab, o newline.

(3 points)
La funzione torna una lista di coppie (word, occorrenze) in cui il
primo elemento è la word ed il secondo è il numero di occorrenze
trovate.  Se una word non appare in alcun file il suo numero di
occorrenze è 0.

(+ 3 points)
Ordinate la lista di coppie in ordine decrescente di numero di
occorrenze ed in caso di parità in ordine alfabetico crescente.

NOTA 1: potete usare le funzioni: os.listdir, os.path.join,
os.path.isfile, os.mkdir, os.path.exists ...
NOTA 2: è proibito usare la funzione os.walk
NOTA 3: usate il carattere '/' come separatore dei path
(che funzione sia in Windows che su MacOS o Linux)

Esempio:
se il path dirin è "ex2" e le words = ["cat", "dog"]
la funzione ritorna: [('dog', 10), ('cat', 5)]
'''

import os


def ex2(dirin, words):
    diz = {}
    for w in words:
        diz[w] = 0
    _ex2(dirin, diz)
    return sorted(diz.items(), key = lambda t: (-t[1], t[0]))

def _ex2(dirin, diz):
    for path in os.listdir(dirin):
        new_path = os.path.join(dirin,path)
        if os.path.isdir(new_path): 
            _ex2(new_path, diz)
        else:
            if new_path.endswith('.txt'):
                file = open(new_path, 'r')
                parole = file.read().split()
                for w in diz.keys():
                    diz[w] += parole.count(w)
    return diz

#words = ["cat", "dog"]
#path = "C:/Users/UtentePC/Desktop/Esame-7/ex2"                  
#print(ex2(path,words))
######################################################################################

if __name__ == '__main__':
    # Scrivi qui i tuoi test addizionali, attenzione a non sovrascrivere
    # gli EXPECTED!
    print('*' * 50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print(
        'Altrimenii puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*' * 50)


