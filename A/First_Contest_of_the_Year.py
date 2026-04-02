#!/usr/bin/env python3

# Key Takeaways :
#
# 1. Read the example of the problem carefully.
# 2. Create an corner case by myself and evaluate the executed code.
#    In this example, suppose the case F == D - 1. 6 days are left
#    and taken over to the next year, which leads to the 6th day
#    for the 1st contest.

D, F = map(int, input().split())

print(7 - (D - F) % 7)
