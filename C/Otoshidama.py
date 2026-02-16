N, Y = map(int, input().split())
count = 0

ans1, ans2, ans3 = -1, -1, -1
found = False
for i in range(0, N + 1):
    for j in range(0, N + 1):
        k = N - (i + j)
        if k < 0 or k > N:
            continue

        if ((i * 10000 + j * 5000 + k * 1000) == Y):
            ans1, ans2, ans3 = i, j, k
            found = True
            break
    if found:
      break

print(ans1, ans2, ans3)
