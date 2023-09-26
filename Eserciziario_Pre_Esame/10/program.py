'''
Es 10: 3 punti
progettare la funzione es10(ftesto,k) che, presi in input 
l'indirizzo di un file di testo ed un intero k, restituisce una stringa di caratteri lunga k.
Il file di testo contiene stringhe di diversa lunghezza 
(una per riga ed ogni riga termina con '\n'), si guardi 
ad esempio il file f9.txt. 
I k caratteri della stringa restituita  dalla funzione si ottiengono
considerando le stringhe lunghe k presenti nel file di testo. 
L'i-mo carattere della stringa sara' il carattere che compare con maggior 
frequenza come i-mo carattere delle stringhe lunghe k nel file di testo (in caso 
di parita' di occorrenze viene scelto il carattere che precede 
gli altri lessicograficamente). 
Nel caso il file di testo non contenga parole lunghe k allora viene restituita 
la stringa vuota.  
Ad Esempio, per il file di testo f9.txt e k=3 la funzione restituisce  la stringa 'are' a 
seguito della presenza in f9.txt delle seguenti 4 stringhe lunghe 3:
tre
due
amo
ora 
'''

path = "C:/Users/UtentePC/Desktop/10/ft9.txt"
def es10(ftesto,k):
    #inizializzo la stringa finale
    stringa_finale = ''
    # apro il file
    file = open(path)
    # creo la lista con tutte le parole del file
    lista = file.read().split()
    # creo una nuova lista con le parole lunghe k
    lista_k = []
    for parola in lista:
        if len(parola) == k:
            lista_k.append(parola)
    if (len(lista_k) == 0):
        return stringa_finale
    # creo una stringa concatenando le parole
    stringa = ''
    for parola in lista_k:
        stringa += parola
        
    lunghezza_lista = len(lista_k) 
    #print(lunghezza_lista)
    
    
    lista_prova = []
    fine = 0
    """
    Nel while generale ciclo sulla lunghezza della parola
    """
    while(fine < k): 
        j = 0
        """
        Ciclo sul numero di elementi con lunghezza k
        """
        #creo una lista con solo le i-esime lettere di ogni parola
        while(j < lunghezza_lista):
            lista_prova.append(stringa[fine+k*j]) 
            print(lista_prova)
            j += 1
            # ESEMPIO [ora,tre,due,amo] primo ciclo contiene ['o', 't', 'd', 'a']
        
        massimo = 0
        """
        Ciclo sulla nuova lista_prova
        """
        for i in range(len(lista_prova)):
            # se il numero tot delle volte della lettera i-esima > massimo
            if (lista_prova.count(lista_prova[i]) > massimo):
                # aggiorno il massimo
                massimo = lista_prova.count(lista_prova[i])
                # mi salvo la lettera
                index = lista_prova[i]
            # se il numero tot delle volte della lettera i-esima == massimo AND la lettera viene prima nell'alfabeto
            if (lista_prova.count(lista_prova[i]) == massimo and lista_prova[i] < index):
                # aggiorno il massimo
                massimo = lista_prova.count(lista_prova[i])
                # mi salvo la lettera
                index = lista_prova[i]
        """
        Se max > 1 metto nella stringa vuota la lettera contenuta in index
        Sennò ordino alfabeticamente la lista_prova e ci metto il primo elemento
        """
        if (massimo > 1):
            stringa_finale += index
        else:
            primo_elemento = sorted(lista_prova)
            stringa_finale += primo_elemento[0]
        fine += 1
        lista_prova = []
        
             
    return stringa_finale



