#!/usr/bin/env python3

from sortedcontainers import SortedList, SortedDict, SortedSet

debug_mode = False
def p(*var):
    global debug_mode
    if debug_mode:
        print("DEBUG:", *var)

N = int(input())
A = list(map(int, input().split()))

def bit_brute_force_patterns(N):
    combinations = []
    for i in range(2 ** N):
        ary = []
        for j in range(N):
            if ((i >> j) & 1):
                ary.append(j)
        combinations.append(ary)

    return combinations

combs = bit_brute_force_patterns(N - 1)

patterns = []
for c in combs:
    p("c=", c)
    updated = [ i + 1 for i in c ]
    # Append 0 and N at the edges.
    updated = [0, *updated, N]
    p("updated=", updated)
    patterns.append(updated)
p(patterns)

calculated = []
for pattern in patterns:
    splited = []
    for start in range(0, len(pattern) - 1):
        p("pattern=", pattern ,", start=", start)
        left = pattern[start]
        right = pattern[start + 1]
        sub = A[left:right]
        splited.append(sub)
    p("splited=", splited)
    calculated.append(splited)

min_score = 2 ** 40

for ary in calculated:
    p("ary=", ary)
    applied_or = []
    while len(ary) > 0:
        tmp = ary.pop()
        if len(tmp) == 1:
            applied_or.append(tmp[0])
        else:
            num = tmp.pop()
            while len(tmp) > 0:
                num = num | tmp.pop()
            applied_or.append(num)
    p("applied_or=", applied_or)

    if len(applied_or) == 1:
        min_score = min(min_score, applied_or[0])
    else:
        no = applied_or.pop()
        while len(applied_or) > 0:
            no = no ^ applied_or.pop()
        min_score = min(min_score, no)

print(min_score)
