#!/usr/bin/env python3

from sortedcontainers import SortedList

N = int(input())
Houses = SortedList(list(map(int, input().split())))
Schools = SortedList(list(map(int, input().split())))

ans = 0
for i in range(N):
    ans += abs(Houses[i] - Schools[i])
    
print(ans)
