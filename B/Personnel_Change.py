#!/usr/bin/env python3

# Key Takeaways:
#
# 1. Create a utility function to list dictionary values
#    according to the order of integer keys.
#
# 2. Check the output format carefully.

N, M = map(int, input().split())

keys_list = list(range(M))
per_dicts = { k : v for k, v
               in zip(keys_list, [0] * M ) }

for i in range(N):
    A, B = map(int, input().split())
    per_dicts[A - 1] -= 1
    per_dicts[B - 1] += 1

keys = list(per_dicts.keys())
keys.sort()

for k in keys:
    print(per_dicts[k])
