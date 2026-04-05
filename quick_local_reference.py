#!/usr/bin/env python3

import code

# ------------------------------------
# Collect negative numbers in a list.
#
# Also, add a single value in the list.
# ------------------------------------
ary = [1, 2, 3, -1, -2]
new_ary = list(filter(lambda a:a < 0, ary))
print(new_ary)
# [-1, -2]
print([x + 10 for x in new_ary])
# [9, 8]

# ------------------------------------
# Integer Division (//)
# ------------------------------------
# print(5 // 5)  => 1
# print(3 // 2)  => 1
# print(10 // 3) => 3

# ------------------------------------
# Convert decimal number to n-adic number
# ------------------------------------
def convert_dec_to_n_adic(decimal, n):

    s = ''
    while decimal > 0:
        s = str(decimal % n) + s
        decimal = decimal // n
    return s

print(convert_dec_to_n_adic(8, 2))
# '1000'

# ------------------------------------
# Remove one leftmost char (or sub string)
# in a string.
# ------------------------------------
S = "abcdefghiabc"
S = S.replace('a', '', count = 1)
# print(S)
# "bcdefghiabc"

# ------------------------------------
# SortedList
# ------------------------------------
from sortedcontainers import SortedList
sorted_list = SortedList([1, 2, 3, 4, 5])
sorted_list.add(6)
sorted_list.add(7)
print(sorted_list)
# [1, 2, 3, 4, 5, 6, 7]

# ------------------------------------
# itertools
# ------------------------------------
import itertools
print("permutations=", list(itertools.permutations(range(1, 4))))
print("combinations=", list(itertools.combinations(range(1, 5), 3)))
print("combinations_with_replacement=",
      list(itertools.combinations_with_replacement(range(1, 4), 3)))
print("product=", list(itertools.product(range(1, 4), range(1, 4))))
# permutations= [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
# combinations= [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
# combinations_with_replacement=
# [(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 2),
#  (1, 2, 3), (1, 3, 3), (2, 2, 2), (2, 2, 3), (2, 3, 3), (3, 3, 3)]
# product= [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

# ------------------------------------
# Bit Brute Force
# ------------------------------------
def bit_brute_force(N, mat):
    comb = []
    for i in range(2 ** N):
        ary = []
        for j in range(N):
            if ((i >> j) & 1):
                ary.append(mat[j])
        comb.append(ary)
    return comb

mat = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]]

print(bit_brute_force(1, mat))
# [[], [[1, 1, 1]]]
print(bit_brute_force(2, mat))
# [[],
# [[1, 1, 1]],
# [[2, 2, 2]],
# [[1, 1, 1], [2, 2, 2]]]
# print(bit_brute_force(3, mat))
# [[],
# [[1, 1, 1]],
# [[2, 2, 2]],
# [[1, 1, 1], [2, 2, 2]],
# [[3, 3, 3]],
# [[1, 1, 1], [3, 3, 3]],
# [[2, 2, 2], [3, 3, 3]],
# [[1, 1, 1], [2, 2, 2], [3, 3, 3]]]
# print(bit_brute_force(4, mat))
# [[],
# [[1, 1, 1]],
# [[2, 2, 2]],
# [[1, 1, 1], [2, 2, 2]],
# [[3, 3, 3]],
# [[1, 1, 1], [3, 3, 3]],
# [[2, 2, 2], [3, 3, 3]],
# [[1, 1, 1], [2, 2, 2], [3, 3, 3]],
# [[4, 4, 4]],
# [[1, 1, 1], [4, 4, 4]],
# [[2, 2, 2], [4, 4, 4]],
# [[1, 1, 1], [2, 2, 2], [4, 4, 4]],
# [[3, 3, 3], [4, 4, 4]],
# [[1, 1, 1], [3, 3, 3], [4, 4, 4]],
# [[2, 2, 2], [3, 3, 3], [4, 4, 4]],
# [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]]

# ------------------------------------
# Characters
# ------------------------------------
import string
# help(string)
# ...
#     ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
#     ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     digits = '0123456789'
#     hexdigits = '0123456789abcdefABCDEF'
#     octdigits = '01234567'
#     punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
#     whitespace = ' \t\n\r\x0b\x0c'
# print(string.ascii_letters)
# print(string.ascii_uppercase)

# Convert character and integer.
print(ord('A'))
print(ord('a'))
print(chr(65))
print(chr(66))

# ------------------------------------
# Dictionary (1)
#
# Add a new key if the dictionary doesn't have
# the same. If it exists as key, apply some operation.
# ------------------------------------
dict = { "apple" : 1, "orange" : 2, "grape" : 3 , "lemon" : 4 }

target = "apple"
if target in dict.keys():
    dict[target] += 100
else:
    dict[target] = 1
print(dict)
# {'apple': 101, 'orange': 2, 'grape': 3, 'lemon': 4}

# ------------------------------------
# Dictionary (2)
#
# Make a dictionary whose values have each isolated
# different data structure. Below example shows set().
#
# Note : Using zip() to gererate dictionary is like
# below.
#
# keys = ['a', 'b', 'c' ]
# values = [ 1, 2, 3 ]
# d = { key : val for key, val in zip(keys, values) }
#
# {'a': 1, 'b': 2, 'c': 3}
# ------------------------------------
keys_list = list(string.ascii_lowercase)
char_dicts = { k : v for k, v
               in zip(keys_list, [ set() for _ in keys_list ]) }
char_dicts['a'].add(1)
char_dicts['b'].add(2)
char_dicts['c'].add(3)
char_dicts['c'].add(4)
char_dicts['c'].add(5)
print(char_dicts)

# ------------------------------------
# print() without a new line (line break)
# ------------------------------------
print("No line break", end="")
print("")

# ------------------------------------
# Initialize and launch an interactive
# shell with vars defined here.
# ------------------------------------
print("===<Variable List>===")
print("string : 'S'")
print("array : 'ary', 'new_ary'")
print("matrix : 'mat'")
print("dictionary : 'dict'")
print("SortedList : 'sorted_list'")

vars = globals().copy()
shell = code.InteractiveConsole(vars)
shell.interact(banner = "Interactive console started (type 'quit()' to exit) : ")
