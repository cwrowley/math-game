#!/usr/bin/env python

import os
from time import time
from random import randint


ntimes = 20
subtraction = False
lo = 1
hi = 9
score = 0

os.system('clear')

score = 0
start = time()
while (score < ntimes):
    a = randint(lo,hi)
    b = randint(lo,hi)
    do_subtraction = subtraction and bool(randint(0,1))
    if do_subtraction:
        question = "%d - %d = " % (a + b, b)
        correct_answer = a
    else:
        question = "%d + %d = " % (a, b)
        correct_answer = a + b
    while True:
        try:
            ans = int(raw_input("%2d) " % (score + 1) + question))
            break
        except ValueError:
            print("Invalid input.  Please enter a number.")
    if ans == correct_answer:
        score += 1
    else:
        print("Oops.  The correct answer is %d." % correct_answer)
end = time()
print("Total time: %.2f seconds" % (end - start))
