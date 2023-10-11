'''
Si implementi la funzione es36(listaDizionari) che presi in input una lista di dizionari
restituisce  un dizionario.
I dizionari in input della listaDizionari  hanno come  chiave stringhe
di caratteri tra 'a' e 'z' e come attributo liste di interi.
Il dizionario restituito deve avere le  chiavi che risultano presenti in tutti i dizionari della  listaDizionari.
A ciascuna chiave x di questo dizionario e' associata una lista di interi.
Un intero e' presente nella lista se e solo se e' presente in tutte le liste di attributi della chiave x.
La lista deve risultare ordinata in modo crescente.

Ad esempio se la listaDizionari contenente i tre dizionari
{'a': [1,3,5],'b':[2,3 ],'d':[3]},
{'a':[5,1,2,3], 'b':[2],'d':[3]},
{'a':[3,5], 'c':[4,1,2],'d':[4]}
il dizionario restituito sara' {'a':[3,5],'d':[]}
'''

def es36(listaDizionari):
    # devo trovare l'insieme delle chiavi che appaiono in tutti i dizionari
    # lo inizializzo con le chiavi del primo dizionario
    keys = set(listaDizionari[0].keys())
    # e lo aggiorno facendo l'intersezione con l'insieme delle chiavi di ciascuno degli altri dizionari
    for d in listaDizionari[1:]:
        keys = keys.intersection(d.keys())
        
    # Inizializziamo un dizionario vuoto chiamato "diz"
    diz = {}
    
    # Iteriamo attraverso le chiavi e i valori del primo dizionario in listaDizionari
    for k, v in listaDizionari[0].items():
        # Verifichiamo se la chiave k è presente nell'insieme keys
        if k in keys:
            # Creiamo una nuova chiave nel dizionario "diz" con la chiave k
            # e associamo un insieme (set) dei valori v a quella chiave
            diz[k] = set(v)

    
    # e poi per ciascun dizionario e per ciascuna chiave
    for d in listaDizionari[1:]:
        for k, v in d.items():
            if k in diz:
                # aggiorno i valori tenendo solo quelli comuni (intersezione)
                diz[k] = diz[k].intersection(v)
    # alla fine ordino i valori associati a ciascuna chiave (ottenendo liste ordinate)
    return {k: sorted(v) for k, v in diz.items()}





























