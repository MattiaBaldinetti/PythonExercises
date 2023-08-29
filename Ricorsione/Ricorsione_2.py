# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 17:02:30 2023

@author: UtentePC
"""

from rtrace import trace

# mi costruisco una lista di valori casuali
import random, graphviz
lista = random.choices(range(-10000,10000), k=10)


class NodoBinario:
    
    def __init__(self, V:int, sx:'NodoBinario'=None, dx:'NodoBinario'=None):
        self._value = V
        self._sx = sx
        self._dx = dx
        
    def __repr__(self):
        return f"\"{self._value}\n{getattr(self,'_altezza','')}\n{getattr(self,'_percorso','')}\""

    def _dot(self):
        "creo l'elenco di nodi ed archi che Graphivz sa visualizzare"
        s = f'{self}\n'
        if self._sx and self._dx:
            s += f'{{rank=same ; {self._sx} ; {self._dx} }}\n'
        if self._sx:
            s += f'{self} -> {self._sx}\n'
            s += self._sx._dot()
        if self._dx:
            s += f'{self} -> {self._dx}\n'
            s += self._dx._dot()
        return s

    def show(self):
        "creo l'oggetto Digraph per visualizzare il grafo diretto"
        G = graphviz.Digraph() 
        G.body.append('rankdir=LR\n' + self._dot())
        return G
        
n1= NodoBinario(1)
n2= NodoBinario(2, dx=n1)
n3= NodoBinario(3)
n4= NodoBinario(4)
n5= NodoBinario(5, dx=n2)
n6= NodoBinario(6, dx=n5)
n7= NodoBinario(7, n4, n3)
n8= NodoBinario(8, n6)
r= NodoBinario(9, n8, n7)
#r.show()


"""
DIAMETRODI UN ALBERO
(lunghezza del percorso più lungo)
"""


# CASO 1: il percorso passa per la radice
# il diametro è la somma delle due profondità massime dei sotto alberi + 2
G = graphviz.Digraph() 
G.body.append(''' rankdir=LR
 A -> B -> C -> D -> E [style=bold color=red]
 A -> F -> G -> H -> I [style=bold color=red]
 B -> J -> K
 F -> L -> O
 G -> M
 J -> N
''') 
# print("DIAMETRO: 8 archi (9 nodi)")


# CASO 2: il percorso NON passa per la radice
# il diametro è il più grande valore calcolato per ciascun nodo dell'albero
G2 = graphviz.Digraph() 
G2.body.append(''' rankdir=LR
 B -> C -> D -> E [style=bold color=red]
 B -> F -> G -> H -> I [style=bold color=red]
 A -> B
 C -> J
 F -> L -> O
 G -> M
''')
# print('DIAMETRO: 7 archi (8 nodi)')



# CASO 3: il percorso NON si biforca
# il diametro è la profondità massima dell'albero
G3 = graphviz.Digraph() 
G3.body.append(''' rankdir=LR
 A -> B -> C -> D -> E -> F -> G -> H -> I [style=bold color=red]
 C -> J
 F -> L -> O
 G -> M
''')
# print("DIAMETRO 8 archi (9 nodi)")


### I 3 STEP PROBABILMENTE DEVONO FAR PARTE DELLA class NodoBinario
"""
Step 1: calcolare le altezze di tutti i sottoalberi
- visita ricorsiva
- visto che vogliamo l'altezza del nodo conviene lavorare in uscita dalla ricorsione
""" 
   
def aggiungi_altezze(root) -> int :
    if root is None:
        return 0
    A_sx = aggiungi_altezze(root._sx)
    A_dx = aggiungi_altezze(root._dx)
    root._altezza = max(A_sx, A_dx) +1
    return root._altezza

#aggiungi_altezze(r)
#r.show()
    
    
"STEP 2: calcolare i percorsi supponendo che passino per ciascun nodo come radice"      
def aggiungi_percorsi(radice):
    "a ciascun nodo aggiungo l'attributo _percorso se passasse per quel nodo come radice"
    if radice is not None:
        A_sx = A_dx = 0
    if radice._sx:
        A_sx = radice._sx._altezza
    if radice._dx:
        A_dx = radice._dx._altezza
    radice._percorso = A_sx + A_dx + 1
    aggiungi_percorsi(radice._sx)
    aggiungi_percorsi(radice._dx)
    
    
"STEP 3: cercare il nodo col valore massimo di percorso o altezza"
def diametro(radice):
    if not radice:
        return 0
    D_sx = diametro(radice._sx)
    D_dx = diametro(radice._dx)
    return max(D_sx, D_dx, radice._percorso, radice._altezza)
 
# print(diametro(r)) # 8
#r.show()   
   

 

    



# ALBERI DI GIOCO (simulazione di tutte le possibili partite)
# Per capire come funziona un gioco o per definire delle strategie vincenti 
#    possiamo costruire tutte le possibili evoluzioni del gioco a partire 
#    dalla configurazione iniziale
# • data una configurazione iniziale ed il giocatore di turno
# • se il gioco è terminato calcoliamo chi ha vinto o se è patta
# • altrimenti individuiamo le mosse applicabili
# • proviamo ad applicare una mossa
# • ci troveremo in una nuova configurazione
# • ripetiamo ricorsivamente ad esplorare le nuove configurazioni finchè è possibile
# • se non ci sono più possibili configurazioni passiamo a provare la prossima mossa


"""
GIOCO: somma di coppie consecutive pari o dispari
- configurazione: una sequenza di interi
- mosse possibili: sommare una coppia di numeri consecutivi pari+pari o dispari+dispari
- terminazione: non ci sono più coppie pari,pari o dispari,dispari

Convergenza: ad ogni passo il numero di elementi diminuisce di 1
Caso base: numeri laternati o lista di un solo elemento
GOAL: trovare tutte le sequenze finali  


Esempio:
[ 1, 13, 2, 7, 9, 2 ]
• [1, 13, 2, 7, 9, 2]->[14, 2, 7, 9, 2]->[16, 7, 9, 2]->[16, 16, 2]->[32, 2]->[34]
• [1, 13, 2, 7, 9, 2]->[1, 13, 2, 16, 2]->[1, 13, 2, 18]->[1, 13, 20]->[14, 20]->[34]   
"""
import graphviz

class GameNode:
    _num_nodi = 0
    
    def __init__(self):
        self.__class__._num_nodi += 1
        self.__id = self.__class__._num_nodi
    
    def dot(self):
        "Costruisco la rappresentazione dell'albero da visualizzare con Graphviz"
        if self._sons:
            s = f'{self.__id} [label={self}]\n' # se non foglia colore nero
        else:
            s = f'{self.__id} [label={self} color=red, style=bold, shape=box] \n' # coloro le foglie di rosso
        for son in self._sons:
            s += f'{self.__id} -> {son.__id}\n' # archi padre -> figlio
            s += son.dot()
        return s
    
    def show(self):
        "Creo l'oggetto Digraph che visualizza il grafo diretto"
        G = graphviz.Digraph() 
        G.body.append('rankdir=LR\n' + self.dot())
        return G          
        
import jdc
# configurazione: lista di valori + figli

class Sequenza(GameNode):
    
    def __init__(self, lista : list[int]):
        super().__init__()
        "Una configurazione contiene la lista di interi"
        self._lista = lista
        self._sons = []
    
    def __repr__(self):
        "Visualizzo la lista"
        return f'"{self._lista}"'
        
        
    """
    S = Sequenza([1, 13, 2, 7, 9, 2])
    S.show()       
    """   
    
    # Mosse valide: tutte le coppie pari o dispari
    # • per ogni possibile posizione i
    #    ▪ la torniamo se i due valori hanno stesso resto diviso 2
    
    def mosse_valide(self):
        "elenco di tutte le posizioni i,i+1 che possono essere sommate"
        return [ i for i in range(len(self._lista)-1)
                # mossa valida se resti uguali (pari+pari o dispari+dispari)
                if self._lista[i]%2 == self._lista[i+1]%2 ] 
    
    """            
    print(S)
    S.mosse_valide()    # [0, 3]
    """
        
    
    # Applicare la mossa vuol dire creare una nuova sequenza
    # - basta sostituire i valori in posizioni i e i+1 con la somma
    
    def applica_mossa(self, i):
        "applico una mossa creando il nodo figlio ed aggiungendolo ai figli"
        nuova_lista = self._lista.copy() # copio la sequenza per non modificarla
        
        # rimpiazzo i due valori con la loro somma usando un assegnamento a slice
        #nuova_lista[i:i+2] = [nuova_lista[i] + nuova_lista[i+1]]
        
        N1 = nuova_lista.pop(i)
        N2 = nuova_lista.pop(i)
        nuova_lista.insert(i, N1 + N2)
        # creo il nuovo nodo e lo aggiungo ai figli
        self._sons.append(Sequenza(nuova_lista))

    """       
    S.applica_mossa(0)
    S.show()    # [14, 2, 7, 9, 2]
    """             
            
    # Generazione di tutto l'albero
    # - per ogni mossa possibile generiamo il nuovo figlio
    # - per ogni figlio generiamo le prossime mosse
        
    def genera(self):
        "applicazione delle mosse valide e generazione dei sottoalberi"
        for i in self.mosse_valide():
            self.applica_mossa(i)
        for son in self._sons:
            son.genera()   

    """        
    S = Sequenza([ 1, 13, 2, 7, 9, 2 ])
    S.genera()
    S.show()
    
    B = Sequenza([2, 7, 9, 3, 5, 4])
    B.genera()
    B.show()
    """
       

    #Trovare la giocata più corta
    # basta cercare la **foglia con profondità  minima dell'albero
    def shortest(self): 
        "minima altezza, ovvero distanza della foglia più vicina dalla radice"
        if not self._sons:
            return 0
        else:
            return min( son.shortest() for son in self._sons ) + 1
    
    #Trovare la giocata più lunga
    # basta cercare la foglia con profondità  massima dell'albero
    def tallest(self): 
        "massima altezza, ovvero distanza della foglia più lontana dalla radice"
        if not self._sons:
            return 0
        else:
            return max( son.tallest() for son in self._sons ) + 1

    # B.shortest(), B.tallest()      
    
    
    """
    Per trovare la foglia più alta/bassa
    • dobbiamo ricordare il nodo assieme alla sua profondità
    """
    def tallest_leaf(self):
        "massima altezza E foglia che gli corrisponde"
        if not self._sons:      # se sono una foglia
            return 0, self      # torno 1 e me stessa
        else:
            # altrimenti calcolo le distanze massime per ciascun figlio
            altezze_figli = [ son.tallest_leaf() for son in self._sons ]
            # e tra queste prendo la coppia massima con la foglia corrispondente
            massimo, nodo = max(altezze_figli, key=lambda coppia: coppia[0])
            # torno la distanza massima +1 E quella foglia
            return massimo + 1, nodo

    def shortest_leaf(self):
        "minima altezza e foglia che la produce"
        if not self._sons:
            return 0, self
        else:
            altezze_figli = [ son.shortest_leaf() for son in self._sons ]
            minimo, nodo = min(altezze_figli, key=lambda coppia: coppia[0])
            return minimo + 1, nodo
                

    # B.tallest_leaf(), B.shortest_leaf() 
    # ((5, "[30]")    ,(1, "[2, 7, 12, 5, 4]"))
        
        
        
        
        
        
        
              
        
        
        
        
        
        
        
        