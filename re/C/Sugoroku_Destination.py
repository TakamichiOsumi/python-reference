# TODO:
# Make the speed faster by scanning A ary in order from the back
# and caching the results to skip duplicate calculations.
#
# The current status shows ACs except for one test.

N = int(input())

MAX = 10 ** 100
A = list(map(int, input().split()))

results = []
count = 1
for i in range(1, N + 1):
    j = i

    prev_idx = j - 1

    while(True):

        next_idx = A[j - 1]
        if next_idx == prev_idx + 1:
            break
        else:
            prev_idx = j - 1
            j = next_idx
            count = count + 1
            if count >= MAX:
                break

    results.append(A[next_idx - 1])

print(*results)
