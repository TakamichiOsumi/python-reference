
N = int(input())
S = []

def anagram_compare(si_exists, sj_exists):
    is_anagram = False
    for i in range(0, 26):
        if si_exists[i] != sj_exists[i]:
            return False
    return True

for i in range(0, N):
    chars = list(input())
    exists = [0] * 26
    for c in chars:
        idx = ord(c) - 97
        exists[idx] = exists[idx] + 1
    S.append(exists)

anagram_count = 0
for i in range(0, N):
    for j in range(i + 1, N):
        if i == j:
            continue
        if anagram_compare(S[i], S[j]):
            anagram_count = anagram_count + 1

print(anagram_count)
