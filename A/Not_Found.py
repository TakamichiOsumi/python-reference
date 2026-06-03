#!/usr/bin/env python3

import string
S = set(input())
all = set(string.ascii_lowercase)
diff = all - S

print(list(diff)[0])



