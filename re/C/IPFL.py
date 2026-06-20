#!/usr/bin/env python3

N = int(input())
S = list(input())
Q = int(input())

is_flipped = False
for i in range(Q):
    T, A, B = map(int, input().split())
    A, B = A - 1, B - 1
    if T == 2:
        if is_flipped:
            is_flipped = False
        else:
            is_flipped = True
    elif T == 1:
        if is_flipped == False:
            # Interpret both A and B directly.
            tmp = S[B]
            S[B] = S[A]
            S[A] = tmp
        else:
            # Calculate the flipped position.
            flipped_A = (A + N) % (2 * N)
            flipped_B = (B + N) % (2 * N)
            tmp = S[flipped_B]
            S[flipped_B] = S[flipped_A]
            S[flipped_A] = tmp

# Prepare for the final output.
if is_flipped:
    S1 = S[0:N]
    S2 = S[N:2 * N]
    S2.extend(S1)
    S2 = ''.join(S2)
    print(S2)
else:
    print(''.join(S))
