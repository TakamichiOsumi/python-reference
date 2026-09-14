#!/usr/bin/env python3

# Key Takeaways:
#
# (1) For any problem that requires to print one example of answer,
#     just simplify the easiest answer case and print it, like below.

N = int(input())
A = list(map(int, input().split()))

unused = []

for i in range(1, N + 1):
    cnt = A.count(i)
    if cnt == 0:
        unused.append(i)
    else:
        if cnt >= 2:
            print("No")
            exit()

print("Yes")
res = []
for i in range(N):
    if A[i] == -1:
        res.append(unused.pop(0))
    else:
        res.append(A[i])

print(*res)
