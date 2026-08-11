#!/usr/bin/env python3

# Key Takeaways:
#
# (1) Estimate memory consumption roughly. The memory limit can
#     accept the definition of an array whose size is 5 * (10 ** 5),
#     as described in [1].
#
# (2) O(10 ** 8) should achieve the AC in terms of time complexity.
#     O(10 ** 9) might not do the same.
#     Every time a query updates the A's element, full for loop to calculate
#     XOR consumes the time. So, *diff* of A's single element must be used to
#     compute A's XOR.
#
#     Calculate XOR for A = [A1, A2, A3, A4] and save the result as tmp.
#     When query=1 comes for A4,
#     calculate tmp - (A4) + (A4 + 1), on the idea level of XOR, as
#     described in [2].
#
# (3) Furthermore, relearn the basic nature of exclusive OR.
#
#     (a) a XOR 0 = a.
#     (b) a XOR a = 0.
#     (c) a XOR b = 0 means a = b.
#     (d) a XOR b == b XOR a.
#     (e) (a XOR b) XOR c == a XOR (b XOR c)
#     (f) by (b) & (e), a XOR x XOR x == a XOR (x XOR x) == a XOR 0 = a.
#
#     The nature of (f) is essential for and can be applied to this problem.
#
# (4) For query = 2, simply decrement all non-zero values.
#     This can be calculated as not O(N).
#
#    The fundamental insight of this is, the maximum number of query=2's
#    decrement is (below) O(Q), since decrement depends on +1 of query=1.
#    (In other words, decrement needs value more than 1.)
#
#    This logic is implemented after [3].

from sortedcontainers import SortedList, SortedDict, SortedSet

debug_mode = False
def p(*var):
    global debug_mode
    if debug_mode:
        print("DEBUG:", *var)

N, Q = map(int, input().split())
A = [0] * (N + 1) # ... [1]
xor_result = 0
non_zeros = SortedSet([])

for i in range(Q):
    s = input()
    if s[0] == '1':
        # query = 1
        q, x = map(int, s.split())
        non_zeros.add(x)
        before = A[x]
        A[x] += 1
        after = A[x]
        xor_result = xor_result ^ before ^ after # ... [2]
    else:
        # for query = 2, implemente the (4) logic ... [3]
        removed = []
        new_tmp = 0
        for idx in non_zeros:
            A[idx] -= 1
            new_tmp ^= A[idx]
            if A[idx] == 0:
                removed.append(idx)
        for r in removed:
            non_zeros.remove(r)
        xor_result = new_tmp

    print(xor_result)
