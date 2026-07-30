#!/usr/bin/env python3

W, B = map(int, input().split())

kg = W * 1000

print(kg // B + 1)
