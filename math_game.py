#!/usr/bin/env python

from random import randint

ntimes = 10
lo = 1
hi = 9
score = 0

for i in range(ntimes):
    a = randint(lo,hi)
    b = randint(lo,hi)
    try:
        ans = int(raw_input("What is %d + %d? " % (a,b)))
    except ValueError:
        break
    if ans == a + b:
        score += 1
        print("Correct! Your score is now %d." % score)
    else:
        print("Oops.  The correct answer is %d.  Your score is now %d." % 
              (a+b, score))
if score == ntimes:
    print("Congratulations!  You have a perfect score of %d!" % score)
elif score >= ntimes-9:
    print("Great job!  Your final score is %d." % score)
else:
    print("Your final score is %d." % score)
