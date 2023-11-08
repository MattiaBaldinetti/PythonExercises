'''    
Es 3: 3 punti
due parole possono fondersi se la prima ha un suffisso di almeno due caratteri 
che coincide col prefisso di pari lunghezza della seconda. 
Il risultato della fusione e' la parola che si ottiene concatenando la prima parola 
con la seconda grazie alla parte comune.
Ad esempio:  
- le due parole 'candela' ed 'elastico' possono fondersi grazie al suffisso 
  'ela' di  3 caratteri, il risultato della fusione e' la parola  'candelastico' 
_ le parole 'Angelo' e 'gelo' possono fondersi grazie al suffisso 'gelo', la parola 
  risultante e''Angelo'. 
_ le parole 'aaaaa' e 'aaab' possono fondersi in diversi, modi: 
    _ grazie al suffisso 'aa' si ottiene la fusione 'aaaaaab' 
    _ grazie al suffisso 'aaa' si ottiene la fusione 'aaaaab'.
  Si definisca la  funzione es2(insieme) che, dato un insieme di parole, restituisce 
  la lista con tutte le possibili fusioni. 
  La lista deve risultare ordinata lessicograficamente e vanno eliminati eventuali 
  duplicati.
  
ESEMPIO: 
se  insieme={  'aaaa', 'acde', 'aacd', 'aaaade'} la funzione restituira' la lista: 
['aaaaaade', 'aaaaade', 'aaaacd', 'aaaade', 'aacde'] 
grazie alle seguenti fusioni:
'aaaa'  'aaaade' ---> 'aaaaaade' con suffisso 'aa'
'aaaa'  'aaaade' ---> 'aaaaade'  con suffisso 'aaa'
'aaaa'  'aaaade' ---> 'aaaade'   con suffisso 'aaaa'
'aaaa'  'aacd'   ---> 'aaaacd'   con suffisso 'aa'
'aacd'  'acde'   ---> 'aacde'    con suffisso 'acd'
'''
def es8(insieme):
    ls_fin=[]
    # per ogni elemento nell'insieme
    for p in insieme:
        # per ogni elemento nell'insieme senza l'elemento p
        for p2 in insieme-{p}:
            # parte da 2 fino
            for i in range(2,len(p)+1):
                if p[-i:]==p2[:i]:
                    ls_fin.append(p+p2[i:])
                else: continue
    ls_fin=set(ls_fin)
    ls_fin=list(ls_fin)
    ls_fin.sort()
    return ls_fin






