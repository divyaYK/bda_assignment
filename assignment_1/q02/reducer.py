#!/usr/bin/python

from __future__ import print_function, division
import sys

numerator = 2
denominator = 1
instances_count = 0

for line in sys.stdin:
  denominator *= round(float(line), 5)
  denominator = round(denominator, 5)
  instances_count += 1

pi = numerator/denominator

print(pi/instances_count)