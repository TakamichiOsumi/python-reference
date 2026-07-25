import re

M, D = map(int, input().split())
S = input()

s = set()
for m in re.finditer(r"G", S):
    if D != 0:
        left = max(m.start(0) - D, 0)
        right = min(m.start(0) + 1 + D, len(S))
    else:
        left = m.start(0)
        right = m.start(0) + 1

    see = set(range(left, right))
    s = s | see

print(len(set(range(M)) - s))

