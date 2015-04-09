#!/usr/bin/env python

import os
from time import time
from random import randint


ntimes = 10
lo = 1
hi = 9
score = 0

os.system('clear')

score = 0
start = time()
while (score < 10):
    a = randint(lo,hi)
    b = randint(lo,hi)
    try:
        ans = int(raw_input("%2d) %d + %d = " % (score + 1, a, b)))
    except ValueError:
        break
    if ans == a + b:
        score += 1
    else:
        print("Oops.  The correct answer is %d." % (a + b))
end = time()
print("Total time: %.2f seconds" % (end - start))
