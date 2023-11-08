#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Steps to do FIRST:
 1) save this file as program.py
 2) assign the variables below with your
    FIRST NAME, LAST NAME, STUDENT ID (Sapienza matriculation number)

To pass the exam it is necessary to:
    - !!!fill in your personal information in the variables below!!!
    - AND solve at least 1 ex-type exercise (recursive problem)
    - AND solve at least 3 func-type exercises
    - AND obtain a score greater than or equal to 18

The final score is the sum of the scores of the solved problems.
"""

name       = 'NAME'
surname    = 'SURNAME'
student_id = 'STUDENT_ID'    # your Sapienza registration number

################################################################################
################################################################################
################################################################################
# ---------------------------- DEBUG SUGGESTIONS ----------------------------- #
# To run only some of the tests, you can comment the entries with which the
# 'tests' list is assigned at the end of grade.py
#
# To debug recursive functions you can turn off the recursive test setting
# DEBUG=True in the file grade.py
#
# DEBUG=True turns on also the STACK TRACE that allows you to know which
# line number in program.py generated the error.
################################################################################

#%% ---------------------------- FUNC 1 ---------------------------- #

'''
Func 1: 2 points

Define the function func1(int_list, keys) that takes as input an
'int_list' list and a set 'keys' containing integers. The function
returns a dictionary in which the keys are the integers from 'keys'
and the values are lists with the integers from 'int_list' divisible
by the corresponding key.  The lists are sorted in descending order.


Example: if int_list=[4, 6, 10, 13] and keys={2, 3, 5}
  the invocation of func1(int_list, keys) must return the dictionary
  {2:[10, 6, 4], 3:[6], 5:[10]}
'''

def func1(int_list, keys):
    # INSERT HERE YOUR CODE
    pass

# int_list=[4, 6, 10, 13]
# keys={2, 3, 5}

# print(func1(int_list, keys))


#%% ---------------------------- FUNC 2 ---------------------------- #
'''
Define a function func2(a_string, char) that takes as input two
strings 'a_string' and 'char' and returns another string. The string
'char' consists of only one character.
The new string has all the characters of the string 'a_string' with a
value unicode strictly greater than the value of the character in
'char'. The characters in the output string are repeated once and in
inverse alphabetical order.  It is suggested that the ord function be
used to determine the unicode value of a character.

Example: if a_string='impossible' the invocation of func2(a_string, 'i') should
         return the string 'spoml'
'''

def func2(a_string, char):
    # INSERT HERE YOUR CODE
    pass

# print(func2('impossible', 'i'))


# ---------------------------- FUNC 3 ---------------------------- #
'''
Func 3: 3 points
Define a function func3(string_list1, string_list2) that takes as
input two lists of strings and returns a new list of strings.  The new
list consists of all those strings in one of the two input lists that
contain as a substring at least one string or an inverted string from
the other list.  The resulting list must be sorted in descending order
by number of characters, in case of equality, in alphabetical order.

Example: if string_list1=['shop', 'park', 'elichopter', 'cat', 'elephant'] and
            string_list2=['ark', 'contact', 'hop', 'mark']
         the invocation of func3(string_list1, string_list2) shall return
         the list ['elichopter','contact','park', 'shop']

         In fact:
             'elichopter' contains 'hop',
             'contact' contains the inverted string of 'cat'
             'park' contains 'ark'
             'shop' contains 'hop'
'''

def func3(string_list1, string_list2):
    # INSERT HERE YOUR CODE
    pass

# string_list1=['shop', 'park', 'elichopter', 'cat', 'elephant']
# string_list2=['ark', 'contact', 'hop', 'mark']
# print(func3(string_list1, string_list2))


#%% ---------------------------- FUNC 4 ---------------------------- #
'''
Func 4: 6 points
Write a function func4(input_file, output_file) that takes in
input two strings, 'input_file' and 'output_file' representing
the paths to two files.
For each line in the file pointed to by 'input_file', you have to
create a line within a new file pointed to by 'output_file'.  In each
line of the file pointed to by 'input_file' there are a series of of
words composed of numeric and alphabetic characters, separated by
spaces and tabs. For each word, the function locates the numeric
characters, transforms them into integers and sums them
together. Next, the function calculates the product of all the values
obtained for that row, writing the result in the form of a string in a
new line in the 'output_file' file.  Each word has at least one
numeric character.

The function must return the sum of all calculated products.

Example: if the contents of the 'input_file' file are as follows.
car13 5park5 spike2
no1ne rebel44 ni4ce

the invocation of func4('input_file', 'output_file') will have to
write into the 'output_file' file the two lines
80
32

and return the value 112.

'''


def func4(input_file, output_file):
    # INSERT HERE YOUR CODE
    pass

# print(func4('func4/func4_test1.txt','func4/func4_out1.txt'))
# print(func4('func4/func4_test2.txt','func4/func4_out2.txt'))
# print(func4('func4/func4_test3.txt','func4/func4_out3.txt'))

#%% ---------------------------- FUNC 5 ---------------------------- #


'''
Func 5: 8 points

Let us define a function func5(input_pngfile) that takes as input
a string that contains the path to a file with an image in
PNG format.
The image given by 'input_pngfile' contains horizontal segments of
uniform color on a black background. A line can contain multiple
segments of different colors, even attached to each
other.
The function must locate all the segments present in the image and
return a list of triples representing the colors of the identified
segments, ordered from longest to shortest. In the case of segments of
equal length, the colors should be ordered considering the order of
the third component, then of the second, and finally of the first
one. The components follow an ascending order.  In case of segments of
equal color, one should consider the one with the longest greatest.

Example: in the image of the file func5/image01.png there are four segments
         one of length 50 with color (0, 128, 200)
         one of length 30 with color (200, 128, 200)
         one of length 30 with color (200, 200, 128)
         one of length 29 with color (0, 128, 200),
         so func5('func5/image01.png') must return the list
         [(0, 128, 200), (200, 200, 128), (200, 128, 200)]
'''

import images


def func5(input_pngfile):
    # INSERT HERE YOUR CODE
    pass

# print(func5('func5/image01.png'))
# print(func5('func5/image02.png'))
# print(func5('func5/image03.png'))
# print(func5('func5/image04.png'))


# ---------------------------- EX 1 ---------------------------- #

'''
Ex1: recursive, 6 points

Write a recursive function ex1(a_set, n), or that within it uses a
recursive function, which takes as input a set of strings 'a_set' and
an integer 'n' and returns a new set. The set must contain all the
possible strings obtained by concatenating n elements belonging to
from a_set, without repetition.
If 'n' is greater than the number of elements in 'a_set', the function
returns an empty set.

Example:
    the function ex1({'a','b','c'}, 2) must return the set
    {'ab', 'ba', 'ac', 'ca', 'bc', 'cb'}
'''


def ex1(a_set, n):
    # INSERT HERE YOUR CODE
    pass
# print(ex1({'a','b','c'}, 2))


# %% ----------------------------------- EX.2 ----------------------------------- #
'''
Ex2: recursive, 6 points

Define the function ex2(root, m, n, k) that is recursive (or that
uses a recursive function) that receives as input the root
of a binary tree of integers, as defined in the `BinaryTree` class of
the module tree.py and three integers m, n, and k. The function
returns the number of nodes of the tree present at a level between m
and n, inclusive, that are multiples of k. The root is assumed to
be at level 0.

Example:
        root
    ______5______           level 0
   |             |
   8__        ___2___       level 1
      |      |       |
     _3_     9       1      level 2
    |   |
    6   12                  level 3

the call to ex2(root, 1, 2, 3) must return the value 2
'''

def ex2(root, m, n, k, level=0):
    # INSERT HERE YOUR CODE
    pass


# from tree import BinaryTree
# root = BinaryTree.fromList([5, [8, None, [3, [6, None, None], [12, None, None]]], [2, [9, None, None],[1, None, None]]])
# print(ex2(root, 1,2,3))

######################################################################################

if __name__ == '__main__':
    print('*' * 50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*' * 50)
