#!/usr/bin/env python3

N = int(input())
answers = []
counter = 1

while counter ** 2 <= N:

    if N % counter == 0:
        answers.append(counter)

        # Append the divisor counterpart without duplicate,
        # like another 5 for divident 25 or 10 for divident 100.
        if counter != (N // counter):
            answers.append(N // counter)

    counter = counter + 1

answers.sort(reverse = False)

for i in range(len(answers)):
    print(answers[i])
