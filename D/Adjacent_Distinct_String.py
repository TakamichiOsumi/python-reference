#!/usr/bin/env python3

# Key Takeawasys:
#
# Picking up indices to insert characters from
# '[max_freq_key] * max_freq' data is too complex to implement.
# It requires iteration per character type. This won't be
# feasible within the contest time.
#
# Prepare a final result data with '[None] * final_len' was
# much simpler to write.

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

        # Main logic
        #
        # Prepare a None array that can accommodate all characters
        # as a result output.
        #
        # Then, insert character in every other index. Restart
        # from the 1st (not the 0th !) index when putting characters
        # reach the end of array.
        result = [None] * final_len
        last_idx = 0
        for i in range(max_freq):
            result[i * 2] = max_freq_key
            last_idx = i * 2
        # Move to and point to the next insert position.
        last_idx += 2
        counts.pop(max_freq_key, None)

        # Use deque as date structure.
        #
        # Appending elements to the end and popping from the leftmost
        # elements are required, to pick up the next character to
        # insert. While appending to the end costs O(1), popping
        # from the leftmost element costs O(n) with list type.
        cur_unsed_chars = deque([])
        for k, v in counts.items():
            cur_unsed_chars.extend([k] * v)

        while cur_unsed_chars:
            # Restart from the result[1] position if insert
            # position exceeds the index of 'result' array.
            if final_len % 2 == 0 and last_idx == final_len:
                last_idx = 1
            elif final_len % 2 == 1 and last_idx == final_len + 1:
                last_idx = 1
            
            result[last_idx] = cur_unsed_chars.pop()
            last_idx += 2

        print("".join(result))
