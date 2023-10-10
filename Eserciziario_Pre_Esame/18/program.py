'''


Es 9: 3 punti
Si definisca la  funzione es18(d1,d2) che, 
- riceve due dizionari aventi per chiavi degli interi e per attributo insiemi di interi.
- restituisce un dizionario.
il dizionaro deve contenere come chiavi le chiavi che sono in comune ad entrambi i dizionari e come 
attributo una tupla di due elementi, il primo elemento e' 
l'insieme intersezione degli attributi della chiave nei due dizionari mentre 
il secondo e' l'unione degli attributi della chiave nei due dizionari.
Ad ESEMPIO se
d1={1: {1,2,3}, 2:{1,2,3}, 5:{1} } e 
d2={1: {3,4,5}, 3:{1,2,3}, 5:{3}, 8: {6} }
allora la funzione  restituisce il dizionario 
{1: ({3}, {1, 2, 3, 4, 5}), 5: (set(), {1, 3})}
'''


def es18(d1, d2):
    dizio = {}
    set1 = set()  
    set2 = set() 
    # per ogni chiave in d1
    for key1,values1 in d1.items():
        # per ogni chiave in d2
        for key2,values2 in d2.items():
            # if d1.chiave == d2.chiave:
            if key1 == key2:
                #per ogni valore in d1:
                for valore1 in values1:
                    # per ogni valore in d2:
                    for valore2 in values2:
                        # se valore uguale 
                        if valore1 == valore2:
                            # aggiungi elemento al set1
                            set1.add(valore1)
                        # aggiungi elementi al set2
                        set2.add(valore1)
                        set2.add(valore2)
                # aggiungi i due set alla chiave comune
                dizio[key1] = (set1,set2)
                
                #rinizializza i set
                set1 = set()  
                set2 = set()
    return dizio





   

         

















