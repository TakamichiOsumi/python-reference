#!/usr/bin/env python3

N = int(input())
S = list(input().split())

s2 = list("abc")
s3 = list("def")
s4 = list("ghi")
s5 = list("jkl")
s6 = list("mno")
s7 = list("pqrs")
s8 = list("tuv")
s9 = list("wxyz")

result = ""
for s in S:
    if s[0] in s2:
        result = result + "2"
    elif s[0] in s3:
        result = result + "3"
    elif s[0] in s4:
        result = result + "4"
    elif s[0] in s5:
        result = result + "5"
    elif s[0] in s6:
        result = result + "6"
    elif s[0] in s7:
        result = result + "7"
    elif s[0] in s8:
        result = result + "8"
    elif s[0] in s9:
        result = result + "9"
                            
print(result)
