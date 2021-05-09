from __future__ import print_function, division
import sys
import math

numerator = 2
denominator = 1

for line in sys.stdin:
  denominator *= round(float(line), 5)
  denominator = round(denominator, 5)

pi = numerator/denominator

print(pi)