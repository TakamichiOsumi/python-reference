#!/usr/bin/env python3

# Key Takeaways:
#
# (1) BFS(breadth-first search) can be started from the *goal*,
#     in this problem.
#
#     It's because each room is connected bidirectionally,
#     when A and B are indicated as input.
#
#     Therefore, defining the 1st room as the starting room
#     and clarifying all of the distances from the room
#     solves the problem.
#
# (2) As described in [1], never forget
#     to skip all of the already-visited rooms.
#
# (3) As described in [2],
#     the distance can be calculated based on 'cur_room'
#     distance.
#
# (4) The routes from the *goal* can be traced
#     by preparing a buffer to save previous room
#     for each and updating it on finding non-visited room.
#     In the below code, 'prev_rooms' var works for this.

from collections import deque

N, M = map(int, input().split())

routes = [ set() for _ in range(N) ]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    routes[A].add(B)
    routes[B].add(A)

# For future reusability, leave the debug print()s as they were written.
def BFS(room_no, start_room, routes):

    visited = [-1] * room_no
    visited[start_room] = 0
    prev_rooms = [-1] * room_no
    prev_rooms[start_room] = 0
    d = deque([start_room])

    dist = 1
    while len(d) > 0:
        cur_room = d.popleft()

        # print("cur_room=", cur_room)
        conns_set = routes[cur_room]
        # print("conns=", conns_set)
        for c in conns_set:
            if visited[c] == -1: # ... [1]
                d.append(c)
                visited[c] = visited[cur_room] + 1 # ... [2]
                prev_rooms[c] = cur_room # ... [3].

    # print("visited=", visited)
    # print("prev_rooms=", prev_rooms)

    return visited, prev_rooms

visited, prev_rooms = BFS(N, 0, routes)

for i in range(N):
    if visited[i] == -1:
        print("No")
        exit()

print("Yes")
for idx, pr in enumerate(prev_rooms):
    if idx == 0:
        continue
    # +1 for accuarete room number.
    print(pr + 1)
