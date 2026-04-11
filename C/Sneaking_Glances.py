#!/usr/bin/env python3

N = int(input())
L = list(map(int, input().split()))

def count_zero_exceed(L, ary):
    # print(ary, end="")
    count = 0
    prev_sum = 0.5

    for i in range(N):
        if ary[i]:
            tmp = prev_sum
            if tmp < 0 and prev_sum + L[i] > 0:
                count += 1
                prev_sum = prev_sum + L[i]
            else:
                prev_sum = prev_sum + L[i]
        else:
            tmp = prev_sum
            if tmp > 0 and prev_sum - L[i] < 0:
                count += 1
                prev_sum = prev_sum - L[i]
            else:
                prev_sum = prev_sum - L[i]

    # print(" ", count)
    return count

max_count = 0
for i in range(2 ** N):
    ary = []
    for j in range(N):
        if ((i >> j) & 1):
            ary.append(True)
        else:
            ary.append(False)
    max_count = max(max_count, count_zero_exceed(L, ary))

print(max_count)
