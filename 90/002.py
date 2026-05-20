#!/usr/bin/env python3

import itertools

# Key Takeaways:
#
# (1) The method to detect pairs can be rephreased as
#     finding +1 and -1 in a 0/1 sequence with a
#     restriction where total score is always equal
#     or greater than zero, when checking the pattern
#     from the leftmost starting element.
#     In this problem, this is '('.
# 
# (2) Get used to zfill() to pad zeros.
#
# (3) 2 ** N is the number of 1/0 patters for N items.

N = int(input())

# Can't complete all parentheses. Exit.
if N % 2 != 0:
    exit()

answers = []
for i in range(2 ** N):
    # Remove "0b" in the string.
    binary_val = str(bin(i))[2:]
    s = str(binary_val).zfill(N)

    if s.count("0") != s.count("1"):
        continue

    score = 0
    fail = False
    for c in s:
        if c == '0':
            # found '('
            score += 1
        else:
            # found ')'
            score -= 1

        # When '(' is regarded as +1, and
        # the socre becomes minus, then
        # the status of this pattern is
        # it uses too much ')' and cannot
        # satisfy the problem requirements.
        if score < 0:
            fail = True
            break

    if fail:
        continue
        
    if score == 0:
        answers.append(s)

# print(answers)

for ans in answers:
    for c in ans:
        if c == "0":
            print("(", end="")
        else:
            print(")", end="")
    print("")
