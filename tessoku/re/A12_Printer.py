#!/usr/bin/env python3

from sortedcontainers import SortedList
import math

debug = True # switch
def p(*var):
    global debug
    if debug:
        print("DEBUG:", *var)

def exceed_K(N, A, middle):
    value = 0
    for i in range(N):
        value += (middle // A[i])
    p("cur prints = ", value, " at ", middle, "th day.")

    if value >= K:
        return True
    else:
        return False

N, K = map(int, input().split())
A = SortedList(map(int, input().split()))
smaller_than_K = 0
equal_or_bigger_than_K = 10 ** 9

# Make sure that all of indexes >= 'equal_or_bigger_than_K' generate
# equal or bigger number of prints compared to K.
#
# When 'smaller_than_K' is bigger than 'equal_or_bigger_than_K',
# it means the edge "FIXED" (confirmed by exceed_K func) as
# equal or bigger than K ('eaual_or_bigger_than') doesn't need
# any updates more.
#
# That's the end timing of the loop.
while equal_or_bigger_than_K > smaller_than_K:

    p("range from", smaller_than_K, "to", equal_or_bigger_than_K)

    # Either [1] or [2] is fine. Both of them lead to AC.
    #
    # The 'exceed_K' function confirms the relationship between K and generated
    # print number by 'middle_boundary'. The point is 'exceed_K' decides
    # expands the range of values equal or bigger than K and let continue the loop.
    #
    # middle_boundary = (smaller_than_K + equal_or_bigger_than_K) // 2 # ... [1]
    middle_boundary = int((smaller_than_K + equal_or_bigger_than_K) / 2) # ... [2]


    if exceed_K(N, A, middle_boundary):
        # Turned out that 'middle_boundary' index generates K which is
        # equal or greater than K.
        #
        # But, This doesn't mean 'middle_boundary - 1' index is similariliy
        # equal or greater than K. Set the 'equal_or_bigger_than_K' to
        # 'middle_boundary' and rerun the loop.
        equal_or_bigger_than_K = middle_boundary
    else:
        # 'middle_boundary' generates smaller number of prints than K.
        # So, at least 'middle_boundary + 1' ~ 'equal_or_bigger_than_K' the
        # range that can generate prints more than K.
        #
        # Therefore, set the 'smaller_than_K' range to 'middle_boundary + 1'.
        smaller_than_K = middle_boundary + 1

# Print the confirmed edge 'equal_or_bigger_than_K'.
print(equal_or_bigger_than_K)
