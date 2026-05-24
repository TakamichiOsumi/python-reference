#!/usr/bin/env python3

from collections import Counter, deque

T = int(input())
for _ in range(T):
    S = input()
    counts = Counter(list(S))

    max_freq = 0
    max_freq_key = None
    final_len = 0
    for k, v in counts.items():
        final_len += v
        if max_freq < v:
            max_freq = v
            max_freq_key = k

    if max_freq > final_len - max_freq + 1:
        print("No")
    else:
        print("Yes")
        result = [None] * final_len

        last_idx = 0
        for i in range(max_freq):
            result[i * 2] = max_freq_key
            last_idx = i * 2
        last_idx += 2
        counts.pop(max_freq_key, None)

        cur_unsed_chars = deque([])
        for k, v in counts.items():
            cur_unsed_chars.extend([k] * v)

        while cur_unsed_chars:
            if final_len % 2 == 0 and last_idx == final_len:
                last_idx = 1
            elif final_len % 2 == 1 and last_idx == final_len + 1:
                last_idx = 1
            
            result[last_idx] = cur_unsed_chars.pop()
            last_idx += 2

        print("".join(result))
