
N = int(input())
S = list(input())

A = list(range(1, N + 1))
for last_idx, c in enumerate(S):
    if c == 'x':
        pass
    else:
        cnt = 0
        for i in range((last_idx + 1) // 2):
            tmp = A[last_idx - cnt]
            A[last_idx - cnt] = A[cnt]
            A[cnt] = tmp
            cnt += 1

print(' '.join(list(map(str, A))))
