#!/usr/bin/env python3

# Key Takeaways:
#
# (1) Save the pair of [c, x] as it is. Never create and append [x] * c,
#     when the problem description defines the maximum size of c is quite big.

from collections import deque, Counter

debug = False
def p(*var):
    global debug
    if debug:
        print("DEBUG:", *var)

Q = int(input())

buf = deque([])

for i in range(Q):
    s = input()

    if s[0] == '1':
        # query = 1
        q, c, x = map(int, s.split())
        buf.append([c, x])
        p(buf)
    else:
        # for query = 2
        q, k = map(int, s.split())
        p("k=", k)
        consumed_c = 0
        val = 0
        while True:
            first = buf[0]
            c, x = first
            if c + consumed_c >= k:
                require = k - consumed_c
                val += require * x
                print(val)
                if c + consumed_c == k:
                    buf.popleft()
                else:
                    buf[0][0] -= require
                break
            else:
                consumed_c += c
                val += (c * x)
                buf.popleft()
        p("end of q=2, ", buf)
