
N = int(input())
S = []

def anagram_compare(si_exists, sj_exists):
    is_anagram = False
    for i in range(0, 26):
        if si_exists[i] != sj_exists[i]:
            return False
    return True

anagram_count = 0

for i in range(0, N):
    chars = list(input())
    exists = [0] * 26
    for c in chars:
        idx = ord(c) - 97
        exists[idx] = exists[idx] + 1
    S.append(exists)

    # Trigger the anagram search from the end index.
    for j in range(i - 1, -1, -1):
        if anagram_compare(S[j], exists):
            anagram_count = anagram_count + 1

print(anagram_count)
