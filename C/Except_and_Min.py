#!/usr/bin/env python3

from sortedcontainers import SortedList

N, Q = map(int, input().split())
A = list(map(int, input().split()))

sorted_A = SortedList(A)

for i in range(Q):
    num = int(input())
    query = list(map(int, input().split()))
    removed = SortedList([])
    for j in range(len(query)):
        # Find the removed value from query.
        removed_value = A[query[j] - 1]
        removed.add(removed_value)
        sorted_A.discard(removed_value)

    print(sorted_A[0])
    
    # Restore balls to the bag.
    for j in range(len(removed)):
        restore = removed.pop(0)
        sorted_A.add(restore)
