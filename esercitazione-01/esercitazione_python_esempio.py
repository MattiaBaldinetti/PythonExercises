import evaluation

"""
### Es. 10 - Facile
Vengono date due stringhe in ingresso ed è necessario controllare se
la prima stringa `S` è stata scritta al rovescio rispetto alla stringa
`T`.

T = 'pippo'
S = 'oppip'

allora S è stata scritta al rovescio.

Mentre

```python
T = 'pippo'
S = 'opppp'
```
non lo è.

Scrivere una funzione check_reverse(S, T) che prende in ingresso due
stringhe e ritorni True se sono a rovescio, altrimenti False.
"""


def check_reverse(S, T):
    stringa = ''
    for t in range(len(T)-1,-1,-1):
        stringa = stringa + T[t]
    if S == stringa:
        return True
    else:
        return False
        

#print(check_reverse('pippo', 'oppip'))
evaluation.evaluate(check_reverse)
#evaluation.show_tests(check_reverse)




