# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 17:27:44 2023

@author: UtentePC
"""

"""
RICORSIONE:
• è possibile rimpicciolire la dimensione del problema da risolvere (riduzione)
• esiste almeno un problema che ha una soluzione elementare (caso base)
• è sempre possibile, applicando ripetutamente la riduzione, arrivare ad un caso base (convergenza)
• è possibile ottenere la soluzione del problema iniziale dalle soluzioni dei sottoproblemi (composizione)


def funzione(problema):
    if is_caso_base(problema):
        return soluzione nota
    else:
        sottoproblema = riduzione(problema)
        sottosoluzione = funzione(sottoproblema)
        soluzione = composizione(sottosoluzione)
        return soluzione
    
"""
# decoratore che stampa le chiamate ed uscite di una funzione ricorsiva
from rtrace import trace


@trace
def fattoriale(N:int) -> int:
    if (N==1):
        return 1
    else:
        return N*fattoriale(N-1)
 
dec = trace(fattoriale)
dec(5)


@trace()
def fibonacci(N):
    if (N<2):
        return 1
    else:
        return fibonacci(N-1) + fibonacci(N-2)
    
#fibonacci.trace(4)

def fibonacci_iterativa(N):
    coppie = [0, 1]
    for i in range(N):
        print(coppie)
        coppie.append(coppie[-1] + coppie[-2])
    print(coppie)
    return coppie[-1]

#print(fibonacci_iterativa(7))


def fibonacci_iter2(N : int) -> int :
    corrente, precedente = 1, 0
    for i in range(N):
        corrente, precedente = corrente+precedente, corrente
    return corrente

#print(fibonacci_iter2(7))




# proviamo invece a lavorare in uscita dalla ricorsione
# - ciascuna chiamata ritorna la coppia corrente, precedente
# ovvero calcoliamo F(N) -> corrente, precedente
# - nel caso base la coppia è 1, 0
# - da corrente, precedente del mese prima (N-1) posso calcolare quelli di N

@trace()
def fibonacci_efficiente(N : int ) -> tuple[int,int] :
    if N == 0:
        return 1, 0 # all'inizio ci sono 0 ed 1 coppia
    else:
        # ottengo i due valori del mese precedente (F(N-1) e F(N-2))
        corrente, precedente = fibonacci_efficiente(N-1)
        # calcolo i due valori per questo mese (F(N) e F(N-1))
        return corrente+precedente, corrente

#print(fibonacci_efficiente(5)[0])

#fibonacci_efficiente.trace(5)



"""
Massimo Comun Divisore di x,y interi positivi
Ovvero dobbiamo trovare quel'intero tale che:
x = M * k
y = M * j
con k,j >= 1 (e senza fattori comuni)

Quali sono le proprieta di ed ?
• se x==y allora k==j==1 e M=x (ecco un buon caso base!)
• altrimenti proviamo a sottrarre il minore dal maggiore
    ▪ z = x-y = M*(k-j) quindi z e y hanno lo stesso MCD,
    e inoltre z è più piccolo di x (ecco la nostra riduzione!)
        ◦ ad ogni passo si riduce la somma k+j di almeno j (il più piccolo)
        ◦ sottraendo un numero più piccolo non si può andare nei negativi
▪ a forza di sottrarre arriveremo per forza a j=k=1 ovvero al caso base (ed ecco la convergenza)
▪ una volta trovato M abbiamo la soluzione di ciascun caso più grande (ricomposizione)

Ottimizzazione: invece di sottrarre y da x calcoliamone il resto -> algoritmo di Euclide
"""
@trace()
def MCD(a,b):
    if not 0<=b<a:
        return False
    else:
        if(b==0):
            return a
        else:
            q = a/b
            r = a%b
            a,b = b,r
            return MCD(a,b)

#print(MCD.trace(108,64))


def MCD_iter(x:int , y:int) -> int:
    while (x != y):
        if (x > y):
            x -= y
        else:
            y -= x
    return x

#print(MCD_iter(108, 64))



"""
Check se una stringa/lista è palindroma
"""

def palindroma_iter(sequenza):
    rovesciata = sequenza[::-1]
    return rovesciata == sequenza

frase = "amoRoma"
#print(palindroma_iter(frase))


def palindroma_iter2(sequenza):
    for i in range(len(sequenza)//2):
        print('comparing', sequenza[i], sequenza[-i-1], sequenza[i]==sequenza[-i-1])
        if sequenza[i] != sequenza[-i-1]:
            return False
    return True

lista = [1, 2, 3, 4, 5, 4, 3, 2, 1]
#print(palindroma_iter2(frase))
#print()
#print(palindroma_iter2(lista))


@trace()
def palindroma_ric(sequenza) -> bool:
    if (len(sequenza) < 2):
        return True
    if(sequenza[0] != sequenza[-1]):
        return False
    else:
         return palindroma_ric(sequenza[1:-1])
        
#palindroma_ric.trace(frase)

@trace()
def _palindroma_ric2(sequenza, inizio:int, fine:int) -> bool:
    if inizio >= fine:
        return True 
    if sequenza[inizio] != sequenza[fine]:
        return False
    return _palindroma_ric2(sequenza, inizio+1, fine-1)

#_palindroma_ric2.trace(frase,0,6)



"""
Esploriamo un albero di directory: cerchiamo tutti i file .txt e la loro dimensione
• una directory contiene files (caso base) e sottodirectory (caso ricorsivo)
• ogni volta che esaminiamo una sottodirectory abbiamo un problema simile a quello iniziale, e più piccolo
• a forza di scendere arriveremo in una sottodirectory che contiene solo file (convergenza)
• i file trovati nelle sottodirectory vanno raccolti assieme a quelli della dir iniziale (composizione)
"""
# Per esaminare directory e files si usa la libreria os

import os

@trace()
def cerca_file_sizes(directory : str) -> dict[str, int] :
    "cerco tutti i file '.txt' e ne ritorno le dimensioni"
    risultato = {}
    for nome in os.listdir(directory):
        # ignoro file e dir che iniziano per '.' oppure '_'
        if nome[0] in '_.': continue
        fullname = directory + '/' + nome
        # se sono nel caso ricorsivo
        if os.path.isdir(fullname):
            trovati = cerca_file_sizes(fullname)
            risultato.update(trovati)
        # altrimenti se Ã¨ un file che finisce con 'txt'
        elif nome.endswith('.txt'):
            size = os.path.getsize(fullname)
            risultato[fullname] = size
    return risultato
        
percorso = "C:/Users/UtentePC/Desktop/UNI/PRIMO ANNO (2020-2021)/PRIMO SEMESTRE-PRIMO ANNO/FONDAMENTI DI PROGRAMMAZIONE (Andrea Sterbini)/Esercizi_Attuali/File/files"
#cerca_file_sizes.trace(percorso)



"""
Soluzione ricorsiva che raccoglie i file
in un dizionario fornito come argomento
"""
def cerca_file_sizes2(directory : str, dizionario : dict[str, int]) -> None:
    "cerco tutti i file '.txt' e ne ritorno le dimensioni"
    for nome in os.listdir(directory):
        # ignoro file e dir che iniziano per '.' oppure '_'
        if nome[0] in '_.': continue
        fullname = directory + '/' + nome
        # se sono nel caso ricorsivo
        if os.path.isdir(fullname):
            cerca_file_sizes2(fullname, dizionario)
        # altrimenti se Ã¨ un file che finisce con 'txt'
        elif nome.endswith('.txt'):
            size = os.path.getsize(fullname)
            dizionario[fullname] = size

D = {}
#cerca_file_sizes2(percorso, D)
#print(D)



"Mi costruisco una lista di valori casuali"
import random 
lista = random.choices(range(-10000,10001), k=10)

# Somma ricorsiva di una lista 
#   caso base: se la lista è vuota la somma è 0
#   se la lista non è vuota: somiamo il primo elemento alla somma del resto della lista
@trace()
def somma_ric(lista):
    if len(lista) == 0:
        return 0
    else:
        # primo elemento della lista, dentro a 'resto' metto tutti i restanti elementi della lista
        primo, *resto = lista 
        print(primo,resto)
        return primo + somma_ric(resto)

#somma = somma_ric.trace(lista)
#somma2 = sum(lista)
#print(somma, somma2, '\n')


@trace()
def somma_ric_distruttiva(L):
    if L:
        ultimo = L.pop()
        return ultimo + somma_ric_distruttiva(L)
    else:
        return 0

#somma3 = somma_ric_distruttiva.trace(lista)
#print(somma2, somma3, '\n')


def somma_iter(L):
    somma = 0
    for i in range(len(L)):
        somma += L[i]
    return somma

#devo rinizializzare la lista perchè nella funzione precedente la elimino
#print(somma_iter(lista))
       

"""
Somma ricorsiva in avanti (simulando il ciclo)
- le variabili di stato, somma, i ed N
    - diventano argomenti della funzione
    - ad ogni step le aggiorniamo nella chiamata ricorsiva
"""
@trace()
def _somma_ric_avanti(L:list[int], i:int, N:int, somma:int) -> int:
    if i==N:
        return somma
    else:
        return _somma_ric_avanti(L, i+1, N, somma + L[i]) # AGGIORNAMENTO

def somma_ric_avanti(L):
    return _somma_ric_avanti(L, 0, len(L), 0)

#print(somma_ric_avanti(lista))



"""
Stampa di una lista 
- in avanti (prima del passo ricorsivo)
- indietro  (dopo il passo ricorsivo)
- avanti poi indietro (prima e dopo)

Analisi:
- la lista vuota non stampa nulla (caso base)
- una volta stampato il primo elemento va stampato il resto (passo ricorsivo)
"""
# per scandire e stampare una lista in avanti
def stampa_in_avanti(L):
    if L:
        primo, *resto = L
        print(primo, end=' ')
        stampa_in_avanti(resto) 


#stampa_in_avanti(lista)
#print()
#print(lista)


# per scandire e stampare una lista a rovescio
def stampa_dalla_fine(L):
    if L:
        primo, *resto = L
        stampa_dalla_fine(resto)
        print(primo, end=' ')
        
#stampa_dalla_fine(lista)
#print()
#print(lista)


# per scandire una lista sia in avanti che a rovescio 
# basta stampare sia prima della ricorsione che dopo
def stampa_inizio_fine(L):
    if L:
        primo, *resto = L
        print(primo, end=' ')
        stampa_inizio_fine(resto)
        print(primo, end=' ')

#stampa_inizio_fine(lista)
#print()
#print(lista)



"""
MERGESORT (ordinamento per fusione)
Osservazione: se due liste sono ordinate è facile e veloce fonderle in una nuova lista ordinata
• per fondere due liste ordinate (merge)
    ▪ il primo elemento della soluzione è uno dei due primi delle due liste
    ▪ il resto della soluzione è la fusione del resto delle due liste
• convergenza: almeno un elemento va a posto per ogni chiamata ricorsiva
• caso base: una delle due liste è vuota
"""
@trace(True)

def merge(L1, L2):
    if not L1:      # caso base: L1 vuota
        return L2
    if not L2:      # caso base: L2 vuota
        return L1
    if L1[0] <= L2[0]:  # caso ricorsivo con L1[0] minore
        return [L1[0]] + merge(L1[1:], L2)
    else:               # caso ricorsivo con L2[0] minore
        return [L2[0]] + merge(L1, L2[1:])

L1 = [1, 15, 59, 76, 98]
L2 = [12, 19, 67, 88]
#mergef.trace(L1, L2)


"""
E se ho una lista disordinata e la voglio ordinare?
• la posso spezzare in due liste disordinate (riduzione)
• le posso ordinare separatamente (chiamata ricorsiva sui sottoproblemi)
• le posso fondere rapidamente (costruzione della soluzione) con merge
• convergenza: a forza di spezzare le liste in 2 si arriverà a liste di 0,1 elementi
• caso base: liste di 1 o 0 elementi, sono già ordinate
"""
L = [1, 5, 2, 9, 4, 6, 1, 90 ]
mid = len(L)//2
L1 = L[:mid]
L2 = L[mid:]
#print(L1, L2)


## oppure una funzione ricorsiva che torna due liste di elementi alternati
@trace()
def splitta(L):
    if not L:
        return [], []
    else:
        primo, *resto = L   # prendo il primo elemento ed il resto
        L1, L2 = splitta(resto)
        L2.append(primo)
        return L2, L1       # aggiungo il valore su una lista e le scambio 
    
#splitta.trace(L)



## Finalmente realizziamo mergeSort
@trace()
def merge_sort(L : list) -> list:
    if len(L) < 2: # [x] e [] sono già ordinate
        return L
    else:
        L1, L2 = splitta(L) # 2 sottoliste disordinate
        sorted1 = merge_sort(L1) # ordino la prima
        sorted2 = merge_sort(L2) # ordino la seconda
        return merge(sorted1, sorted2) # le fondo
    
#merge_sort.trace(L)



"""
Alberi Binari
- si parte da un nodo 'radice' che non ha più 'padri'
- ogni nodo può avere fino a 2 'figli'
- i nodi senza figli sono le 'foglie'
- ogni nodo ha un solo 'padre'
"""

import graphviz
T = graphviz.Digraph() 
T.body.append('''
 radice -> "nodo\n0" -> "nodo\n00" -> "foglia\n000"
 radice -> "nodo\n1" -> "nodo\n10" -> "foglia\n100"
 "nodo\n0" -> "nodo\n01" -> "foglia\n010"
 "nodo\n1" -> "nodo\n11" -> "foglia\n110"
 "nodo\n00" -> "foglia\n001"
 "nodo\n10" -> "foglia\n101"
 "nodo\n01" -> "foglia\n011"
 "nodo\n11" -> "foglia\n111"
''')
#print(T)



#                           A 
#                         /   \
#                        /     \
#                       /       \
#                      F         B
#                     / \         \
#                    Z   G         K
                   
                
# visita PREordine: a f z g b k
# visita POSTordina: z f g a b k
# visita INordine: z g f k b a


# usiamo gli oggetti per rappresentare i nodi dell'albero
class NodoBinario:
    def __init__(self,   V : int, 
                         left  : 'NodoBinario' = None, 
                         right : 'NodoBinario' = None):
        self._value = V
        self._sx = left
        self._dx = right
        
    def __repr__(self):
        return f'NodoBinario({self._value})'

n11 = NodoBinario(11)
n10 = NodoBinario(10)
n1 = NodoBinario(1, right=n11)
n0 = NodoBinario(0, left= n10)
r = NodoBinario(100, n0, n1)
#print(r)


"""
Stampa di un albero
con visita in PREordine (la radice PRIMA dei sottoalberi)
"""
# radice è un nodo oppure None
# per stampare indentato passo un argomento 'livello'
# e lo incremento ogni volta che scendo in un sottoalbero
def stampa_PRE(radice : NodoBinario, livello : int =0) -> None :
    print('|--'*livello, radice) 
    if radice:
        stampa_PRE(radice._sx, livello+1)
        stampa_PRE(radice._dx, livello+1)
        
#stampa_PRE(r)


"""
Stampa di un albero
con visita in POSTordine (la radice DOPO i sottoalberi)
"""
def stampa_POST(radice : NodoBinario, livello : int =0) -> None :
    if radice:
        stampa_POST(radice._sx, livello+1)
        stampa_POST(radice._dx, livello+1)
    print('|--'*livello, radice) 
        
#stampa_POST(r)


"""
Stampa di un albero
con visita iINordine (la radice TRA i sottoalberi)
"""
def stampa_IN(radice : NodoBinario, livello : int =0) -> None :
    if radice:
        stampa_IN(radice._sx, livello+1)
    print('|--'*livello, radice)
    if radice:
        stampa_IN(radice._dx, livello+1)
     
        
#stampa_IN(r)



"""
Calcolo della profondità/altezza di un albero (in uscita)
    • Una foglia ha altezza 1 (caso base)
    • un nodo ha altezza 1 + la massima altezza dei sottoalberi (passo ricorsivo + composizione)
Oppure:
    • None ha altezza 0
"""
@trace()
def altezza(radice):
    if radice is None:
        return 0
    H_sx = altezza(radice._sx)
    H_dx = altezza(radice._dx)
    return 1 + max(H_sx, H_dx)

#print(altezza.trace(r))


"""
Calcolo della profondità in "andata":
• si fornisce come argomento la profondità massima incontrata finora
• la si aggiorna visitando tutto l'albero
    ▪ (ogni volta che si scende in un sottoalbero si somma 1 alla profondità)
• se il nodo è None si torna la profondità corrente
• altrimenti il nodo esiste e la profondità è il massimo delle profondità dei due sottoalberi
"""
@trace()
def altezza2(radice, profondità=0):
    if radice is None:
        return profondità
    P_sx = altezza2(radice._sx, profondità+1)
    P_dx = altezza2(radice._dx, profondità+1)
    return max(P_sx, P_dx)

#print(altezza2.trace(r))



"""
Alberi N-ari (con numero indefinito di figli)
• value: valore del nodo
• sons: elenco di figli
"""


G3 = graphviz.Digraph() 
G3.body.append('''
 2 [color=green]
 19 [color=red]
 14 -> 11
 14 -> 12
 14 -> 2
 11 -> 19
 11 -> 13
 11 -> 3
 11 -> 4
''')
#print(G3)


# utility che mi permette di aggiungere con %%add_to dei metodi definiti in celle separ
import jdc
class NodoNario :
    
    def __init__(self, V:int, sons:list['NodoNario'] = None):
        # ATTENTI AL DEFAULT!!!
        self._value = V
        if sons is None:
            self._sons = []
        else:
            self._sons = sons

    def __repr__(self):
        return f"NodoNario({self._value}, {len(self._sons)} sons)"


    # stavolta scriviamo le funzioni come metodi della classe NodoNario
    
    """
    Altezza del nodo nell'albero(quanti livelli ha sotto)'
    • esploro l'albero ricorsivamente
    • l'altezza di un nodo è 1 + max altezza dei sottoalberi figli
    • l'altezza di una foglia è 0
    """

    # metodo per calcolare l'altezza del nodo
    def altezza(self):
        # se non ci sono figli si torna 0
        return max( [son.altezza()+1 for son in self._sons], default=1 )
    
    """
    Stampa (in preordine) di un nodo e dei figli
    • aggiungo un argomento livello che incremento ogni volta che scendo
    • prima stampo il nodo indentato del livello corrente
    • poi stampo ricorsivamente i sottoalberi con livello+1
    """
    # metodo per stampare l'albero
    def stampa(self, livello=0):
        indent = '|--'*livello
        print(indent, self)
        for son in self._sons:
            son.stampa(livello+1)

    """
    Cerchiamo il massimo valore nell'albero
    • esploriamo ricorsivamente
    • il valore massimo di un sottoalbero è il massimo tra il valore della 
        radice ed i valori dei sottoalbero
    """
    # versione in stile non-funzionale
    def massimo(self):
        M = self._value
        for s in self._sons:
            m = s.massimo()
            if M < m:
                M = m
        return M

    # versione in stile funzionale
    def massimo2(self):
        return max([s.massimo2() for s in self._sons] + [self._value])

    # versione che porta il massimo come argomento
    # da aggiornare mano a mano che si esplora l'albero
    def massimo3(self, max_corrente=None):
        if max_corrente is None:
            max_corrente = self._value
        else:
            max_corrente = max(max_corrente, self._value)
        for son in self._sons:
            max_corrente = son.massimo3(max_corrente)
        return max_corrente


    """
    Cerchiamo il nodo con massimo valore
    - esploriamo ricorsivamente
    - il nodo massimo di un sottoalbero è il nodo che contiene il massimo tra 
        il valore della radice ed i valori dei sottoalberi
    """
    def max_node(self):
        M = [self] + [s.max_node() for s in self._sons]
        #print(M)
        return max(M, key=lambda x: x._value)
    
    def min_node(self):
        M = [self] + [s.min_node() for s in self._sons]
        #print(M)
        return min(M, key=lambda x: x._value)
        
    """
    Cerchiamo la differenza in altezza tra nodo con valore massimo e 
        nodo con valore minimo
    """
    def depth_of_max(self,livello=0):
        M = [(self._value, livello)] + [ son.depth_of_max(livello+1)
                                        for son in self._sons]
        return max(M, key=lambda x: x[0])
    
    def depth_of_max2(self,livello=0):
        M = self._value
        P = livello
        for son in self._sons:
            m,p = son.depth_of_max2(livello+1)
            if m > M:
                M = m
                P = p
        return M, P
    
    def depth_of_min(self,livello=0):
        M = [(self._value, livello)] + [ son.depth_of_min(livello+1) 
                                        for son in self._sons]
        return min(M, key=lambda x: x[0])


# Esempi
n19 = NodoNario(19)
n2 = NodoNario(2)
n3 = NodoNario(3)
n4 = NodoNario(4)
n13 = NodoNario(13)
n12 = NodoNario(12)
n11 = NodoNario(11, [n3, n4, n13, n19])
n14 = NodoNario(14, [n2, n11, n12])

#n14.altezza()

#n14.stampa()

#n14.massimo()
#n14.massimo2()
#n14.massimo3()

#n14.max_node(), n14.min_node()

#n14.depth_of_max(), n14.depth_of_min()
















