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

        # Use deque as date structure.
        #
        # Appending elements to the end and popping from the leftmost
        # elements are required, to pick up the next character to
        # insert. While appending to the end costs O(1), popping
        # from the leftmost element costs O(n) with list type.
        cur_unused_chars = deque([])
        for key, val in sorted(counts.items(), key = lambda x:x[1]):
            cur_unused_chars.extend([key] * val)

        last_idx = 0
        while cur_unused_chars:
            result[last_idx] = cur_unused_chars.pop()
            last_idx += 2
            # Restart from the left side.
            if final_len % 2 == 0 and last_idx == final_len:
                last_idx = 1
            elif final_len % 2 == 1 and last_idx == final_len + 1:
                last_idx = 1
        print("".join(result))
