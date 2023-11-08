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


import images
from random import randint

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
    

    # Può far comodo avere un secondo costruttore che genera colori casuali
    @classmethod 
    def random(cls, m:int=0, M:int=0) -> 'Colore':
        "torna il colore con i valori delle luminosità in [m...M]"
        return cls(randint(m,M), randint(m,M), randint(m,M))

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
            "solo quando devo creare un file PNG mi assicuro che il pixel sia intero nel range 0..255"
            return min(255,max(0, int(round(C))))
        return bound(self._R), bound(self._G), bound(self._B)
    
    def __repr__(self):
        "stringa che deve essere visualizzata per stampare il colore"
        return f"Colore({self._R},{self._G},{self._B})"
        
    
    # luminosità media
    def luminosità(self):
        "calcola la luminosità media di un pixel (senza badare se è un valore intero)"
        return (self._R + self._G + self._B)/3
    
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


# Esempi
p1 = Colore(255, 0, 0)
p2 = Colore( 0,255, 0)
#print(p1, p2) 

p3 = p2 + p1 # uso l'operatore somma tra due colori che ho definito sopra
#print(p3)

p4 = p3 * 0.5 # uso l'operatore prodotto per una costante che ho definito sopra
#print(p4)

p5 = Colore(120, 34, 200)
#print(p5)





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
            if sfondo is None:
                sfondo = Colore.black
            self._W = larghezza
            self._H = altezza
            self._img = [ [sfondo for _ in range(larghezza)]
                                  for _ in range(altezza)]


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
        return [ [pixel._asTriple() for pixel in riga]
                                    for riga in self._img ]
    
    def is_inside(self, x : float, y : float) -> bool:
        "verifico se le coordinate x,y sono dentro l'immagine"
        return 0 <= x < self._W and 0 <= y < self._H
    
    def get_pixel(self, x: float, y: float): # leggo il pixel più vicino 
        "leggo un pixel se è dentro l'immagine oppure torno il più vicino sul bordo"
        x = int(round(x)) # float -> int
        y = int(round(y)) # float -> int
        x = min(self._W-1, max(0, x))
        y = min(self._H-1, max(0, y))
        return self._img[y][x]
    
    def set_pixel(self, x : float, y : float, color) -> None:
        "cambio un pixel se Ã¨ dentro l'immagine"
        x = round(x)
        y = round(y)
        if 0 <= x < self._W and 0 <= y < self._H:
            self._img[y][x] = color
    
    # fa comodo poter trovare i colori intorno ad un punto, fino a distanza k
    def vicini(self, x : int, y : int, k : int) -> list[Colore]:
        "torno i colori nei pixel 2k x 2k intorno al punto x,y"
        return [ self.get_pixel(X,Y)    for X in range(x-k,x+k+1)
                                        for Y in range(y-k,y+k+1)
                                        if self.is_inside(X,Y)  ]

    def visualizza(self):
        "visualizza l'immagine in Spyder / Jupyter"
        return images.visd(self._asTriples())
    
#trecime = Immagine(filename='3cime.png')
#trecime.visualizza()


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
#img.visualizza()
#img.draw_circle(10,60, 10, Colore.green).visualizza()


A = Immagine(filename='3cime.png')
#A.visualizza()

A.draw_ellipse(50,50, 100, 100, 100, Colore.red)
#A.visualizza()

A.draw_rectangle(20,60, 100, 80, Colore.green) 
#A.visualizza()

A.draw_circle(-20,60, 100, Colore.green) 
#A.visualizza()



 

"""
Definiamo il FILTRO  GENERICO e poi lo specializziamo aggiungendo funzionalità 
 - nell' __init__ riceve tutti i parametri che gli serviranno
 - ha un metodo nuovo_pixel(self, pixel) per i filtri che non dipendono dalla posizione
 - ha un metodo nuovo_pixel(self, immagine, x, y) per i filtri che dipendono dalla posizione
 - ha un metodo reset(self) per azzerarlo ed usarlo su altre immagini
 - ha il metodo applica(self, immagine)
"""
class GenericFilter: # tutti i filtri specializzano questa classe
    
    def nuovo_pixel(self, pixel : Colore) -> Colore :
        raise NotImplementedError()
    
    def nuovo_pixel_XY(self, immagine : Immagine, x : int, y : int) -> Colore :
        raise NotImplementedError()

    def reset(self) -> None :
        raise NotImplementedError()

    def applica(self, immagine : Immagine) -> Immagine:
        raise NotImplementedError()


class FiltroPixel(GenericFilter): # tutti i filtri indipendenti dalla posizione
    "un filtro che NON dipende dalla posizione del pixel"
    
    # applicazione di un filtro per ottenere una nuova immagine
    def applica(self, immagine : Immagine) -> Immagine:
        "costruisco una nuova immagine con ciascun pixel trasformato tramite il filtro"
        assert isinstance(immagine, Immagine), f"l'oggetto {immagine} non è una Immagine"
        nuova_immagine = Immagine(larghezza=immagine._W, altezza=immagine._H)
        for y,riga in enumerate(immagine._img):
            for x,pixel in enumerate(riga):
                nuova_immagine._img[y][x] = self.nuovo_pixel(pixel)
        return nuova_immagine
    
    def nuovo_pixel(self, pixel : Colore ) -> Colore:
        "trasformazione nulla di un pixel"
        return pixel  # per default ritorno lo stesso pixel
 

class FiltroXY (GenericFilter):    # tutti i filtri dipendenti dalla posizione
    "un filtro che DIPENDE dalla posizione del pixel"
    
    def applica(self, immagine : Immagine) -> Immagine:
        "applicazione di un filtro che conosce la posizione del pixel"
        assert isinstance(immagine, Immagine), f"{immagine} non è una Immagine"
        nuova_immagine = Immagine(larghezza=immagine._W, altezza=immagine._H)
        self.reset()   # se il filtro contiene info da usi precedenti le azzero
        for y in range(immagine._H):
            for x in range(immagine._W):
                nuova_immagine._img[y][x] = self.nuovo_pixel_XY(immagine,x,y)
        return nuova_immagine
    
    def nuovo_pixel_XY(self, immagine : Immagine, x : int, y : int) -> Colore :
        "trasformazione nulla di un pixel a coordinate x, y"
        return immagine.get_pixel(x,y)     # per default ritorno lo stesso pixel
    
    def reset(self) -> None:  # per default non faccio nulla
        pass 
  
 
"""
VISUALIZZAZIONE DI UN ALBERO CON I SEGUENTI COLLEGAMENTI   
import graphviz
figura = graphviz.Digraph()
figura.body.append('''
        GenericFilter -> FiltroPixel
        GenericFilter -> FiltroXY
        FiltroPixel   -> BiancoENero
        FiltroPixel   -> Negativo
        FiltroPixel   -> LuminositÃ 
        FiltroPixel   -> Contrasto
        FiltroPixel   -> RandomNoise
        FiltroXY      -> Blur
        FiltroXY      -> Pixellato
        FiltroXY      -> Lente
        FiltroXY      -> RandomNoiseXY
    ''')
"""


"Genera pixel grigi della stessa luminosità dell'originale"
class BiancoENero(FiltroPixel):
    
    def nuovo_pixel(self, pixel:Colore) -> Colore:
        L = pixel.luminosità()
        return Colore(L,L,L)    # grigio di luminosità L
    
trecime = Immagine(filename='3cime.png')
#BiancoENero().applica(trecime).visualizza() 


"Inverte la scala di luminosità"
class Negativo(FiltroPixel):
    
    def nuovo_pixel(slef, pixel:Colore) -> Colore:
        return Colore.white - pixel

#Negativo().applica(trecime).visualizza()  


"Moltiplica il colore per un fattore k"
class CambioLuminosità(FiltroPixel):
    
    def __init__(self, k:float) -> None:
        self._k = k
        
    def nuovo_pixel(self, pixel:Colore) -> Colore:
        return pixel * self._k
        
#CambioLuminosità (0.5).applica(trecime).visualizza()
#CambioLuminosità (1.5).applica(trecime).visualizza()    



"Avvicina/Allontana i colori scuri e chiari al/dal grigio"
class Contrasto(FiltroPixel):
    
    def __init__(self, k:float) -> None:
        "Contrasto(k)"
        self._k = k
    
    def nuovo_pixel(self, pixel:Colore) -> Colore:
        return Colore.grey + (pixel-Colore.grey)*self._k
    
#Contrasto(0.8).applica(trecime).visualizza()
#Contrasto(1.2).applica(trecime).visualizza()


"""
Sfocatura/Blur
- da al pixel il colore medio dei vicini fino a distanza k
"""
class Blur(FiltroXY):
    
    def __init__(self, k:float):
        "inizializzo il filtro col parametro k"
        self._k = k
        
    def nuovo_pixel_XY(self, immagine:Immagine, x:int, y:int) -> Colore:
        "ciascun pixel  è la media del gruppo grande 2k * 2k che lo circonda"
        vicini = immagine.vicini(x,y,self._k)
        return sum(vicini,Colore.black) / len(vicini)

#Blur(2).applica(trecime).visualizza()
#Blur(5).applica(trecime).visualizza()

"""
Effetto pixelato
 - per ogni pixel trova il quadretto che lo contiene
 - calcola la media dei pxel nel quadretto
 - si ricorda questo valore (per non doverlo ricalcolare tante volte)
 - da a tutti i pixel del quadretto lo stesso valore medio
"""
class Pixellato(FiltroXY):
    "filtro che pixella l'immagine con la Media dei pixel del quadretto"
    
    def __init__(self, size:int):
        "inizializzo il filtro con la dimensione del qudretto"
        self._size = size
        self._valori : dict[tuple[int.int], Colore] = {}    # per ricordare i quadratini già  calcolati
     
    def reset(self) -> None :
        "per riusare lo stesso filtro su una diversa immagine lo devo resettare"
        self._valori = {}
        
    def nuovo_pixel_XY(self, immagine : Immagine, x : int, y : int) -> Colore:
        "ciascun pixel è la media del gruppo grande 2k*2k che lo circonda"
        X = x - x % self._size + self._size//2    # centro del quadrato
        Y = y - y % self._size + self._size//2
        if not (X,Y) in self._valori:             # ottimizzazione
            vicini = immagine.vicini(X, Y, self._size//2 )
            self._valori[X,Y] = sum(vicini, Colore.black)/len(vicini)
        return self._valori[X,Y]


#Pixellato(5).applica(trecime).visualizza()
#Pixellato(10).applica(trecime).visualizza()
#Pixellato(15).applica(trecime).visualizza()



"""
Effetto Lente
- all'esterno del cerchio della lente lascia l'immagine uguale
- all'interno legge i pixel che stanno ad una distanza dal centro della lente maggiorata/diminiuta di un fattore k'
"""
class Lente(FiltroXY):
    
    def __init__(self, x : int, y : int, 
                 raggio : int, ingrandimento : float) -> None:
        "inizializzo il filtro con posizione e raggio della lente e fattore di ingrandimento"
        self._x = x
        self._y = y
        self._raggio2 = raggio*raggio
        self._ingrandimento = ingrandimento
    
    def nuovo_pixel_XY(self, immagine : Immagine , x : int, y : int):
        """ciascun pixel che sta dentro la lente 
            è preso da quello che sta sulla retta dal centro della lente
            ad una distanza aumentata di ingrandimento
        """
        dx = x - self._x
        dy = y - self._y
        if dx*dx + dy*dy <= self._raggio2:
            # cerca il pixel giusto
            X = self._x + dx * self._ingrandimento
            Y = self._y + dy * self._ingrandimento
            return immagine.get_pixel(X,Y)
        else:
            # altrimenti lascio il pixel così com'è¨
            return immagine.get_pixel(x,y)
        
#Lente(100,100,100,0.5).applica(trecime).visualizza()
#Lente(100,100,100,1.5).applica(trecime).visualizza()



"""
Rumore sul Pixel
- RandomNoise: aggiunge al pixel una variazione di colore casuale da -k a +k per ogni canale
- RandomLight: aggiunge al pixel una variazione di grigio casuale da -k a +k uguale per tutti i canali
"""
class RandomNoise(FiltroPixel):
    def __init__(self, k : int) -> None :
        self._k = k
    
    def nuovo_pixel(self, colore : Colore) -> Colore :
        return colore + Colore.random(-self._k, +self._k)

class RandomLight(RandomNoise):
    
    def nuovo_pixel(self, colore : Colore) -> Colore :
        L = randint(-self._k, +self._k)
        return colore + Colore(L,L,L)

#RandomNoise(50).applica(trecime).visualizza()
#RandomLight(50).applica(trecime).visualizza()



"""
Rumore sulla posizione del pixel (FiltroXY)
- sceglie un pixel vicino entro distanza k
"""
from random import randint

class RandomNoiseXY(FiltroXY):
    
    def __init__(self, k:int) -> None:
        self._k = k
        
    def nuovo_pixel_XY(self, immagine:Immagine, x:int, y:int) -> Colore:
        X = x + randint(-self._k, self._k)
        Y = y + randint(-self._k, self._k)
        return immagine.get_pixel(X,Y)

#RandomNoiseXY(5).applica(trecime).visualizza()




"""
(CONCLUSIONI)
• INTERFACCIA UGUALE: anche se i due tipi di filtro sono diversi si applicano allo stesso modo!!!
    ▪ nomi uguali dei metodi -> oggetti intercambiabili (ricordate il "Duck Typing"?)
    ▪ l'applicazione che li usa non deve preoccuparsi di come sono fatti
    (tranne in questo caso per la loro creazione)
    
• RIUSO DEL CODICE: ciascun filtro eredita le funzionalità comuni dalla superclasse e la estende
▪ una unica realizzazione delle funzionalità comuni -> meno errori di copy/paste e di aggiornamento
"""




"""
DISEGNO DI FIGURE SULLE IMMAGINI
• una Figura ha:
    ▪ un colore
    ▪ eventuali altri parametri
• e può:
    ▪ essere disegnata su una immagine in una certa posizione
    
import graphviz
figura = graphviz.Digraph()
figura.body.append('''
        Figuta ha posizione e colore -> Punto
        Figuta ha posizione e colore -> Linea
        Figuta ha posizione e colore -> Ellisse
        Figuta ha posizione e colore -> Poligono ha lati
        Ellisse -> Cerchio
        Poligono ha lati -> Triangolo
        Poligono ha lati -> Poligono Regolare ha lati uguali
        Poligono ha lati -> Rettangolo
        Triangolo -> Triangolo Equilatero
        Rettangolo -> Quadrato
        Poligono Regolare ha lati uguali -> Triangolo Equilatero
        Poligono Regolare ha lati uguali -> Pentagono
        Poligono Regolare ha lati uguali -> Qaudrato
    ''')
"""



"""
Figura e Punto
• tutte le Figure hanno un colore ed una posizione
• il punto disegna un pixel di quel colore nella posizione
"""
class Figura:
    
    def __init__(self, colore:Colore, x:float, y:float):
        self._colore = colore
        self._x = x
        self._y = y
        
    def disegna(self, immagine:Immagine) -> None:
        pass    # per default non faccio nulla
        
class Punto(Figura):
    
    def disegna(self, immagine:Immagine) -> None:
        immagine.set_pixel(self._x, self._y, self._color)


"""
Linea (segmento)
• tutte le Figure hanno un colore ed una posizione
• il punto disegna un pixel di quel colore nella posizione
"""
import math, random

class Linea (Figura):
    
    def __init__(self, colore : Colore, x0 : float, y0 : float, 
                 lunghezza : float, angolo : float):
        "una linea che parte da un punto, e ha lunghezza e direzione"
        super().__init__(colore, x0, y0)
        self._lunghezza = lunghezza
        self._angolo    = angolo
        self._cos = math.cos(math.radians(angolo))
        self._sin = math.sin(math.radians(angolo))

    # creo un secondo costruttore (classmethod) che 
    # dalle coordinate degli estremi calcola distanza ed angolo
    @classmethod
    def lato(cls, colore, x,y, x1, y1) -> 'Linea' :
        "costruttore che parte dagli estremi della linea"
        dx = x1 - x
        dy = y1 - y
        lunghezza = math.dist((x,y),(x1,y1))
        angolo = math.degrees(math.atan2(dy, dx))
        return cls(colore, x, y, lunghezza, angolo)
    
    # viceversa, data una linea fa comodo trovare l'altro estremo
    def estremo(self):
        "torna l'altro estremo"
        return (self._x + self._cos*self._lunghezza,
                self._y + self._sin*self._lunghezza)

    def disegna(self, immagine : Immagine) -> None:
        "disegna la linea usando trigonometria"
        # scandisco la lunghezza della linea per disegnarne i punti
        for i in range(round(self._lunghezza)+1):
            X = self._x + i*self._cos
            Y = self._y + i*self._sin
            immagine.set_pixel(X,Y,self._colore)


canvas = Immagine(500, 200)
for x in range(0,200,20):
    for y in range(0,200,20):
        Linea(Colore.random(), x, y, 20, random.randint(1,260)).disegna(canvas)

Linea.lato(Colore.random(200,250), 300, 50, 400, 150).disegna(canvas)
#canvas.visualizza()



"""
Poligono
- un qualsiasi poligono è fatto da un gruppo di linee 
- (non verifichiamo che siano consecutive o che sia una superficie chiusa)
"""
class Poligono(Figura):
    "Un poligono è una figura fatta di linee"
    
    def __init__(self, linee : list[Linea]):
        self._linee  = linee        
    
    def disegna(self, immagine: Immagine):
        for l in self._linee:
            l.disegna(immagine)
            
Poligono([
    Linea.lato(Colore.red,   300, 100, 330, 100),
    Linea.lato(Colore.green, 300, 100, 300, 140),
    Linea.lato(Colore.cyan,  330, 100, 300, 140)
]).disegna(canvas)
#canvas.visualizza()


"""
Triangolo
- dati 3 punti, ne costruisce le tre linee
"""
class Triangolo(Poligono):
    "Un Triangolo è un poligono con 3 lati"
    
    def __init__(self, colore : Colore,  
                         x  : float, y  : float, 
                         x1 : float, y1 : float, 
                         x2 : float, y2 : float):
        lato1 = Linea.lato(colore, x, y, x1,y1)
        lato2 = Linea.lato(colore, x1,y1,x2,y2)
        lato3 = Linea.lato(colore, x2,y2,x, y)
        super().__init__([lato1, lato2, lato3])

canvas = Immagine(500, 200)
Triangolo(Colore.red, 250,50, 290, 100, 270, 150).disegna(canvas)
#canvas.visualizza()


"""
Rettangolo
• dato l'angolo sopra a sinistra, larghezza, altezza e inclinazione
• costruisce le 4 linee
"""
class Rettangolo(Poligono):
    "Un Rettangolo Ã¨ un poligono con 4 lati perpendicolari"
    
    def __init__(self, colore : Colore, x : float, y : float, 
                 larghezza : float, altezza : float, angolo : float):
        self._larghezza = larghezza
        self._altezza   = altezza
        self._angolo    = angolo
        sopra           = Linea(colore, x, y, larghezza, angolo)
        sinistra        = Linea(colore, x, y, altezza,   angolo+90)
        x1,y1           = sopra.estremo()       # vertice in alto a destra
        destra          = Linea(colore, x1, y1, altezza, angolo+90)
        x2,y2           = sinistra.estremo()    # vertice in basso a sinistra
        sotto           = Linea(colore, x2, y2, larghezza, angolo)
        super().__init__([sopra, sotto, sinistra, destra])
        

canvas = Immagine(500, 200)        
Rettangolo(Colore.green, 100, 50, 300, 100, 0).disegna(canvas)
#canvas.visualizza()


"""
Un Quadrato è un rettangolo con i lati uguali
"""
class Quadrato(Rettangolo):
    
    def __init__(self, colore : Colore, x: float, y: float, 
                 lato : int, direzione : float):
        super().__init__(colore, x, y, lato, lato, direzione)

Quadrato(Colore.red, 200, 100, 100, -30).disegna(canvas)
#canvas.visualizza()  





"""
METODOLOGIA di analisi Object Oriented
• Si individuano le strutture dati necessarie (class)
• con i loro attributi (informazioni "personali" di ciascun dato)
    ▪ se una informazione è identica e comune a tutti gli individui la posso mettere come attributo di classe
• la loro inizializzazione ( __init__ )
• i metodi fondamentali (operazione sui dati o che calcolano valori a partire dagli attributi)
    ▪ se vogliamo creare l'oggetto in altri modi possiamo creare un @classmethod

Ogni volta che vogliamo aggiungere una funzionalità ci dobbiamo chiedere quale oggetto deve essere "responsabile"
(oppure "conosce le informazioni") per calcolarla

Metafora dell'ufficio
• E' un po' come voler organizzare un ufficio con persone che hanno tipi di mansioni diverse
    ▪ ciascuno ha le sue informazioni e si cerca di non assegnarle a più uffici (classi)
    ▪ gli scambi tra impiegati devono essere minimi



Ereditarietà (Specializzazione/Riuso e Ampliamento delle funzionalita)
Se si vede che diverse classi condividono dei comportamenti/attributi comuni
- definiamo una super-classe che contiene l'implementazione comune dei metodi o gli attributi comuni
- nelle sottoclassi che ereditano da questa mettiamo solo gli attributi diversi ed i metodi diversi
    (se necessario c'è anche il modo di chiamare i metodi della superclasse)

Esempio: tutti gli animali visualizzati in un gioco hanno una posizione, una icona, un verso ...
 l'insieme degli attributi e metodi comuni può essere messo nella classe Animale
 da cui ereditano Cane, Gatto, Cavallo, Ornitorinco ....
"""


"ESEMPIO DI FIGURE GEOMETRICHE DA DISEGNARE CON LA TURTLE"
# Tutte le Figure hanno:
# - posizione
# - colore
# - un metodo che le disegna (che per default non fa nulla)
# - un metodo che ne calcola l'area (per default 0)

# Ciascuna specifica figura
# - ha dei parametri specifici (raggio, lati, cateti, fuochi, retta e fuoco, ...)
# - ha il suo metodo specifico che la disegna
# - ha il suo metodo specifico che ne calcola l'area

# Definiamo la gerarchia di classi:
# Figura
#   Punto
#   Linea
#       Freccia
#   Rettangolo
#       Quadrato
#       TriangoloRettangolo
#   PoligonoRegolare
#       Triangolo
#       Pentagono
#   EllisseApprossimataDaCerchi
#       Cerchio



import turtle
t = turtle.Turtle()
turtle.colormode(255)

class Figura:
    
    def __init__(self, x, y, colore, direzione=0, spessore=1, campitura=None):
        self._x = x
        self._y = y
        self._colore = colore
        self._direzione = direzione
        self._spessore = spessore
        self._campitura = campitura

    def area(self):
        raise Exception("Il metodo 'area' non è stato implementato")

    def draw(self, turtle):
        turtle.end_fill()
        turtle.up()
        turtle.goto(self._x,self._y)
        turtle.setheading(self._direzione)
        turtle.color(self._colore)
        turtle.pensize(self._spessore)
        turtle.down()
        if self._campitura:
            turtle.fillcolor(self._campitura)
            turtle.begin_fill()
        
    def move(self, x, y):
        self._x = x
        self._y = y


class Rettangolo(Figura):
    
    def __init__(self, x, y, colore, larghezza, altezza, 
                 direzione=0, spessore=1, campitura=None):
        "creo un nuovo rettangolo"
        # riuso l'inizializzazione della mia superclasse per
        # gli attributi che giÃ  sa gestire
        super().__init__(x, y, colore, direzione, spessore, campitura)
        # gestisco qui gli attributi aggiuntivi
        self._larghezza = larghezza
        self._altezza = altezza

    def area(self):
        "calcolo l'area del rettangolo"
        return self._larghezza * self._altezza

    def draw(self, turtle):  
        """
        Disegno il rettangolo son la tartaruga fornita come parametro.
        """
        super().draw(turtle)
        turtle.forward(self._larghezza)
        turtle.left(90)
        turtle.forward(self._altezza)
        turtle.left(90)
        turtle.forward(self._larghezza)
        turtle.left(90)
        turtle.forward(self._altezza)
        turtle.left(90)
        turtle.end_fill()


class PoligonoRegolare(Figura):
    "Costruisco un poligono regolare"
    
    def __init__(self, x, y, lato, N, colore, 
                 direzione=0, spessore=1, campitura=None):
        super().__init__(x, y, colore, direzione, spessore, campitura)
        self._N = N
        self._lato = lato
        
    def draw(self, turtle):
        super().draw(turtle)
        angolo_esterno = 360/self._N
        for _ in range(self._N):                        
            turtle.forward(self._lato)
            turtle.left(angolo_esterno)
        turtle.end_fill()



class Quadrato(Rettangolo):
    
    def __init__(self, x, y, lato, colore, 
                 direzione=0, spessore=1, campitura=None):
        super().__init__(x, y, colore, lato, lato, 
                         direzione, spessore, campitura )


r = Rettangolo(50, 100, (255,0,0), 200, 100, direzione=45, spessore=5, campitura=(255,255,0))
p = PoligonoRegolare(-100, -100, 50, 5, (0,0,255), 20, 4, campitura=(255,0,0) )
q = Quadrato(100, 100, 90, (0,255,0), -30, 10)

#N.B. t = turtle.Turtle()
r.draw(t)
r.move(-200,-100)
r.draw(t)
p.draw(t)
q.draw(t)

print(r.area(), q.area())























# per pixellare una immagine su una dimensione S
def pixella(x : int,y : int, I : 'Immagine', S : int):
    X = x - x%S + S//2
    Y = y - y%S + S//2
    return I.get_pixel(X,Y)   # se sbordo ci pensa da solo

def pixella10(x,y,I):    # potremmo definire una funziona ad hoc
    return pixella(x,y,I,10)


# oppure usare una lambda
#A.applica_filtro_XY(lambda x,y,I: pixella(x,y,I,10)).visualizza()

    
from random import randint
    
def rumore(x, y, I, k): # leggo un pixel a caso nell'intorno [-k, k]
    "sostituisco il pixel con un vicino"
    X = x + randint(-k,k)
    Y = y + randint(-k,k)
    return I.get_pixel(X,Y)
    
#A.applica_filtro_XY(lambda x,y,I: rumore(x,y,I,5)).visualizza()






































































































































































