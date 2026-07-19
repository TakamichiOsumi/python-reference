
N = int(input())

all_taken = 10000
cur_taken = 10000
for _ in range(N):
    A, B, S = input().split()
    A = int(A)
    B = int(B)
    charge = A - B
    if S == "keep":
        cur_taken = cur_taken - B
    else:
        cur_taken = cur_taken - B + charge
    all_taken = all_taken - B + charge

print(cur_taken - all_taken)
