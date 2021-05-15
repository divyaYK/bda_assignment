#!/usr/bin/python

"""mapper.py"""

from __future__ import print_function
import sys
import math

prime_numbers = []
numbers_to_send = []
isPrime = True

for line in sys.stdin:
    number = int(line)
    if number == 0 or number == 1:
        continue

    for j in range(2, int(math.sqrt(number)) + 1):
        if number % j == 0 or number == 2:
            isPrime = False
    if isPrime:
        print(number)
    isPrime = True
