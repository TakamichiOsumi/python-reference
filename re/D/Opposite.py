#!/usr/bin/env python3

import math

N = int(input())
x0, y0 = map(int, input().split())
x_N_o, y_N_o = map(int, input().split())

center_x = (x0 + x_N_o) / 2.0
center_y = (y0 + y_N_o) / 2.0

# Convert degrees <=> radians.
theta = 2 * math.pi * (360 / N) / 360

# Rotate the x0 and y0, after making them shifted to the center.
# Make it back to the original position after the rotation.
new_x = (x0 - center_x) * math.cos(theta) - (y0 - center_y) * math.sin(theta) + center_x
new_y = (x0 - center_x) * math.sin(theta) + (y0 - center_y) * math.cos(theta) + center_y

print(new_x, new_y)
