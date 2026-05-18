#!/usr/bin/env python3

N, X = map(int, input().split())
A = list(map(int, input().split()))

results = [a for a in A if a != X]

print(*results)
