'''
si definisca la funzione es62(matrice) che riceve come argomento una matrice (lista di liste)
di interi e che:
    - individua le coordinate x1,y1 del MINIMO valore in essa contenuto
        (in caso di parita' si prenda l'elemento con x minima 
        e in caso di ulteriore parita' quello con y minima)
    - individua le coordinate x2,y2 del MASSIMO valore in essa contenuto
        (in caso di parita' si prenda l'elemento con x massima
        e in caso di ulteriore parita' quello con y massima)
    - scambia le due righe y1 ed y2 e le due colonne x1 ed x2.
Ritorna come risultato la matrice ottenuta.
La matrice originale non deve essere modificata.    
La funzione deve poter funzionare anche se x1==x2 e/o y1==y2.

Esempio: se
            | 2  0   -4 |                   | 5  10  20 |
matrice =   | 5  10  20 |   risultato =>    | 2  0   -4 |
            | 5  1   -1 |                   | 5  1   -1 |
Se invece            
            | 2   0  -4 |                   | -1  1  25 |
matrice =   | 5  10  10 |   risultato =>    | 10 10   5 |
            | 25  1  -1 |                   | -4  0   2 |
'''

def es62(matrice):
    # Massimo valore
    imax = jmax = 0
    for j in range(len(matrice[0])):
        for i in range(len(matrice)):
            if matrice[i][j] >= matrice[imax][jmax]:
                imax = i
                jmax = j
                
    # Minimo valore
    imin = jmin = 0
    for j in range(len(matrice[0])):
        for i in range(len(matrice)):
            if matrice[i][j] < matrice[imin][jmin]:
                imin = i
                jmin = j
    
    # # Crea una copia della matrice originale
    m1 = [[matrice[i][j] for j in range(len(matrice[0]))] for i in range(len(matrice))]
    
    "Scambio i1 con i2 e j1 con j2"
    for j in range(len(matrice[0])):
        m1[imin][j] = matrice[imax][j]
        m1[imax][j] = matrice[imin][j]
    for i in range(len(matrice)):
        m1[i][jmin], m1[i][jmax] = m1[i][jmax], m1[i][jmin]
    
    return m1
        
        
        
        
        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
