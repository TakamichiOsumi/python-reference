#!/usr/bin/env python3

N = int(input())

mountains = {}
for i in range(N):
    S, T = input().split()
    T = int(T)
    mountains[S] = T

sorted_mountains = sorted(mountains.items(), key=lambda x: x[1])
second_moutain = sorted_mountains[-2]

# Print the moutain name
print(second_moutain[0])

