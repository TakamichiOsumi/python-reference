#!/usr/bin/env python3

# Key Takeaways:
#
# (1) The essential point of the main logic is
#     appending temtative 'x' to the 'record', when undecided
#     choice can be made.
#     This 'x' contributes to future (idx + K) win, because
#     it avoids declaring a concrete choice and the future
#     (idx + K) choice can choose whatever it wants,
#     when the idx choice cannot win.
#
# (2) Writing up the win-lose relationship as below comments
#     helps to write the scoring logics.
#     ----------
#     'r' <= 'p'
#     'p' <= 's'
#     's' <= 'r'

N, K = map(int, input().split())
Rock_Score, Scissors_Score, Paper_Score = map(int, input().split())
Opponent = list(input())

score = 0
record = [None] * N
for idx, cur_opponent in enumerate(Opponent):
    if idx - K < 0:
        if cur_opponent == 'r':
            score += Paper_Score
            record[idx] = 'p'
        elif cur_opponent == 'p':
            score += Scissors_Score
            record[idx] = 's'
        elif cur_opponent == 's':
            score += Rock_Score
            record[idx] = 'r'
        else:
            pass
    else:
        if cur_opponent == 'r':
            if record[idx - K] == 'p':
                record[idx] = 'x'
            else:
                record[idx] = 'p'
                score += Paper_Score
        elif cur_opponent == 'p':
            if record[idx - K] == 's':
                record[idx] = 'x'
            else:
                record[idx] = 's'
                score += Scissors_Score
        elif cur_opponent == 's':
            if record[idx - K] == 'r':
                record[idx] = 'x'
            else:
                record[idx] = 'r'
                score += Rock_Score

print(score)
