''' 
Si implementi la funzione es37(listaDizionari) che presi in input una lista di dizionari
restituisce  un dizionario.
I dizionari della listaDizionari  hanno come  chiave stringhe di caratteri tra 'a' e 'z' 
e come attributo liste di interi.

Il dizionario restituito deve avere come chiavi le chiavi  comuni ad almeno la meta' dei 
dizionari della lista.
A ciascuna chiave x di questo dizionario e' associato un insieme.
Un intero deve essere presente nell'insieme associato ad x se e solo se compare come attributo di x
in almeno uno dei dizionari della listaDizionari.
Ad esempio se la listaDizionari contenente i tre dizionari
{'a': [1,3,5],'b':[2,3 ],'d':[3]}, 
{'a':[5,1,2,3], 'b':[2],'d':[3]},
{'a':[3,5], 'c':[4,1,2],'d':[4]}
il dizionario restituito sara' {'a':{1,2,3,5},'b':{2,3},'d':{3,4}}
'''

def es37(listaDizionari):
    # lunghezza della lista di dizionari
    listDiz = len(listaDizionari)
    
    #inzializzo lista vuota
    lista = []
    
    # valore che calcola il minimo numero di chiavi necessarie 
    # per comparire nel dizio finale (deto: 'fatttore presenza')
    val_listDiz = listDiz//2
    
    # aggiungo alla lista tutte le chiavi 
    for dizio in listaDizionari:
        for k,v in dizio.items():
            lista.append(k)
      
    nuova_lista = []    
    # per ogni chiave nella lista
    for x in lista:
        i = 0
        count = 0
        # scorro tutta la lista di nuovo
        while (i < len(lista)):
            # verifico quante volte la chiave X è presente nella lista
            if x == lista[i]:
                count += 1
            i+=1
        # svolgo i calcoli per capire se dato il 'fattore presenza'
        # posso aaggiungere i valori alla lista corrispondente a quella chiave X
        if listDiz == 1:
            nuova_lista.append(x)
        if listDiz == 2:
            if count >= val_listDiz:
                nuova_lista.append(x)
        if listDiz > 2:
            if count >= val_listDiz + 1:
                nuova_lista.append(x)
                        
            
            
    nuova_lista = set(nuova_lista)
    dizio_finale = {}
    
    # ogni chiave del dizio ha valore un set vuoto
    for x in nuova_lista:
        dizio_finale[x] = set()

    # per ogni chiave nella lista
    for x in nuova_lista:
        # per ogni dizionario nella listaDizionari
        for dizio in listaDizionari:
            # per ogni chiave, valore nel dizio
            for k,v in dizio.items():
                # if la chiave nella lista == chiave nel dizio
                if x == k:
                    # aggiungo tutti i valori a quella chiave
                    for valore in v:
                        dizio_finale[x].add(valore)
    
    
    return dizio_finale




         
        














