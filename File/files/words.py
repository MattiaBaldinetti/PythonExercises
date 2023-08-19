
def noalpha(s):
    '''Ritorna una stringa contenente tutti i caratteri non alfabetici contenuti in s, senza ripetizioni'''
    noa = ''
    for c in s:
        if not (c in noa or c.isalpha()):	# se non (ho già visto c oppure è alfabetico)
            noa += c
    return noa

def words(s):
    '''Ritorna la lista delle parole contenute nella stringa s'''
    noa = noalpha(s)
    for c in noa:
        s = s.replace(c, ' ')
    return s.split()

if __name__ == '__main__':
    def test_noalpha(s):
        print(s)
        print('Non alfabetici:', '"'+noalpha(s)+'"' )
    test_noalpha("""Frase (con parentesi [],{}, simboli vari %&#@), accapo,
    numeri 0987 e puntegg.!""")
    test_noalpha("FraseSenzaCaratteriNonAlfabetici")

    def test_words(s):
        print(s)
        print('words:', words(s))

    s = """def words(s):
    '''Ritorna la lista delle parole contenute nella stringa s'''
    noa = noalpha(s)
    for c in noa:
    s = s.replace(c, ' ')
    return s.split()"""
    test_words(s)
