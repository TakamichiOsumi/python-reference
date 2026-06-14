#!/usr/bin/env python3

from collections import deque

T = int(input())
for _ in range(T):
    N = int(input())
    weight_sum = 0
    force_sum = 0
    loss = []
    for i in range(N):
        weight, force = list(map(int, input().split()))
        weight_sum += weight
        force_sum += force
        loss.append(weight + force)

    sorted_loss = deque(sorted(loss,
                               reverse = True))
    cnt = 0
    total_loss = 0
    while True:
        minimum = sorted_loss.pop()
        
        if force_sum - minimum < 0:
            break
        else:
            cnt += 1
            force_sum -= minimum

        if len(sorted_loss) <= 0:
            break

        
    print(cnt)
