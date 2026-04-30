#!/usr/bin/env python3

import itertools
from queue import Queue

# Key Takeaways:
#
# (1)  Do not use single variable name for various
#      contexts. This might lead to a confusing bug.
#      In this problem, making 'start_city', 'cur_city',
#      'visitable_city' was a good idea.
#
# (2) Check the existence of dictionary key, before
#     accessing the dictionary[key].
#
# (3) Create a new set from a single value by writing
#     new_set = set([value]).
#
# (4) Make the search speed faster by using set().
#
# (5) Scrutinize the problem input.
#     In this problem, as the 2nd example shows,
#     there can be no route input. Then,
#     abstracting unique cities from (a, b) doesn't
#     work.

def search_from_city(start_city, city_num, my_dict):
    q = Queue()
    visited = [ False ] * (city_num + 1)
    found_paths = 0

    q.put(start_city)
    visited[start_city] = True

    while not q.empty():
        cur_city = q.get()

        if cur_city in my_dict.keys():
            for visitable_city in my_dict[cur_city]:
                if not visited[visitable_city]:
                    visited[visitable_city] = True
                    q.put(visitable_city)
                    found_paths += 1

    return found_paths

N, M = map(int, input().split())

my_dict = {}
for i in range(M):
    a, b = map(int, input().split())
    if a in my_dict.keys():
        my_dict[a].add(b)
    else:
        my_dict[a] = set([b])

count = N
for n in range(N + 1):
    count += search_from_city(n, N, my_dict)

print(count)
