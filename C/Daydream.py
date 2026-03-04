#!/usr/bin/env python3

S = input()

# -----------------------------------------------
# Both 'd' or 'e' can follow all of below cases.
# 01234   567890 (index of 'S' for reference)
# -----------------------------------------------
# dream + eraser
# dream + erase
# dream   er
# dream
# erase
# erase   r

def compare(S, p, target):

    for i in range(len(target)):
        # If S is 'er' and target is 'erase',
        # then, the first two characters are same.
        #
        # In this type of case, eraser() or erase()
        # should be regarded as False, while er()
        # should return True.
        #
        # To achieve this logic, when the p reaches
        # the end of the string, return False
        # and leave the check to the successsor
        # functions like erase() and er(),
        # which leads to the expected string match.
        if p + i >= len(S):
            return False

        if S[p + i] != target[i]:
            return False

    return True

def dreamer(S, p):
    return compare(S, p, "dreamer")

def dream(S, p):
    return compare(S, p, "dream")

def eraser(S, p):
    return compare(S, p, "eraser")

def erase(S, p):
    return compare(S, p, "erase")

def er(S, p):
    return compare(S, p, "er")

p = 0
conclusion = True

while len(S) > p:

    c = S[p]

    if c == 'd':
        if dream(S, p):
            p += len("dream");
        else:
            conclusion = False
            break

        # This is the second additional check.
        #
        # Since S can end here or just have 'er'
        # at the end, it's necessary to refer to
        # the left length of S, like the top
        # while loop condition.
        if len(S) - p > 0 and S[p] == 'e':
            if eraser(S, p):
                p += len("eraser")
                continue

            if erase(S, p):
                p += len("erase")
                continue

            if er(S, p):
                p += len("er")
                continue

            conclusion = False
            break

        # Just found "dream". Next can be another dream or dreamer.
        # Go back to the start.
        continue

    elif c == 'e':

        if eraser(S, p):
            p += len("eraser")
            continue

        if erase(S, p):
            p += len("erase")
            continue

        conclusion = False
        break

    else:
        conclusion = False
        break

if conclusion:
    print("YES")
else:
    print("NO")
