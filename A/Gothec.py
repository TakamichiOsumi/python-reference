#!/usr/bin/env python3

# Key Takeaways:
# 1. Finish the problem with less typing solutions.
# 2. A new line can be inserted with backslash ('\') during if condition.
#    (Basic syntax)

M, D = map(int, input().split())

if (M == D and M in [3, 5, 7, 9]) or \
   (M == 1 and D == 7):
    print("Yes")
else:
    print("No")
