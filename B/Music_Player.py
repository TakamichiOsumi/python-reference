#!/usr/bin/env python3

Q = int(input())

def check(playing, sound):
    if playing and sound >= 3:
        print("Yes")
    else:
        print("No")

sound = 0
playing = False
for i in range(Q):
    A = int(input())
    if A == 1:
        sound += 1
    elif A == 2:
        if sound >= 1:
            sound -= 1
    elif A == 3:
        playing = False if playing else True
    # Check the current status
    check(playing, sound)
