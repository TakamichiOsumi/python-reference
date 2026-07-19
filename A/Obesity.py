
H, W = map(int, input().split())

if (W * 100 * 100 / (H ** 2)) >= 25.0:
    print("Yes")
else:
    print("No")
