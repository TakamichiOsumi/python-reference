#!/usr/bin/env python3

# ------------------------------------
# Array assignment
# ------------------------------------
length, *A = [5, 1, 2, 3, 4, 5]
print(length == (len(A))) # True
length, *A = [1, 1]
print(length == len(A)) # True
print(type(length)) # <class 'int'>
print(type(A)) # <class 'list'>

# ------------------------------------
# Collect negative numbers in a list.
#
# Also, add a single value in the list.
# ------------------------------------
ary = [1, 2, 3, -1, -2, 5]
new_ary = list(filter(lambda a:a < 0, ary))
print(new_ary)
# [-1, -2]
print([x + 10 for x in new_ary])
# [9, 8]

# ------------------------------------
# Pick up some elements in array per
# specific size.
# ------------------------------------
size = 3
for start in range(0, len(ary), size):
    print(ary[start : start + size])
# [1, 2, 3]
# [-1, -2, 5]

# ------------------------------------
# Sorting 'String' numbers shows
# different result with 'Integer' numbers.
# ------------------------------------
str_ary = ["1", "2", "3", "4", "5",
           "11", "12", "13"]
str_ary.sort(reverse = True)
int_ary = list(map(int, str_ary))
int_ary.sort(reverse = True)
print(str_ary)
print(int_ary)
# ['5', '4', '3', '2', '13', '12', '11', '1']
# [13, 12, 11, 5, 4, 3, 2, 1]


# ------------------------------------
# String operation
# ------------------------------------
print("python".upper())
print("PYTHON".lower())
print("Python".swapcase())

# ------------------------------------
# Iterate array from the end index.
#
# The next code shows the print
# output of -2, -1, 3, 2, 1.
# ------------------------------------
# for i in ary[::-1]:
#     print(i)

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

# ------------------------------------
# Bit Brute Force from N integer
# ------------------------------------
def bit_brute_force_patterns(N):
    combinations = []
    for i in range(2 ** N):
        ary = []
        for j in range(N):
            if ((i >> j) & 1):
                ary.append(j)
        combinations.append(ary)

    return combinations

# print(bit_brute_force_patterns(3))
# [[], [0], [1], [0, 1], [2], [0, 2], [1, 2], [0, 1, 2]]

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
# Set operations
# ------------------------------------
a = { 1, 2, 3, 4, 5 }
b = { 3, 4, 5, 6, 7 }
print(a | b) # { 1, 2, 3, 4, 5, 6, 7 }
print(a & b) # { 3, 4, 5 }
print(a - b) # { 1, 2 }
print(b - a) # { 6, 7 }

# ------------------------------------
# Dictionary (2)
#
# Make a dictionary whose values have each isolated
# different data structure. Below example shows set().
#
# Note : Using zip() to gererate dictionary requires
# two lists like below.
#
# keys = ['a', 'b', 'c' ]
# values = [ 1, 2, 3 ]
# d = { k : v for k, v in zip(keys, values) }
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
# Print dictionary values in ascending
# keys order.
#
# Besides, recognize the difference
# between list.sort() and
# new_list = sorted(list).
# ------------------------------------
keys = [5, 4, 3, 1, 2, 6]
values = ["a", "b", "c", "d", "e", "f"]
my_dict = { k : v for k, v
            in zip(keys, values) }

keys = list(my_dict.keys())
keys.sort()

# This 'keys' variable can be replaced
# with sorted(my_dict.keys()).
for k in keys:
    print(k, my_dict[k])
# 1 d
# 2 e
# 3 c
# 4 b
# 5 a
# 6 f

# ------------------------------------
# print() without a new line (line break)
# ------------------------------------
print("No line break", end="")
print("")

# ------------------------------------
# deque
# ------------------------------------
from collections import deque

d = deque([1, 2, 3])
d.append(4) # append an element at the end
d.appendleft(0) # append an element at the front
print(d)
# deque([0, 1, 2, 3, 4])
print(d.pop()) # pop from the end
# 4
print(d.popleft()) # pop from the front
# 0

# ------------------------------------
# numpy
# ------------------------------------
import numpy

npmat = numpy.array(range(24)).reshape(4, 6)
print(npmat)
# array([[ 0,  1,  2,  3,  4,  5],
#        [ 6,  7,  8,  9, 10, 11],
#        [12, 13, 14, 15, 16, 17],
#        [18, 19, 20, 21, 22, 23]])
print(npmat.ndim) # 2
print(npmat.shape[0]) # 4
print(npmat.shape[1]) # 6
print(npmat.T)
# array([[ 0,  6, 12, 18],
#        [ 1,  7, 13, 19],
#        [ 2,  8, 14, 20],
#        [ 3,  9, 15, 21],
#        [ 4, 10, 16, 22],
#        [ 5, 11, 17, 23]])

# ------------------------------------
# Regular Expression
#
# Get the matched indexes to retrieve.
# Note that the m.end(0) is the next
# index of the last character captured
# by the regular expression.
# ------------------------------------
import re
S = "This is a test. foo and bar."
for m in re.finditer(r"(foo)|(bar)", S):
    print("Index=", m.start(0), "&", m.end(0),
          ", Sub string : ", S[ m.start(0) : m.end(0) ])

# ------------------------------------
# * DO NOT ADD ANY NOTES AFTER THE SHELL START *
#
# Initialize and launch an interactive
# shell with vars defined here.
# ------------------------------------
import code

print("===<Variable List>===")
print("string : 'S'")
print("array : 'ary', 'new_ary'")
print("matrix : 'mat'")
print("dictionary : 'dict'")
print("SortedList : 'sorted_list'")
vars = globals().copy()
shell = code.InteractiveConsole(vars)
shell.interact(banner = "Interactive console started (type 'quit()' to exit) : ")
