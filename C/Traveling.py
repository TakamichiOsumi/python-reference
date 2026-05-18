#!/usr/bin/env python3

N = int(input())

cur_x, cur_y = 0, 0
prev_time = 0
for i in range(N):
    time, dest_x, dest_y = map(int, input().split())
    left_time = time - prev_time
    move_counts = abs(dest_x - cur_x) + abs(dest_y - cur_y)
    possible = ((move_counts <= left_time) and ((left_time - move_counts) % 2 == 0))

    if possible is False:
        print("No")
        # Consume the left inputs and exit.
        for j in range(N - 1 - i):
            input()
        exit()

    cur_x = dest_x;
    cur_y = dest_y;
    prev_time = time
        
print("Yes")
