"""
Disegnare alberi (esempio di figura frattale (https://it.wikipedia.org
/wiki/Frattale) )
• Un albero di livello 0 è una foglia (cerchietto) (caso base)
• Un albero di livello N è formato da: (ricomposizione)
    ▪ un tronco lungo X
    ▪ un albero di livello N-1 inclinato a sinistra, con tronco 80% di X (sottoproblema)
    ▪ un albero di livello N-1 inclinato a destra, con tronco 70% di X (sottoproblema)
Questa è una definizione ricorsiva: i due rami sono due alberi!
Mi serve uno strumento di disegno:
    • col modulo turtle posso tracciare movimenti relativi alla tartaruga
    • col modulo random posso generare colori casuali
"""

import turtle
from random import randint # generatore di interi casuali turtle.colormode(255) # setto i colori in modalità RGB
t = turtle.Turtle() # creo una tartaruga t.penup() # alzo la penna
t.left(90) # giro verso l'alto t.back(200) # mi posiziono in basso
t.pensize(5) # con penna cicciotta
t.speed(0) # e velocità alta
#help(turtle) 

def albero(t, tronco, angolo, livelli):
    'disegno un albero con un certo tronco iniziale e # di livelli'
    # TODO
    if livelli == 0:
        draw_leaf(t)
    else:
        # disegno il tronco (e mi sposto alla fine)
        draw_trunk(t, tronco)
        # mi giro a sinistra
        t.left(angolo)
        # disegno il ramo sinistro, più piccolo 80%
        albero(t, tronco * 0.8, angolo, livelli-1)
        # mi giro a destra
        t.right(angolo*2) # disegno il ramo destro, più piccolo 70%
        albero(t, tronco * 0.7, angolo, livelli-1)
        # torno nella direzione iniziale
        t.left(angolo)
        # torno alla base del tronco
        t.back(tronco)
        
# devo definire come disegnare il tronco e la foglia
def draw_trunk(t, lunghezza):
    'Disegno un tratto di colore casuale'
    # TODO
    # cambio colore a caso
    R = randint(100, 200)
    G = randint(100, 200)
    B = randint(100, 200)
    t.color(R,G,B)
    # abbasso la penna
    t.pendown()
    # mi muovo in avanti di lunghezza pixel
    t.forward(lunghezza)
    # alzo la penna
    t.penup()
    # NOTA: ora sono all'estremo opposto del tronco
    
    
def draw_leaf(t):
    'disegno una foglia col colore corrente'
    # TODO
    # abbasso la penna
    t.pendown()
    # disegno un pallino
    t.dot()
    # alzo la p
    
## Vediamo se funziona :-)
#t.clear() # pulisco il foglio 
print(albero(t,100,30,6))