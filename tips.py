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
