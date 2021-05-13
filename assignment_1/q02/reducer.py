#!/usr/bin/python

from __future__ import print_function, division
import sys

numerator = 2
denominator = float(1)
instances_count = 0
pi = 0

for line in sys.stdin:
  denominator = float(line)
  pi += (numerator/denominator)
  instances_count += 1

print(pi/instances_count)