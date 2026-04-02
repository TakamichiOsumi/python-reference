#!/usr/bin/env python3

# Key Takeaways :
#
# 1. Insert debug print()s at an appropriate level of granularity.
# 2. For the 1st execution of an isolated function, gain a lot of information
#    by inserting some testing codes to check new cases other than the problem input.
#    This reduces much time to implement the function because of early debugging.

N, M = map(int, input().split())
S = input() # len(S) == N
T = input() # len(T) == M

def make_same_string(sub_S, T):
    # print("compare ", sub_S, "and", T)
    inc_count = 0

    for i in range(len(sub_S)):
        copied_T = T
        for j in range(10):
            s1 = sub_S[i]
            s2 = str((int(copied_T[i]) + j) % 10)
            # print(s1, " vs. ", s2)
            if s1 == s2:
                break
            else:
                inc_count += 1

    return inc_count

min_count = 10 ** 15
for i in range(N - M + 1):
    sub_S = S[i : i + len(T)]
    min_count = min(min_count,
                    make_same_string(sub_S, T))

print(min_count)

# print("a=", make_same_string("02", "91"))
# print("b=", make_same_string("10", "10"))
# print("c=", make_same_string("10", "40"))
# print("d=", make_same_string("10", "55"))
