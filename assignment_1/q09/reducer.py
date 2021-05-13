#!/usr/bin/python

from __future__ import print_function, division
import sys

success = 0
instances_count = 0

for line in sys.stdin:
  if line!="":
    success += float(line)
    instances_count += 1

print(success/instances_count)