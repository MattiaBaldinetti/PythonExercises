# -*- coding: utf-8 -*-
import testlib
import isrecursive
import os
import sys
import glob
import hashlib

if not os.path.exists('program.py'):
    print('WARNING: Save program.empty.py as program.py\n'
          'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    sys.exit(0)

import program


def my_decorator(func):
    def wrapped_func(*args, **kwargs):
        col = ''
        if any(err in args[0] for err in ['[OK]', 'Correct']):
            col = COL['GREEN']
        if any(err in args[0] for err in ['error', 'Error', 'ERROR',]):
            col = COL['RED']
        return func(f'{COL["BOLD"]}{col}', *args, f'{COL["RST"]}{COL["ENDC"]}', **kwargs, )
    return wrapped_func


my_print = my_decorator(print)

################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #

# ----- The use of the following functions in your program is forbidden ------ #
# ---------------------------------------------------------------------------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################

#### Use DEBUG=True to disable the recursion tests and enable the
#### stack trace: each error will produce a more verbose output
####
#### Mettete DEBUG=True per disattivare i test di ricorsione  e
#### fare debug delle funzioni più facilmente attivando stack trace
# %% ---------------------- DEBUG VARIABLE -------------------
DEBUG = True
# DEBUG = False
# %% ---------------------- TEST SECTION -------------------
#############################################################################

COL = {'RED': '\u001b[31m',
       'RST': '\u001b[0m',
       'GREEN': '\u001b[32m',
       'YELLOW' : '\u001b[33m',
       'BOLD' : '\033[1m',
       'ENDC' : '\033[0m'}


def test_personal_data_entry():
    if 'name' in program.__dict__:
        assert program.name       != 'NAME', f"{COL['YELLOW']}ERROR: Please assign the 'name' variable with YOUR NAME in program.py{COL['RST']}"
        assert program.surname    != 'SURNAME', f"{COL['YELLOW']}ERROR: Please assign the 'surname' variable with YOUR SURNAME in program.py{COL['RST']}"
        assert program.student_id != 'MATRICULATION NUMBER', f"{COL['YELLOW']}ERROR: Please assign the 'student_id' variable with YOUR MATRICULATION NUMBER in program.py{COL['RST']}"
    else:
        assert program.nome      != 'NOME', f"{COL['YELLOW']}ERRORE: Indica il tuo NOME in program.py{COL['RST']}"
        assert program.cognome   != 'COGNOME', f"{COL['YELLOW']}ERRORE: Indica il tuo COGNOME in program.py{COL['RST']}"
        assert program.matricola != 'MATRICOLA', f"{COL['YELLOW']}ERRORE: Indica il tuo NUMERO DI MATRICOLA in program.py{COL['RST']}"
    return 0 # ALL OK, ci pensano le asserzioni a dare errore se c'è qualcosa che non va

###############################################################################

# %% ----------------------------------- FUNC1 ------------------------- #
def do_func1_tests(int_list, keys, expected):
    res = program.func1(int_list, keys)
    if res == None:
        raise testlib.NotImplemented()
    testlib.checkDict(res, expected)
    return 0.5


def test_func1_1():
    '''
    int_list = [4, 6, 10, 13]
    keys = {2, 3, 5}
    expected = {2:[10, 6, 4], 3:[6], 5:[10]}
    '''
    int_list = [4, 6, 10, 13]
    keys = {2, 3, 5}
    expected = {2:[10, 6, 4], 3:[6], 5:[10]}
    return do_func1_tests(int_list, keys, expected)

def test_func1_2():
    '''
    int_list = [29, 54, 5, 32, 46]
    keys = {5, 23}
    expected = {5: [5], 23: [46]}
    '''
    int_list = [29, 54, 5, 32, 46]
    keys = {5, 23}
    expected = {5: [5], 23: [46]}
    return do_func1_tests(int_list, keys, expected)

def test_func1_3():
    '''
    int_list = [200, 189, 115, 50, 24, 7, 196, 91, 103, 136]
    keys = {7, 97}
    expected = {97: [], 7: [196, 189, 91, 7]}
    '''
    int_list = [200, 189, 115, 50, 24, 7, 196, 91, 103, 136]
    keys = {7, 97}
    expected = {97: [], 7: [196, 189, 91, 7]}
    return do_func1_tests(int_list, keys, expected)

def test_func1_4():
    '''
    int_list = [2, 51, 440, 471, 317, 425, 437, 185, 299, 35, 125, 69, 146, 333, 15, 178, 261, 264, 146, 234, 74, 270, 285, 414, 31, 398, 268, 94, 200, 423, 120, 254, 172, 282, 119, 91, 175, 425, 310, 493, 232, 10, 337, 290, 342, 140, 418, 143, 412, 152]
    keys = {5, 23, 37}
    expected = {5: [440, 425, 425, 310, 290, 285, 270, 200, 185, 175, 140, 125, 120, 35, 15, 10], 37: [333, 185, 74], 23: [437, 414, 299, 69]}
    '''
    int_list = [2, 51, 440, 471, 317, 425, 437, 185, 299, 35, 125, 69, 146, 333, 15, 178, 261, 264, 146, 234, 74, 270, 285, 414, 31, 398, 268, 94, 200, 423, 120, 254, 172, 282, 119, 91, 175, 425, 310, 493, 232, 10, 337, 290, 342, 140, 418, 143, 412, 152]
    keys = {5, 23, 37}
    expected = {5: [440, 425, 425, 310, 290, 285, 270, 200, 185, 175, 140, 125, 120, 35, 15, 10], 37: [333, 185, 74], 23: [437, 414, 299, 69]}
    return do_func1_tests(int_list, keys, expected)



# %% ----------------------------------- FUNC2 ------------------------- #
def do_func2_tests(a_string, char, expected):
    res = program.func2(a_string, char)
    if res == None:
        raise testlib.NotImplemented()
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] La stringa restituita non è corretta / The returned string is incorrect\n[ERROR] expected={expected} returned={res}.\n {'*'*50}''')
        return 0
    return 0.5


def test_func2_1():
    '''
    a_string = 'impossible'
    char = 'i'
    expected = 'spoml'
    '''
    a_string = 'impossible'
    char = 'i'
    expected = 'spoml'
    return do_func2_tests(a_string, char, expected)

def test_func2_2():
    '''
    a_string = 'abracadabra'
    char = 'b'
    expected = 'rdc'
    '''
    a_string = 'abracadabra'
    char = 'b'
    expected = 'rdc'
    return do_func2_tests(a_string, char, expected)

def test_func2_3():
    '''
    a_string = ''
    char = ' '
    expected = ''
    '''
    a_string = ''
    char = ' '
    expected = ''
    return do_func2_tests(a_string, char, expected)

def test_func2_4():
    '''
    a_string = 'capslockunhinderedbacklistartsgamesparasolphiltershobbledehoysmdvpratedfutonselectrocutedprevaricatemistakeobjectivenessallegorizesdisgustingunorderedunreleasedsuperadded'
    char = 'Z'
    expected = 'zyvutsrponmlkjihgfedcba'
    '''
    a_string = 'capslockunhinderedbacklistartsgamesparasolphiltershobbledehoysmdvpratedfutonselectrocutedprevaricatemistakeobjectivenessallegorizesdisgustingunorderedunreleasedsuperadded'
    char = 'Z'
    expected = 'zyvutsrponmlkjihgfedcba'
    return do_func2_tests(a_string, char, expected)

# %% ----------------------------------- FUNC3 ------------------------- #
def do_func3_tests(string_list1, string_list2, expected):
    res = program.func3(string_list1, string_list2)
    testlib.checkList(res, expected)
    return 2/3


def test_func3_1():
    '''
    string_list1=['shop', 'park', 'elichopter', 'cat', 'elephant']
    string_list2=['ark', 'contact', 'hop', 'mark']
    expected = ['elichopter','contact','park', 'shop']
    '''
    string_list1=['shop', 'park', 'elichopter', 'cat', 'elephant']
    string_list2=['ark', 'contact', 'hop', 'mark']
    expected = ['elichopter','contact','park', 'shop']
    return do_func3_tests(string_list1, string_list2, expected)

def test_func3_2():
    '''
    string_list1=['fig', 'hoy', 'ids', 'save', 'roe', 'detersive', 'list']
    string_list2=['devastatingly', 'strategists', 'formalist']
    expected = ['devastatingly', 'formalist']
    '''
    string_list1=['fig', 'hoy', 'ids', 'save', 'roe', 'detersive', 'list']
    string_list2=['devastatingly', 'strategists', 'formalist']
    expected = ['devastatingly', 'formalist']
    return do_func3_tests(string_list1, string_list2, expected)

def test_func3_3():
    '''
    string_list1=['succouring', 'compartmental', 'sour', 'varityped', 'go', 'fulmination', 'wilfulness', 'dangerous', 'subtracting', 'fragmented', 'preciseness', 'rem', 'hypnotically']
    string_list2=['hartebeests', 'absorbencies', 'straitening', 'precise', 'saragossa', 'enumerates', 'regna', 'margarines', 'invigilates', 'maladapted', 'prosperous', 'capitalize']
    expected = ['preciseness', 'enumerates', 'dangerous', 'saragossa']
    '''
    string_list1=['succouring', 'compartmental', 'sour', 'varityped', 'go', 'fulmination', 'wilfulness', 'dangerous', 'subtracting', 'fragmented', 'preciseness', 'rem', 'hypnotically']
    string_list2=['hartebeests', 'absorbencies', 'straitening', 'precise', 'saragossa', 'enumerates', 'regna', 'margarines', 'invigilates', 'maladapted', 'prosperous', 'capitalize']
    expected = ['preciseness', 'enumerates', 'dangerous', 'saragossa']
    return do_func3_tests(string_list1, string_list2, expected)

# %% ----------------------------------- FUNC4 ------------------------- #

def do_func4_tests(ID, expected):
    input_file = f'func4/func4_test{ID}.txt'
    output_file= f'func4/func4_out{ID}.txt'
    expected_file=f'func4/func4_exp{ID}.txt'
    res = program.func4(input_file, output_file)
    if res == None:
        raise testlib.NotImplemented()
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il valore ritornato non è corretto! / Returned value is incorrect!\n'''
              f'''[ERROR] Expected {expected} returned {res}\n {'*'*50}''')
        return 0
    testlib.check_text_file(output_file, expected_file)
    return 2


def test_func4_1():
    '''
    input_file = func4/func4_test1.txt
    output_file = func4/func4_out1.txt
    '''
    ID = 1
    expected = 112
    return do_func4_tests(ID, expected)

def test_func4_2():
    '''
    input_file = func4/func4_test2.txt
    output_file = func4/func4_out2.txt
    '''
    ID = 2
    expected = 46610
    return do_func4_tests(ID, expected)


def test_func4_3():
    '''
    input_file = func4/func4_test3.txt
    output_file = func4/func4_out3.txt
    '''
    ID = 3
    expected = 625513
    return do_func4_tests(ID, expected)

# %% ----------------------------------- FUNC5 ------------------------- #
import images

def do_test_func5(ID, expected):
    img_in  = f'func5/image0{ID}.png'

    res = program.func5(img_in)
    if res != expected:
        testlib.checkList(res, expected)
    return 2


def test_func5_1():
    '''
    imm_in = func5/image01.png
    expected = [(0, 128, 200), (200, 200, 128), (200, 128, 200)]
    '''
    ID = 1
    expected = [(0, 128, 200), (200, 200, 128), (200, 128, 200)]
    return do_test_func5(ID, expected)


def test_func5_2():
    '''
    imm_in = func5/image02.png
    expected = [100, 400, 900, 1600, 2500]
    '''
    ID = 2
    expected = [(200, 128, 200), (0, 128, 200), (200, 200, 128), (200, 28, 200)]
    return do_test_func5(ID, expected)


def test_func5_3():
    '''
    imm_in = func5/image03.png
    expected = [(177, 110, 44), (88, 131, 73), (135, 95, 98), (84, 118, 199), (125, 103, 210), (216, 237, 76), (245, 52, 148), (132, 68, 177), (13, 208, 224), (202, 121, 243)]
    '''
    ID = 3
    expected = [(177, 110, 44), (88, 131, 73), (135, 95, 98), (84, 118, 199), (125, 103, 210), (216, 237, 76), (245, 52, 148), (132, 68, 177), (13, 208, 224), (202, 121, 243)]
    return do_test_func5(ID, expected)


def test_func5_4():
    '''
    imm_in = func5/image04.png
    expected = [(252, 128, 3), (248, 128, 7), (244, 128, 11), (240, 128, 15), (236, 128, 19), (232, 128, 23), (228, 128, 27), (224, 128, 31), (220, 128, 35), (216, 128, 39), (212, 128, 43), (208, 128, 47), (204, 128, 51), (200, 128, 55), (196, 128, 59), (192, 128, 63), (188, 128, 67), (184, 128, 71), (180, 128, 75), (176, 128, 79), (172, 128, 83), (168, 128, 87), (164, 128, 91), (160, 128, 95), (156, 128, 99), (152, 128, 103), (148, 128, 107), (144, 128, 111), (140, 128, 115), (136, 128, 119), (132, 128, 123), (128, 128, 127), (124, 128, 131), (120, 128, 135), (116, 128, 139), (112, 128, 143), (108, 128, 147), (104, 128, 151), (100, 128, 155), (96, 128, 159), (92, 128, 163), (88, 128, 167), (84, 128, 171), (80, 128, 175), (76, 128, 179), (72, 128, 183), (68, 128, 187), (64, 128, 191), (60, 128, 195), (56, 128, 199), (52, 128, 203), (48, 128, 207), (44, 128, 211), (40, 128, 215), (36, 128, 219), (32, 128, 223), (28, 128, 227), (24, 128, 231), (20, 128, 235), (16, 128, 239), (12, 128, 243), (8, 128, 247), (4, 128, 251), (0, 128, 255)]
    '''
    ID = 4
    expected = [(252, 128, 3), (248, 128, 7), (244, 128, 11), (240, 128, 15), (236, 128, 19), (232, 128, 23), (228, 128, 27), (224, 128, 31), (220, 128, 35), (216, 128, 39), (212, 128, 43), (208, 128, 47), (204, 128, 51), (200, 128, 55), (196, 128, 59), (192, 128, 63), (188, 128, 67), (184, 128, 71), (180, 128, 75), (176, 128, 79), (172, 128, 83), (168, 128, 87), (164, 128, 91), (160, 128, 95), (156, 128, 99), (152, 128, 103), (148, 128, 107), (144, 128, 111), (140, 128, 115), (136, 128, 119), (132, 128, 123), (128, 128, 127), (124, 128, 131), (120, 128, 135), (116, 128, 139), (112, 128, 143), (108, 128, 147), (104, 128, 151), (100, 128, 155), (96, 128, 159), (92, 128, 163), (88, 128, 167), (84, 128, 171), (80, 128, 175), (76, 128, 179), (72, 128, 183), (68, 128, 187), (64, 128, 191), (60, 128, 195), (56, 128, 199), (52, 128, 203), (48, 128, 207), (44, 128, 211), (40, 128, 215), (36, 128, 219), (32, 128, 223), (28, 128, 227), (24, 128, 231), (20, 128, 235), (16, 128, 239), (12, 128, 243), (8, 128, 247), (4, 128, 251), (0, 128, 255)]
    return do_test_func5(ID, expected)
# %% ----------------------------------- EX1 ------------------------- #
def do_test_ex1(a_set, n, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            res = program.ex1(a_set, n)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            if res == None:
                raise testlib.NotImplemented()
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex1(a_set, n)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] L'insieme ritornato non è corretto/ The set returned is not correct\n{'*'*50}
                 Expected: {expected}\n
                 Returned: {res}.''')
    return 2

def test_ex1_1():
    '''
    a_set = {'a','b','c'}
    n = 2
    expected = {'ab', 'ba', 'ac', 'ca', 'bc', 'cb'}
    '''
    a_set = {'a','b','c'}
    n = 2
    expected = {'ab', 'ba', 'ac', 'ca', 'bc', 'cb'}
    return do_test_ex1(a_set, n, expected)


def test_ex1_2():
    '''
    a_set = {'a','b','c','d'}
    n = 3
    expected = {'cda', 'bad', 'dac', 'cab', 'bca', 'cdb', 'adc', 'bac', 'dba', 'dcb', 'adb', 'dbc', 'bda', 'abc', 'bcd', 'cba', 'cad', 'dab', 'dca', 'acd', 'acb', 'abd', 'cbd', 'bdc'}
    '''
    a_set = {'a','b','c','d'}
    n = 3
    expected = {'cda', 'bad', 'dac', 'cab', 'bca', 'cdb', 'adc', 'bac', 'dba', 'dcb', 'adb', 'dbc', 'bda', 'abc', 'bcd', 'cba', 'cad', 'dab', 'dca', 'acd', 'acb', 'abd', 'cbd', 'bdc'}
    return do_test_ex1(a_set, n, expected)


def test_ex1_3():
    '''
    a_set = {'a', 'bc', 'def', 'ghij', 'klmno', 'pqrstu', 'vwxyz'}
    n = 4
    '''
    a_set = {'a', 'bc', 'def', 'ghij', 'klmno', 'pqrstu', 'vwxyz'}
    n = 4
    expected = {'defbcklmnoa', 'pqrstuvwxyzdefbc', 'pqrstubcaghij', 'klmnoghijpqrstubc', 'klmnodefpqrstubc', 'klmnoavwxyzpqrstu', 'apqrstuklmnobc', 'avwxyzpqrstubc', 'bcdefpqrstuvwxyz', 'pqrstuklmnovwxyzghij', 'ghijaklmnopqrstu', 'klmnobcghija', 'apqrstudefbc', 'pqrstubcavwxyz', 'defabcklmno', 'bcpqrstughijvwxyz', 'pqrstughijklmnovwxyz', 'klmnopqrstughijdef', 'ghijvwxyzadef', 'bcaghijpqrstu', 'pqrstuklmnoghijbc', 'abcdefvwxyz', 'klmnobcvwxyza', 'vwxyzklmnoaghij', 'klmnovwxyzpqrstubc', 'aklmnovwxyzpqrstu', 'pqrstughijdefklmno', 'aghijbcpqrstu', 'pqrstuklmnodefghij', 'vwxyzpqrstughijklmno', 'klmnopqrstuaghij', 'avwxyzbcdef', 'pqrstudefghijklmno', 'vwxyzbcdefklmno', 'klmnovwxyzapqrstu', 'vwxyzklmnodefbc', 'ghijpqrstudefa', 'bcghijdefpqrstu', 'ghijpqrstudefklmno', 'bcklmnopqrstughij', 'klmnoghijbcpqrstu', 'klmnobcadef', 'avwxyzbcpqrstu', 'vwxyzklmnopqrstubc', 'bcghijvwxyzpqrstu', 'avwxyzghijdef', 'bcapqrstudef', 'defpqrstuklmnobc', 'vwxyzdefbcpqrstu', 'pqrstuaghijbc', 'vwxyzbcghijdef', 'bcdefghija', 'bcpqrstuklmnoa', 'bcdefklmnoa', 'vwxyzghijapqrstu', 'ghijklmnopqrstubc', 'bcvwxyzpqrstughij', 'klmnobcpqrstuvwxyz', 'vwxyzbcklmnodef', 'klmnopqrstudefghij', 'bcpqrstuadef', 'ghijbcklmnodef', 'aghijpqrstudef', 'defklmnoabc', 'defvwxyzklmnopqrstu', 'ghijpqrstubcdef', 'pqrstughijklmnodef', 'pqrstubcdefvwxyz', 'avwxyzpqrstudef', 'pqrstudefvwxyzbc', 'defghijpqrstuklmno', 'klmnoapqrstudef', 'klmnoapqrstubc', 'adefbcvwxyz', 'aghijdefbc', 'pqrstughijavwxyz', 'avwxyzdefbc', 'pqrstuvwxyzdefklmno', 'vwxyzklmnopqrstua', 'klmnopqrstuvwxyzbc', 'pqrstuvwxyzghijklmno', 'bcapqrstughij', 'vwxyzadefbc', 'vwxyzbcklmnoghij', 'klmnovwxyzadef', 'defapqrstughij', 'abcvwxyzklmno', 'klmnoabcvwxyz', 'ghijpqrstuklmnobc', 'bcvwxyzghijpqrstu', 'bcghijadef', 'ghijabcklmno', 'vwxyzpqrstudefghij', 'aklmnobcghij', 'bcvwxyzghijdef', 'ghijklmnovwxyza', 'bcaklmnoghij', 'pqrstughijklmnobc', 'defbcghijpqrstu', 'vwxyzghijbca', 'vwxyzdefbca', 'klmnodefvwxyzghij', 'pqrstubcvwxyzghij', 'pqrstughijdefvwxyz', 'klmnobcpqrstudef', 'pqrstubcklmnoghij', 'klmnoabcpqrstu', 'apqrstubcvwxyz', 'bcdefpqrstuklmno', 'klmnobcvwxyzghij', 'vwxyzghijdefa', 'pqrstuaklmnoghij', 'defapqrstubc', 'pqrstuabcghij', 'adefpqrstuvwxyz', 'vwxyzbcpqrstua', 'vwxyzpqrstuadef', 'ghijaklmnovwxyz', 'ghijvwxyzdefbc', 'defklmnobcvwxyz', 'klmnobcvwxyzdef', 'vwxyzabcklmno', 'defvwxyzghija', 'defghijklmnoa', 'bcdefklmnoghij', 'klmnoabcghij', 'abcpqrstuvwxyz', 'pqrstuklmnoaghij', 'defbcpqrstughij', 'klmnoaghijpqrstu', 'defghijbcpqrstu', 'ghijdefpqrstubc', 'klmnobcdefvwxyz', 'bcpqrstudefklmno', 'vwxyzbcapqrstu', 'abcklmnoghij', 'vwxyzdefghijklmno', 'pqrstughijbcvwxyz', 'pqrstuavwxyzghij', 'vwxyzklmnobcdef', 'ghijbcvwxyzklmno', 'ghijabcdef', 'klmnovwxyzghijpqrstu', 'defavwxyzbc', 'ghijbcavwxyz', 'bcghijvwxyzklmno', 'bcghijpqrstuklmno', 'klmnopqrstudefa', 'bcdefklmnovwxyz', 'vwxyzbcdefa', 'defbcvwxyzpqrstu', 'pqrstughijdefbc', 'ghijbcpqrstua', 'bcklmnodefa', 'defpqrstubcvwxyz', 'avwxyzdefghij', 'vwxyzbcadef', 'adefvwxyzghij', 'vwxyzdefklmnoa', 'ghijdefvwxyza', 'bcklmnoadef', 'abcvwxyzdef', 'vwxyzklmnoghijdef', 'vwxyzdefpqrstuklmno', 'ghijapqrstuklmno', 'defbcghijklmno', 'klmnoaghijvwxyz', 'pqrstuadefklmno', 'klmnovwxyzaghij', 'klmnoapqrstuvwxyz', 'aklmnodefbc', 'aklmnodefvwxyz', 'vwxyzghijklmnobc', 'ghijdefpqrstua', 'bcaklmnodef', 'avwxyzpqrstughij', 'bcdefghijklmno', 'bcdefvwxyza', 'defklmnoaghij', 'klmnovwxyzbcpqrstu', 'ghijvwxyzklmnobc', 'bcvwxyzpqrstudef', 'vwxyzaklmnopqrstu', 'defghijbcvwxyz', 'apqrstuklmnoghij', 'vwxyzbcklmnopqrstu', 'pqrstuavwxyzbc', 'vwxyzklmnobcpqrstu', 'ghijbcvwxyza', 'bcapqrstuvwxyz', 'pqrstuklmnodefa', 'ghijadefklmno', 'klmnoghijvwxyzbc', 'pqrstubcklmnovwxyz', 'vwxyzghijdefpqrstu', 'ghijpqrstuabc', 'defghijpqrstua', 'defghijklmnopqrstu', 'klmnodefbcghij', 'defabcvwxyz', 'klmnoadefpqrstu', 'ghijvwxyzbcpqrstu', 'pqrstuvwxyzbcghij', 'pqrstuaghijvwxyz', 'vwxyzapqrstuklmno', 'defbcvwxyza', 'bcpqrstudefghij', 'vwxyzghijaklmno', 'ghijpqrstubca', 'bcdefghijpqrstu', 'bcklmnopqrstudef', 'defpqrstuvwxyzbc', 'ghijvwxyzabc', 'pqrstudefbca', 'defbcvwxyzklmno', 'ghijdefbcvwxyz', 'vwxyzapqrstughij', 'ghijvwxyzklmnoa', 'vwxyzghijklmnodef', 'ghijklmnovwxyzdef', 'pqrstuklmnoabc', 'bcpqrstuklmnoghij', 'pqrstughijvwxyza', 'pqrstudefavwxyz', 'defklmnopqrstubc', 'bcavwxyzghij', 'defklmnovwxyzbc', 'aklmnopqrstudef', 'pqrstudefklmnobc', 'ghijpqrstubcklmno', 'klmnovwxyzdefpqrstu', 'ghijpqrstuvwxyzbc', 'defabcpqrstu', 'defpqrstuvwxyzghij', 'klmnobcpqrstua', 'ghijdefapqrstu', 'abcpqrstudef', 'ghijdefvwxyzklmno', 'klmnovwxyzpqrstua', 'klmnodefvwxyzpqrstu', 'klmnopqrstudefbc', 'bcdefpqrstua', 'ghijbcdefa', 'adefpqrstuklmno', 'pqrstuklmnoghijvwxyz', 'pqrstubcdefklmno', 'ghijbcpqrstudef', 'adefvwxyzbc', 'klmnoghijdefa', 'apqrstughijdef', 'ghijapqrstudef', 'klmnobcpqrstughij', 'adefpqrstughij', 'aghijvwxyzdef', 'pqrstughijklmnoa', 'pqrstudefklmnoghij', 'klmnoaghijbc', 'pqrstuaklmnodef', 'ghijdefaklmno', 'aklmnobcpqrstu', 'vwxyzpqrstudefbc', 'vwxyzpqrstughijbc', 'ghijdefbcpqrstu', 'bcklmnoghija', 'aklmnopqrstuvwxyz', 'pqrstuklmnovwxyza', 'ghijklmnodefvwxyz', 'bcpqrstuaghij', 'defbcpqrstuklmno', 'pqrstuaghijklmno', 'vwxyzdefghijbc', 'vwxyzbcaklmno', 'defbcpqrstuvwxyz', 'vwxyzdefpqrstubc', 'defklmnovwxyza', 'vwxyzpqrstughijdef', 'ghijklmnoapqrstu', 'klmnobcvwxyzpqrstu', 'abcghijklmno', 'bcklmnodefghij', 'defbcklmnovwxyz', 'aghijpqrstuvwxyz', 'defghijapqrstu', 'bcvwxyzpqrstua', 'aklmnobcvwxyz', 'defghijklmnovwxyz', 'ghijpqrstuaklmno', 'ghijavwxyzdef', 'pqrstuvwxyzklmnobc', 'klmnoapqrstughij', 'bcpqrstughija', 'defpqrstuvwxyza', 'klmnopqrstuabc', 'pqrstudefklmnovwxyz', 'bcpqrstuavwxyz', 'ghijpqrstuvwxyza', 'defvwxyzpqrstuklmno', 'defvwxyzklmnoghij', 'aklmnovwxyzghij', 'pqrstuvwxyzdefa', 'ghijbcpqrstuklmno', 'pqrstubcghija', 'vwxyzdefklmnoghij', 'defapqrstuklmno', 'vwxyzapqrstudef', 'bcavwxyzpqrstu', 'klmnopqrstubcdef', 'bcadefklmno', 'ghijavwxyzklmno', 'ghijbcapqrstu', 'bcghijpqrstuvwxyz', 'defklmnobca', 'ghijavwxyzpqrstu', 'defvwxyzaghij', 'vwxyzpqrstughija', 'defbcghija', 'abcghijvwxyz', 'pqrstughijbcklmno', 'adefbcklmno', 'klmnodefaghij', 'defvwxyzpqrstughij', 'vwxyzaklmnobc', 'bcaghijdef', 'defklmnovwxyzghij', 'klmnodefvwxyza', 'ghijvwxyzpqrstuklmno', 'ghijadefbc', 'defklmnobcghij', 'klmnoghijadef', 'vwxyzklmnopqrstughij', 'ghijbcvwxyzpqrstu', 'klmnopqrstubcvwxyz', 'avwxyzdefpqrstu', 'bcvwxyzadef', 'apqrstubcdef', 'vwxyzdefklmnopqrstu', 'vwxyzaghijdef', 'bcklmnovwxyzghij', 'klmnopqrstuvwxyzdef', 'bcpqrstughijdef', 'pqrstubcghijklmno', 'bcpqrstuvwxyzdef', 'vwxyzapqrstubc', 'defpqrstuvwxyzklmno', 'bcklmnodefpqrstu', 'klmnovwxyzdefa', 'klmnoghijvwxyzdef', 'klmnoghijpqrstua', 'adefghijpqrstu', 'pqrstubcghijdef', 'klmnoghijdefvwxyz', 'pqrstudefaklmno', 'vwxyzghijadef', 'avwxyzbcklmno', 'defghijavwxyz', 'defghijvwxyzpqrstu', 'pqrstudefabc', 'klmnobcavwxyz', 'defavwxyzklmno', 'pqrstughijadef', 'aghijklmnodef', 'bcghijklmnovwxyz', 'ghijaklmnodef', 'defbcghijvwxyz', 'ghijklmnopqrstudef', 'klmnovwxyzpqrstughij', 'vwxyzbcdefghij', 'pqrstughijbca', 'pqrstudefklmnoa', 'ghijklmnopqrstuvwxyz', 'avwxyzklmnodef', 'ghijbcpqrstuvwxyz', 'bcghijpqrstudef', 'defklmnoghijbc', 'vwxyzabcghij', 'klmnoavwxyzghij', 'vwxyzklmnodefa', 'ghijdefavwxyz', 'defghijvwxyza', 'apqrstubcklmno', 'bcghijdefa', 'aklmnoghijpqrstu', 'pqrstudefvwxyzklmno', 'vwxyzaghijbc', 'klmnoghijdefbc', 'ghijklmnobcvwxyz', 'bcvwxyzdefpqrstu', 'pqrstuklmnobcdef', 'ghijdefbca', 'klmnodefghijvwxyz', 'bcvwxyzklmnodef', 'defvwxyzbcpqrstu', 'aghijpqrstuklmno', 'adefvwxyzpqrstu', 'abcpqrstuklmno', 'klmnoadefbc', 'ghijvwxyzklmnodef', 'ghijvwxyzbcklmno', 'pqrstudefaghij', 'klmnodefghija', 'defvwxyzpqrstubc', 'apqrstuklmnovwxyz', 'pqrstuklmnovwxyzbc', 'bcadefpqrstu', 'pqrstuvwxyzaklmno', 'adefklmnobc', 'pqrstuklmnobcvwxyz', 'avwxyzbcghij', 'vwxyzghijklmnopqrstu', 'defklmnoghijpqrstu', 'aklmnoghijvwxyz', 'vwxyzdefapqrstu', 'vwxyzklmnobca', 'defpqrstubcghij', 'klmnodefpqrstua', 'klmnodefpqrstughij', 'defaklmnopqrstu', 'aklmnopqrstubc', 'bcklmnopqrstua', 'vwxyzklmnopqrstudef', 'klmnopqrstuavwxyz', 'ghijavwxyzbc', 'defpqrstuklmnovwxyz', 'abcdefpqrstu', 'ghijdefabc', 'adefklmnoghij', 'defklmnobcpqrstu', 'vwxyzadefghij', 'ghijvwxyzbca', 'pqrstubcdefa', 'ghijklmnovwxyzpqrstu', 'bcpqrstudefvwxyz', 'vwxyzdefklmnobc', 'pqrstuaklmnobc', 'ghijapqrstubc', 'bcdefghijvwxyz', 'vwxyzpqrstubcdef', 'klmnopqrstughija', 'pqrstuvwxyzghijdef', 'vwxyzklmnoapqrstu', 'defklmnoghijvwxyz', 'pqrstuabcklmno', 'defghijabc', 'vwxyzklmnoadef', 'ghijadefvwxyz', 'bcghijaklmno', 'avwxyzklmnopqrstu', 'aghijdefpqrstu', 'ghijdefklmnopqrstu', 'vwxyzpqrstuklmnoa', 'pqrstubcadef', 'klmnovwxyzbcdef', 'bcdefaklmno', 'ghijabcvwxyz', 'avwxyzghijbc', 'defvwxyzabc', 'apqrstughijklmno', 'defbcapqrstu', 'klmnodefapqrstu', 'bcpqrstughijklmno', 'avwxyzklmnobc', 'defpqrstuaklmno', 'vwxyzghijbcpqrstu', 'pqrstubcklmnoa', 'klmnopqrstubcghij', 'bcadefvwxyz', 'pqrstudefghijvwxyz', 'bcaghijvwxyz', 'ghijdefpqrstuvwxyz', 'vwxyzdefaghij', 'aklmnopqrstughij', 'ghijbcklmnopqrstu', 'abcvwxyzghij', 'defaghijklmno', 'defvwxyzklmnoa', 'vwxyzghijklmnoa', 'apqrstuvwxyzdef', 'ghijbcadef', 'bcvwxyzpqrstuklmno', 'defpqrstuavwxyz', 'ghijadefpqrstu', 'aklmnodefpqrstu', 'bcpqrstuklmnodef', 'bcvwxyzklmnoghij', 'abcklmnopqrstu', 'defavwxyzghij', 'defpqrstuklmnoa', 'aghijbcdef', 'defghijvwxyzklmno', 'vwxyzpqrstudefklmno', 'vwxyzdefbcklmno', 'apqrstuvwxyzbc', 'ghijbcklmnoa', 'ghijpqrstubcvwxyz', 'vwxyzaghijpqrstu', 'aklmnovwxyzbc', 'pqrstuvwxyzdefghij', 'vwxyzaklmnoghij', 'apqrstughijvwxyz', 'klmnodefavwxyz', 'adefbcpqrstu', 'abcklmnovwxyz', 'pqrstuadefghij', 'aghijvwxyzbc', 'defklmnovwxyzpqrstu', 'defghijaklmno', 'ghijklmnodefpqrstu', 'pqrstughijabc', 'adefklmnopqrstu', 'pqrstughijbcdef', 'ghijpqrstudefvwxyz', 'klmnovwxyzbca', 'defpqrstuabc', 'pqrstuabcdef', 'ghijvwxyzpqrstudef', 'ghijklmnobca', 'vwxyzbcklmnoa', 'bcdefavwxyz', 'bcapqrstuklmno', 'bcghijavwxyz', 'defpqrstuklmnoghij', 'klmnoghijbcvwxyz', 'apqrstuklmnodef', 'aklmnovwxyzdef', 'vwxyzghijdefklmno', 'defklmnopqrstughij', 'pqrstubcklmnodef', 'vwxyzpqrstubcklmno', 'vwxyzklmnoghijpqrstu', 'ghijklmnoabc', 'adefklmnovwxyz', 'ghijpqrstuvwxyzklmno', 'ghijbcdefpqrstu', 'avwxyzklmnoghij', 'vwxyzabcdef', 'klmnoghijapqrstu', 'pqrstughijdefa', 'defvwxyzapqrstu', 'adefpqrstubc', 'pqrstuklmnovwxyzdef', 'bcvwxyzghijklmno', 'aghijvwxyzklmno', 'bcpqrstuaklmno', 'vwxyzklmnodefghij', 'ghijvwxyzklmnopqrstu', 'klmnovwxyzbcghij', 'klmnobcghijvwxyz', 'bcklmnodefvwxyz', 'bcghijklmnoa', 'vwxyzghijbcdef', 'defpqrstughija', 'vwxyzbcpqrstudef', 'klmnovwxyzghija', 'pqrstuvwxyzklmnoa', 'vwxyzklmnoghija', 'defaghijpqrstu', 'defaklmnoghij', 'aghijvwxyzpqrstu', 'bcpqrstuvwxyza', 'bcdefapqrstu', 'defbcklmnopqrstu', 'defbcklmnoghij', 'pqrstudefbcvwxyz', 'vwxyzpqrstubcghij', 'vwxyzbcaghij', 'abcdefghij', 'defpqrstuaghij', 'bcklmnovwxyzdef', 'vwxyzghijdefbc', 'bcghijklmnodef', 'ghijpqrstudefbc', 'bcklmnopqrstuvwxyz', 'pqrstuklmnoavwxyz', 'pqrstuaklmnovwxyz', 'avwxyzghijpqrstu', 'vwxyzklmnodefpqrstu', 'vwxyzpqrstuaghij', 'bcklmnovwxyza', 'ghijvwxyzapqrstu', 'klmnovwxyzdefbc', 'aghijpqrstubc', 'ghijklmnodefbc', 'vwxyzghijpqrstubc', 'klmnobcaghij', 'vwxyzdefghijpqrstu', 'ghijdefpqrstuklmno', 'bcvwxyzaklmno', 'defaghijbc', 'pqrstudefvwxyzghij', 'pqrstuadefvwxyz', 'bcvwxyzklmnoa', 'defbcpqrstua', 'bcvwxyzdefghij', 'vwxyzdefpqrstua', 'bcvwxyzghija', 'klmnoghijabc', 'ghijklmnobcpqrstu', 'bcghijapqrstu', 'ghijapqrstuvwxyz', 'defghijklmnobc', 'adefbcghij', 'aklmnobcdef', 'defpqrstughijbc', 'ghijklmnopqrstua', 'ghijklmnovwxyzbc', 'vwxyzbcpqrstughij', 'klmnoabcdef', 'klmnoadefvwxyz', 'vwxyzghijpqrstudef', 'ghijvwxyzbcdef', 'apqrstughijbc', 'pqrstuvwxyzaghij', 'klmnodefvwxyzbc', 'defklmnoghija', 'defklmnopqrstua', 'bcklmnoghijvwxyz', 'vwxyzpqrstudefa', 'ghijpqrstuavwxyz', 'bcklmnoavwxyz', 'klmnopqrstuvwxyza', 'klmnobcdefghij', 'pqrstuvwxyzbcdef', 'defbcaghij', 'bcklmnovwxyzpqrstu', 'abcpqrstughij', 'pqrstuklmnoghija', 'pqrstughijvwxyzdef', 'defpqrstughijvwxyz', 'defvwxyzklmnobc', 'apqrstuvwxyzklmno', 'vwxyzbcghijklmno', 'vwxyzdefaklmno', 'bcvwxyzapqrstu', 'pqrstuavwxyzdef', 'klmnovwxyzdefghij', 'ghijvwxyzdefa', 'defvwxyzpqrstua', 'defbcavwxyz', 'defaklmnobc', 'ghijbcdefvwxyz', 'bcghijpqrstua', 'klmnoghijdefpqrstu', 'klmnodefbca', 'pqrstughijvwxyzklmno', 'pqrstuvwxyzklmnodef', 'ghijklmnoadef', 'apqrstuvwxyzghij', 'defvwxyzbcghij', 'klmnodefbcpqrstu', 'pqrstuaghijdef', 'vwxyzklmnoabc', 'vwxyzadefklmno', 'vwxyzaklmnodef', 'defaklmnovwxyz', 'abcklmnodef', 'pqrstuvwxyzghijbc', 'vwxyzbcghija', 'klmnopqrstudefvwxyz', 'defghijpqrstubc', 'vwxyzaghijklmno', 'ghijabcpqrstu', 'klmnobcapqrstu', 'vwxyzghijpqrstua', 'adefghijklmno', 'ghijklmnoavwxyz', 'aklmnodefghij', 'ghijvwxyzdefpqrstu', 'ghijpqrstuklmnovwxyz', 'bcdefaghij', 'adefghijbc', 'pqrstuavwxyzklmno', 'ghijvwxyzaklmno', 'avwxyzghijklmno', 'vwxyzghijpqrstuklmno', 'bcklmnoghijdef', 'vwxyzbcdefpqrstu', 'pqrstuvwxyzabc', 'bcdefvwxyzklmno', 'vwxyzdefghija', 'abcdefklmno', 'klmnovwxyzabc', 'defpqrstughijklmno', 'bcaklmnopqrstu', 'apqrstudefvwxyz', 'vwxyzpqrstuklmnoghij', 'pqrstudefghijbc', 'bcklmnoaghij', 'bcaklmnovwxyz', 'avwxyzdefklmno', 'pqrstudefghija', 'vwxyzpqrstuklmnobc', 'defvwxyzbca', 'defklmnoavwxyz', 'defklmnopqrstuvwxyz', 'defvwxyzghijklmno', 'bcpqrstudefa', 'ghijklmnobcdef', 'ghijbcaklmno', 'bcghijvwxyzdef', 'aghijdefklmno', 'adefghijvwxyz', 'pqrstubcvwxyza', 'defbcvwxyzghij', 'aghijbcklmno', 'bcklmnoghijpqrstu', 'apqrstudefklmno', 'pqrstubcghijvwxyz', 'bcklmnoapqrstu', 'vwxyzklmnobcghij', 'pqrstubcvwxyzklmno', 'bcdefklmnopqrstu', 'pqrstubcaklmno', 'ghijvwxyzdefklmno', 'bcghijvwxyza', 'defabcghij', 'defavwxyzpqrstu', 'vwxyzdefabc', 'klmnoaghijdef', 'bcadefghij', 'pqrstughijaklmno', 'ghijbcvwxyzdef', 'defghijbcklmno', 'ghijbcklmnovwxyz', 'klmnoadefghij', 'defghijvwxyzbc', 'klmnobcdefa', 'aklmnoghijdef', 'adefvwxyzklmno', 'pqrstuklmnoadef', 'ghijaklmnobc', 'pqrstuklmnobcghij', 'defbcaklmno', 'aghijbcvwxyz', 'aghijklmnovwxyz', 'bcpqrstuvwxyzghij', 'vwxyzpqrstuklmnodef', 'ghijvwxyzpqrstua', 'pqrstughijvwxyzbc', 'pqrstuvwxyzghija', 'ghijdefklmnobc', 'bcdefpqrstughij', 'ghijpqrstuklmnodef', 'klmnopqrstughijbc', 'vwxyzbcpqrstuklmno', 'ghijpqrstuklmnoa', 'ghijdefbcklmno', 'bcdefvwxyzghij', 'apqrstudefghij', 'ghijdefklmnoa', 'abcvwxyzpqrstu', 'bcvwxyzdefklmno', 'pqrstubcdefghij', 'defapqrstuvwxyz', 'aghijklmnopqrstu', 'bcdefvwxyzpqrstu', 'vwxyzpqrstubca', 'bcghijdefvwxyz', 'pqrstuadefbc', 'pqrstubcvwxyzdef', 'vwxyzpqrstuaklmno', 'pqrstuklmnoghijdef', 'defklmnoapqrstu', 'pqrstudefbcklmno', 'vwxyzghijbcklmno', 'ghijdefvwxyzbc', 'defpqrstubca', 'klmnobcghijpqrstu', 'defghijbca', 'pqrstuvwxyzadef', 'klmnodefpqrstuvwxyz', 'vwxyzklmnoghijbc', 'ghijklmnodefa', 'ghijvwxyzpqrstubc', 'defvwxyzbcklmno', 'defvwxyzaklmno', 'defvwxyzghijpqrstu', 'defaghijvwxyz', 'defvwxyzghijbc', 'klmnopqrstughijvwxyz', 'klmnoghijbcdef', 'ghijdefklmnovwxyz', 'defghijpqrstuvwxyz', 'klmnopqrstuvwxyzghij', 'pqrstuvwxyzbcklmno', 'aghijdefvwxyz', 'klmnoghijpqrstuvwxyz', 'klmnovwxyzghijdef', 'abcghijpqrstu', 'pqrstuklmnodefbc', 'vwxyzdefpqrstughij', 'klmnovwxyzghijbc', 'bcpqrstuvwxyzklmno', 'klmnodefabc', 'aklmnoghijbc', 'bcaghijklmno', 'vwxyzpqrstuabc', 'klmnoghijbca', 'pqrstuvwxyzbca', 'bcpqrstuklmnovwxyz', 'avwxyzpqrstuklmno', 'vwxyzbcghijpqrstu', 'vwxyzabcpqrstu', 'klmnoavwxyzdef', 'klmnodefbcvwxyz', 'klmnoghijvwxyzpqrstu', 'ghijdefvwxyzpqrstu', 'klmnobcghijdef', 'klmnopqrstuadef', 'abcghijdef', 'klmnobcdefpqrstu', 'ghijpqrstuadef', 'bcavwxyzdef', 'defpqrstubcklmno', 'ghijbcdefklmno', 'vwxyzdefbcghij', 'aghijklmnobc', 'pqrstudefvwxyza', 'bcghijklmnopqrstu', 'vwxyzghijabc', 'apqrstubcghij', 'bcavwxyzklmno', 'bcvwxyzdefa', 'klmnoavwxyzbc', 'bcvwxyzaghij', 'vwxyzadefpqrstu', 'pqrstudefbcghij', 'klmnoghijvwxyza', 'pqrstuklmnodefvwxyz', 'klmnoghijavwxyz', 'bcvwxyzklmnopqrstu', 'klmnoghijpqrstudef', 'bcghijdefklmno', 'klmnodefghijpqrstu', 'pqrstuklmnobca', 'klmnovwxyzpqrstudef', 'pqrstuabcvwxyz', 'pqrstuvwxyzklmnoghij', 'klmnopqrstubca', 'ghijpqrstuvwxyzdef', 'klmnodefghijbc'}
    return do_test_ex1(a_set, n, expected)

# %% ----------------------------------- EX2 ------------------------- #
import tree
def do_ex2_test(root, m, n, k, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex2(root, m, n, k)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex2(root, m, n, k)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR]Il valore ritornato non è corretto! / The returned value is incorrect!!\nReturned={res}, expected={expected}''')
        return 0
    return 2


def test_ex2_1():
    '''
        root
    ______5______
   |             |
   8__        ___2___
      |      |       |
     _3_     9       1
    |   |
    6   12

    m=1
    n=2
    k=3
    expected = 2
    '''
    root = tree.BinaryTree.fromList([5, [8, None, [3, [6, None, None], [12, None, None]]], [2, [9, None, None],[1, None, None]]])
    m=1
    n=2
    k=3
    expected = 2
    return do_ex2_test(root, m, n, k, expected)

def test_ex2_2():
    '''
              root
          ______2______
         |             |
      __ 7__        ___5___
     |      |      |       |
    _4_     3_    _0_     _5_
   |   |      |  |   |   |   |
   2   -1     1  8   3   2   9

    m=0
    n=4
    k=2
    expected = 6
    '''
    root = tree.BinaryTree.fromList([2, [7, [4, [2, None, None], [-1, None, None]], [3, None, [1, None, None]]], [5, [0, [8, None, None], [3, None, None]], [5, [2, None, None], [9, None, None]]]])
    m=0
    n=4
    k=2
    expected = 6
    return do_ex2_test(root, m, n, k, expected)


def test_ex2_3():
    '''
    A big tree
    m=3
    n=7
    k=3
    expected = 38
    '''
    root = tree.BinaryTree.fromList([-2, [5, [13, [-7, [2, [26, [27, [10, [0, None, [24, None, None]], [14, None, None]], [13, [30, [2, None, None], None], [-3, None, [-1, None, None]]]], [10, [28, None, None], [-1, [-3, [30, None, None], [-9, None, None]], [19, None, None]]]], None], [8, [11, [-2, [4, None, None], [5, None, None]], [6, [24, None, None], [19, None, None]]], [9, None, [1, [18, None, [-3, None, None]], [22, None, [-10, [5, None, None], None]]]]]], [17, [12, [26, [10, [21, None, [1, None, None]], [26, None, [30, None, None]]], [-3, [-2, [-3, None, [-2, [28, None, None], [21, None, None]]], [7, [-4, None, None], None]], [-1, [2, [18, None, None], [-2, None, None]], [24, [4, None, None], [30, [-4, None, None], None]]]]], [-2, [16, None, [9, [17, [23, None, None], None], [21, None, None]]], [-8, [2, None, [-10, None, None]], [20, [21, [7, None, None], [-5, [20, None, None], None]], [0, None, [-4, None, None]]]]]], [-1, None, [6, [30, [22, None, None], None], [28, [-4, None, None], [-10, None, None]]]]]], [-5, [13, [20, None, [17, [17, [25, [4, [5, [-4, [21, None, None], None], None], [-3, [21, None, None], None]], None], [14, [-10, [5, None, [28, [15, [7, None, [12, None, None]], [7, None, None]], [24, None, [-2, None, None]]]], [-4, [2, None, None], [14, None, None]]], [10, None, [7, [12, None, None], [19, [0, None, None], None]]]]], None]], [5, [2, [14, [3, None, None], [0, None, None]], [5, [15, None, [15, None, None]], [22, [15, None, None], [6, None, None]]]], None]], [-7, [-7, [14, [5, [24, None, [3, [4, [10, None, None], None], [27, None, None]]], [-5, [30, None, None], [24, None, None]]], [-8, [4, [-10, [10, [27, None, None], [5, None, [14, None, None]]], [10, [27, None, None], [16, None, None]]], [15, [20, None, None], [28, None, [-7, [-5, None, None], [10, None, None]]]]], [25, [17, [7, [19, None, None], [-4, [3, None, None], [12, None, None]]], [12, [23, None, None], [2, None, None]]], [20, [4, None, None], [22, [22, None, None], [21, [27, None, None], None]]]]]], [9, [12, [6, [-4, [-2, None, None], [11, None, [18, None, None]]], [25, [11, None, None], [25, None, None]]], [7, [10, [6, [18, None, None], [18, None, [0, None, None]]], [30, [5, None, None], None]], [8, None, [25, [2, None, [-4, None, None]], [-2, [27, None, None], [-4, None, None]]]]]], [1, [-9, [-10, [26, [17, None, None], None], [28, [-2, [22, None, None], None], [-6, None, [30, None, None]]]], [28, [19, [-3, None, [25, None, [10, None, None]]], [8, None, [4, None, None]]], [11, [8, None, None], [24, None, [-10, None, None]]]]], [26, [29, [-10, None, None], [-6, None, None]], None]]]], [-2, [20, [-10, [2, None, [28, [-9, [11, None, None], None], [1, None, None]]], [13, [10, None, None], [-2, None, None]]], [-4, [19, [-9, None, [-1, None, None]], [-8, [12, [21, None, None], [8, None, None]], [3, [7, None, [17, None, None]], [23, None, None]]]], [25, [3, [19, None, [-4, [25, None, None], None]], [-10, None, None]], [12, [4, [-10, None, None], None], [18, [15, [27, None, None], [-2, None, None]], [13, None, None]]]]]], [-6, [29, [17, [-4, None, [-5, None, None]], [-2, [-3, None, [-8, None, None]], [-7, None, None]]], [8, [11, [21, [-3, None, [2, None, None]], [2, None, None]], [-6, None, None]], None]], [-9, [29, [23, None, [25, [20, None, None], None]], [30, [24, [6, [25, None, None], [24, None, None]], [2, [25, None, None], [-9, [3, None, None], None]]], [16, [0, None, [-1, None, None]], [30, None, None]]]], [28, [25, [5, [3, None, None], [9, [4, None, None], None]], [-8, None, [21, None, None]]], [23, [16, [-7, [7, None, None], [12, None, None]], [16, None, [16, None, None]]], [-8, [24, None, [5, None, None]], [2, [23, None, None], [14, None, None]]]]]]]]]]], [20, [20, [19, [-2, [-1, [3, [24, [12, None, None], None], [5, None, None]], [10, None, None]], [27, [29, [24, None, None], None], [30, [-9, [4, None, None], None], None]]], [-10, [21, [26, [24, None, None], None], [5, None, [18, None, None]]], [-4, [1, None, None], [1, None, None]]]], [23, [2, [4, [21, None, [30, None, None]], None], [16, [-8, None, None], [6, None, None]]], [14, [12, None, [27, [-5, None, None], [10, None, None]]], [6, [18, None, None], [3, None, None]]]]], None]] )
    m=3
    n=7
    k=3
    expected = 38
    return do_ex2_test(root, m, n, k, expected)

################################################################################
# %% --------------------- TESTS ---------------------
tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1, test_func1_2, test_func1_3, test_func1_4,
    test_func2_1, test_func2_2, test_func2_3, test_func2_4,
    test_func3_1, test_func3_2, test_func3_3,
    test_func4_1, test_func4_2, test_func4_3,
    test_func5_1, test_func5_2, test_func5_3, test_func5_4,
#    test_ex1_1,  test_ex1_2,  test_ex1_3,
#    test_ex2_1,    test_ex2_2, test_ex2_3,
    test_personal_data_entry,
]

if __name__ == '__main__':
    if test_personal_data_entry() < 0:
        print(f"{COL['RED']}PERSONAL INFO MISSING. PLEASE FILL THE INITIAL VARS WITH YOUR NAME SURNAME AND STUDENT_ID{COL['RST']}")
        sys.exit()
    testlib.runtests(   tests,
                        verbose=True,
                        logfile='grade.csv',
                        stack_trace=DEBUG)
    testlib.check_exam_constraints()
    if 'matricola' in program.__dict__:
        print(f"{COL['GREEN']}Nome: {program.nome}\nCognome: {program.cognome}\nMatricola: {program.matricola}{COL['RST']}")
    elif 'student_id' in program.__dict__:
        print(f"{COL['GREEN']}Name: {program.name}\nSurname: {program.surname}\nStudentID: {program.student_id}{COL['RST']}")
    else:
        print('we should not arrive here the  matricola/student ID variable is not present in program.py')
################################################################################
