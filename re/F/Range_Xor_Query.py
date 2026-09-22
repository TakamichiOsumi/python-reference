#!/usr/bin/env python3

# Key Takeaways:
#
# When building a segment tree, note that input array
# doesn't get updated, only by calling st.set().
# It updates only the internal array. Therefore,
# use st.get() for the value reference like [1].

from atcoder.segtree import SegTree

def xor_op(d1, d2):
    return d1 ^ d2

N, Q = map(int, input().split())
A = list(map(int, input().split()))

st = SegTree(xor_op, 0, A)

for _ in range(Q):
    T, X, Y = map(int, input().split())
    if T == 1:
        ref = st.get(X - 1) # ... [1]
        st.set(X - 1, ref ^ Y)
    else:
        val = st.prod(X - 1, Y)
        print(val)
