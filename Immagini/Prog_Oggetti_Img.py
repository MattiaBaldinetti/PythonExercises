# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 18:21:02 2023

@author: UtentePC
"""


"""
PROGRAMMAZIONE AD OGGETTI

• Gli oggetti sono la fusione di:
    ▪ attributi: i dati che caratterizzano una particolare entità
    (per esempio un cane ha un peso, un nome, un genere, una età, un colore ...)

    ▪ metodi: le funzionalità caratteristiche quella particolare entità
    (un cane abbaia, si muove, scodinzola, mangia, morde, si accoppia ...)

La descrizione di una tipologia di oggetto si chiama classe (i Cani)
Ciascun individuo di una certa tipologia si chiama istanza della classe
Abbiamo usato ampiamente gli oggetti (str, int, dict, tuple, float, bool ...) e i loro metodi
"""



"""
COME DEFINIRE UN NUOVO TIPO DI OGGETTO

class NomeDellaClasse (EstendendoLaClasse):
        attributi_di_classe = valore    #valore condivisi tra tutte le istanze/individui
        
        
        def __init__(self, <arogmenti>):    #metodo speciale che inizializza l'istanza
            self.attributo_individuale = valore1    #definisco un valore personale di un individuo/istanza
        
        def metodo1(self, <argomenti>):     #comportamenti di tutti gli individui
            corpo del metodo

"""




"""
TRASFORMIAMO I COLORI IN OGGETTO
Per poter (ri)scrivere le trasformazioni che abbiamo fatto sui colori come espressioni semplici
Per esempio:
    • luminosità(colore, k) diventa colore*k
    • contrasto(colore,k) diventa (colore-grigio)*k + grigio
Come?
    • basta ridefinire i metodi che realizzano le operazioni matematiche ( __add__ , __mul__ , ...)
    • così definiamo una matematica dei colori
"""


# libreria che permette di definire una classe spezzata in più celle Jupyter
import jdc
# ATTENZIONE: nella realtà i metodi devono essere INDENTATI dentro la classe


class Colore:
    # definisco un elenco di colori standard,ma li creiamo dopo
    black : 'Colore'    # i tipi li metto come stringa perchè
    white : 'Colore'    # la classe Colore non è ancora
    red   : 'Colore'      # completamente definita
    green : 'Colore'
    blue  : 'Colore'
    cyan : 'Colore'
    yellow : 'Colore'
    purple : 'Colore'
    grey : 'Colore'
    
    
    def __init__(self, R:float, G:float, B:float):
        "un colore contiene i tre canali R, G, B"
        self._R = R
        self._G = G
        self._B = B
        
    # N.B: tutti i metodi devono essere indentati dentro la classe

#A = Colore(123,234,12)
#print(A._R) #123
    

    # Poi (ri)definiamo somma e differenza ( __add__ e __sub__ )
    def __add__(self, other:'Colore'):
        "somma tra due colori"
        assert type(other) == Colore, "Il secondo argomento non è un Colore"
        return Colore(self._R+other._R, self._G+other._G, self._B+other._B )
    
    def __sub__(self, other:'Colore'):
        "differenza tra due colori"
        assert type(other) == Colore, "Il secondo argomento non è un Colore"
        return Colore(self._R-other._R, self._G-other._G, self._B-other._B )
    
    
    # e prodotto o divisione per una costante K ( __mul__ e __truediv__ )
    def __mul__(self, k:float):
        "moltiplicazione di un colore per una costante"
        return Colore(self._R*k, self._G*k, self._B*k)
    
    def __truediv__(self, k:float):
        "divisione di un colore per una costante"
        return Colore(self._R/k, self._G/k, self._B/k)
    
    
    # un paio di metodi di comodo
        # conversione da colore a tripla (per poi salvare i file con images.save)
        # visualizzazione del colore come stringa (__repr__ oppure __str__)
    def _asTriple(self):
        "creo la tripla di interi tra 0 e 255 che serve per le immagini PNG"
        def bound(C):
            return min(255,max(0, int(round(C))))
        return bound(self._R), bound(self._G), bound(self._B)
    
    def __repr__(self):
        "stringa che deve essere visualizzata per stampare il colore"
        return f"Colore({self._R},{self._G},{self._B})"
        
    
    # luminosità media
    def luminosità(self):
        "calcola la luminosità media di un pixel (senza badare se è un valore intero)"
        return Colore(self._R + self._G + self._B)/3
    
    
    # grigio
    def grigio(self):
        "creo un colore grigio con la stessa luminosità"
        L = self.luminosità()
        return Colore(L,L,L)

    # negativo
    def negativo(self):
        "ottengo il colore inverso"
        return Colore.white - self
    
    # illumina
    def illumina(self, k:float):
        "ottengo il colore schiarito/scurito di un fattore k"
        return self*k
    
    # contrasto
    def contrasto(self, k:float):
        "ottengo il colore allontanato/avvicinato di un fattore k dal grigio"
        return Colore.grey + (self - Colore.grey) * k
    
    
# solo dopo che ho definito la classe Color posso definire dei colori
# posso aggiungerle degli *attributi di classe*
# che contengono *istanze di Color*
# ad esempio alcuni colori standard

# NON INDENTATO SOTTO Colore
Colore.white = Colore(255, 255, 255)
Colore.black = Colore( 0, 0, 0)
Colore.red = Colore(255, 0, 0)
Colore.green = Colore( 0, 255, 0)
Colore.blue = Colore( 0, 0, 255)
Colore.yellow = Colore(255, 255, 0)
Colore.purple = Colore(255, 0, 255)
Colore.cyan = Colore( 0, 255, 255)
Colore.grey = Colore.white / 2      # STO USANDO __truediv__ !!!

#print(Colore.grey) 
    

"""
ESEMPI
"""
rosso = Colore(255, 0, 0)
verde = Colore(0, 255, 0)

p3 = rosso + verde  # uso loperatore tra due colori che ho definito
#print(p3)

p4 = p3 *0.5    # uso l'operatore per una costante che ho definito
#print(p4)

# media di 4 colori
LC = [rosso, verde, p3, p4]
media = sum(LC, Colore.black) / len(LC)
#print(media)

C = Colore(56, 200, 31)
#print(C)

ill = C.illumina(0.8)
#print(ill)

contr = C.contrasto(1.5)
#print(contr)

colore = Colore.contrasto(C, 0.8)
#print(colore)

#%%%%
"""
DEFINIZIAMO ORA UNA CLASSE Immagine
• che contiene una lista di liste di Colore invece che di triple RGB
• e magari anche le proprie dimensioni
• che sa applicare filtri semplici o filtri XY
• che posso caricare da un file
• che posso salvare su un file
• sulla quale posso disegnare (line, pixel, rectangle ...)

COMINCIO CON CLASSE E COSTRUTTORE __init__
Posso creare una immagine in due modi:
    • leggendola da un file PNG e convertendo le triple in Color
    • o fornendo dimensioni e colore di sfondo
in entrambi i casi mi segno le dimensioni una volta per tutte
"""

import images
from math import dist
from typing import Optional, Callable

class Immagine:
    
    def __init__(self,   larghezza: Optional[int] = None,
                         altezza:   Optional[int] = None,
                         sfondo:    Optional[int] = None,
                         filename: Optional[int] = None):
        
        if filename: # leggo l' immagine e la converto in una matrice di Colore 
            img = images.load(filename)
            self._img = [ [Colore(R,G,B) for R,G,B in riga] for riga in img]
            self._H = len(img)
            self._W = len(img[0])
        else: #altrimenti creo un immagine monocolore e ne ricordo le dimnesioni
            self._W = larghezza
            self._H = altezza
            self._img = [ [sfondo for _ in range(larghezza)]
                                  for _ in range(altezza) 
                        ]


    """
    Definisco un paio di metodi di utilità
    • visualizzazione della immagine come stringa ( __repr__ )
    • salvataggio su file
    • conversione da Colori a triple
    • visualizzazione in Spyder/Jupyter/Ipython
    """


    def __repr__(self):
        "per stampare l'immagine ne mostro solo le dimensioni"
        return f"Immagine({self._W}x{self._H})"
    
    def save(self, filename: str):
        "si salva l'immagine dopo averla convertita in matrice di triple"
        images.save(self._asTriples(), filename)
        return self
    
    #metodo privato, inizia per _
    def _asTriples(self):
        "conversione dell' immagine da matrice di Colore a matrice di triple"
        return [ [c._asTriple() for c in riga]
                                for riga in self._img ]
    
    def visualizza(self):
        "visualizza l'immagine in Spyder / Jupyter"
        return images.visd(self._asTriples())
    
#trecime = Immagine(filename='3cime.png')
#trecime.visualizza()


    def set_pixel(self, x: float, y: float, color : Colore) -> 'Immagine': # cambio il pix
        "cambio un pixel se è dentro l'immagine"
        x = int(round(x)) # float -> int
        y = int(round(y)) # float -> int
        if 0 <= x < self._W and 0 <= y <= self._H:
            self._img[y][x] = color
        return self

    def get_pixel(self, x: float, y: float): # leggo il pixel più vicino 
        "leggo un pixel se è dentro l'immagine oppure torno il più vicino sul bordo"
        x = int(round(x)) # float -> int
        y = int(round(y)) # float -> int
        x = min(self._W-1, max(0, x))
        y = min(self._H-1, max(0, y))
        return self._img[y][x]
    

    """
    Metodi per disegnare linee
     - orizzontale
     - verticale
     - inclinata (qualsiasi)
    """

    def draw_line_H(self, x: int, y: int, x1: int, color: Colore) -> 'Immagine': 
        "disegno una linea orizzontale"
        x,x1 = min(x,x1),max(x,x1)
        for X in range(x, x1+1):
            self.set_pixel(X,y, color)
        return self

    def draw_line_V(self, x: int, y: int, y1: int, color: Colore) -> 'Immagine': 
        "disegno una linea verticale"
        y,y1 = min(y,y1),max(y,y1)
        for Y in range(y, y1+1):
            self.set_pixel(x,Y, color)
        return self
        
    def draw_line(self, x1: int,y1: int, x2:int,y2:int, color: Colore) -> 'Immagine':
        "disegno una linea qualsiasi"
        dx = x1 - x2
        dy = y1 - y2
        if dx == 0: # se dx=0 mi muovo in verticale
            self.draw_line_V(x1,y1,y2) 
        elif dy == 0: # se dy=0 mi muovo in orizzontale
            self.draw_line_H(x1,y1,x2) 
        elif abs(dx) > abs(dy): # se dx più grande itero sulle X
            m = dy/dx
            # FIXME: direzione da x1 a x2
            for X in range(x1,x2+1):
                Y = m*(X-x1) + y1
                self.set_pixel(X,Y,color)
        else: # altrimenti sulle Y
            m = dx/dy
            # FIXME: direzione da y1 a y2
            for Y in range(y1,y2+1):
                X = m*(Y-y1) + x1
                self.set_pixel(X,Y,color)
        return self


    """
    Metodi per disegnare figure
        • rettangoli vuoti o pieni
        • triangoli vuoti
        • poligoni regolari
        • ellissi e cerchi
    """
    
    # rettangolo pieno
    def draw_rectangle_full(self, x: int, y: int, x1: int, y1: int, color: Colore) -> 'Immagine':   
        "disegno un rettangolo pieno disegnando tante linee orizzontali"
        for Y in range(y, y1+1):
            self.draw_line_H(x,Y,x1, color)
        return self
    
    # rettangolo
    def draw_rectangle(self, x: int, y: int, x1: int, y1: int, color: Colore) -> 'Immagine':  
        "disegno un rettangolo vuoto (4 linee)"
        self.draw_line_H(x ,y ,x1,color)
        self.draw_line_H(x ,y1,x1,color)
        self.draw_line_V(x ,y ,y1,color)
        self.draw_line_V(x1,y ,y1,color)
        return self
    
    def draw_ellipse_full(self, x1: int,y1: int, x2: int,y2: int, D: int, color: Colore ) -> 'Immagine':
        "una ellisse piena"
        for x in range(self._W):
            for y in range(self._H):
                D1 = dist((x,y),(x1,y1))
                D2 = dist((x,y),(x2,y2))
                if D1+D2 < D:
                    self.set_pixel(x,y,color)
        return self
    
    def draw_ellipse(self, x1: int,y1: int, x2: int,y2: int, D: int, color: Colore ) -> 'Immagine':
        "una ellisse vuota"
        for x in range(self._W):
            for y in range(self._H):
                D1 = dist((x,y),(x1,y1))
                D2 = dist((x,y),(x2,y2))
                if D1+D2 - D < 1:
                    self.set_pixel(x,y,color)
        return self
    
    def draw_circle_full(self, xc: int, yc: int, r: int, color: Colore) -> 'Immagine':
        "un cerchio Ã¨ una ellisse con i due fuochi coincidenti e D=2*r"
        return self.draw_ellipse_full(xc, yc, xc, yc, 2*r, color)
    
    def draw_circle(self, xc: int, yc: int, r: int, color: Colore) -> None:
        "un cerchio Ã¨ una ellisse con i due fuochi coincidenti e D=2*r"
        return self.draw_ellipse(xc, yc, xc, yc, 2*r, color)


    """
    Meccanismi per applicare un filtro
    • applica_filtro (solo al singolo pixel)
    • applica_filtro_XY (per filtri che devono conoscere la posizione)
    """
    
    def applica_filtro(self, filtro : Callable[[Colore], Colore]) -> 'Immagine':
        "creo una nuova immagine applicando a tutti i pixel il filtro"
        nuova = Immagine(self._W, self._H, Colore.black)
        for y,riga in enumerate(self._img):
            for x,pixel in enumerate(riga):
                nuova._img[y][x] = filtro(pixel)
        return nuova

    def applica_filtro_XY(self, filtro : Callable[[int, int, 'Immagine'], Colore]) -> 'Immagine':
        "creo una nuova immagine applicando a tutti i pixel il filtro XY"
        # non c'Ã¨ bisogno di passare W,H perchÃ¨ sono giÃ  nella immagine
        nuova = Immagine(self._W, self._H, Colore.black)
        for y in range(self._H):
            for x in range(self._W):
                nuova._img[y][x] = filtro(x,y,self)
        return nuova
  
    
 
# ESEMPI
img = Immagine(larghezza=50, altezza=100, sfondo=Colore.red)
img.visualizza()
img.draw_circle(10,60, 10, Colore.green).visualizza()


A = Immagine(filename='3cime.png')
A.visualizza()

A.draw_ellipse(50,50, 100, 100, 100, Colore.red)
A.visualizza()

A.draw_rectangle(20,60, 100, 80, Colore.green) 
A.visualizza()

A.draw_circle(-20,60, 100, Colore.green) 
A.visualizza()

    
#%%%%

# per pixellare una immagine su una dimensione S
def pixella(x : int,y : int, I : 'Immagine', S : int):
    X = x - x%S + S//2
    Y = y - y%S + S//2
    return I.get_pixel(X,Y)   # se sbordo ci pensa da solo

def pixella10(x,y,I):    # potremmo definire una funziona ad hoc
    return pixella(x,y,I,10)


# oppure usare una lambda
A.applica_filtro_XY(lambda x,y,I: pixella(x,y,I,10)).visualizza()

    
from random import randint
    
def rumore(x, y, I, k): # leggo un pixel a caso nell'intorno [-k, k]
    "sostituisco il pixel con un vicino"
    X = x + randint(-k,k)
    Y = y + randint(-k,k)
    return I.get_pixel(X,Y)
    
A.applica_filtro_XY(lambda x,y,I: rumore(x,y,I,5)).visualizza()


#%%%%

# per aggiungere rumore casuale ad una immagine
    # possiamo aggiungere a ciascun pixel un piccolo valore random (filtro locale)


# %%%% lens slideshow={"slide_type": "subslide"}
# per dare l'effetto lente
    # nella zona della lente
    # mettiamo dei pixel che stanno a distanza K volte 
    # quella che si ha dal centro della lente

# %%
# TODO: generalizzare le operazioni di disegno

# Definiamo una classe FiguraGeometrica con i metodi (da specializzare)
    # draw(x, y, Immagine) che usa SOLO Immagine.set_pixel
    # area()               che ne calcola l'area
    # ...
    
# Definiamo le figure
    # Punto
    # Linea
    # Rettangolo
    # Triangolo
    # PoligonoRegolare
        # Quadrato
        # TriangoloEquilatero
        # Pentagono
    # Ellisse
        # Cerchio    




































































































































































