# ------------------------------------
# template
# ------------------------------------
# print("template")

# ------------------------------------
# Collect negative numbers in a list.
# ------------------------------------
ary = [1, 2, 3, -1, -2]
new_ary = list(filter(lambda a:a < 0, ary))
print(new_ary)
# => [-1, -2]

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

# ------------------------------------
# Remove one leftmost char (or sub string)
# in a string.
# ------------------------------------
S = "abcdefghiabc"
S = S.replace('a', '', count = 1)
# print(S) => bcdefghiabc


# ------------------------------------
# SortedList
# ------------------------------------
from sortedcontainers import SortedList
sorted_list = SortedList([1, 2, 3, 4, 5])
sorted_list.add(6)
sorted_list.add(7)
print(sorted_list) # => [1, 2, 3, 4, 5, 6, 7]

# ------------------------------------
# itertools
# ------------------------------------
import itertools
print("permutations=", list(itertools.permutations(range(1, 4))))
print("combinations=", list(itertools.combinations(range(1, 5), 3)))
print("combinations_with_replacement=", list(itertools.combinations_with_replacement(range(1, 4), 3)))
print("product=", list(itertools.product(range(1, 4), range(1, 4))))
# permutations= [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
# combinations= [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
# combinations_with_replacement= [(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 2), (1, 2, 3), (1, 3, 3), (2, 2, 2), (2, 2, 3), (2, 3, 3), (3, 3, 3)]
# product= [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
