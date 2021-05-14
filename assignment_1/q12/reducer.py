"""reducer.py"""

from __future__ import print_function
import sys

prime_numbers = []

# input comes from STDIN
for line in sys.stdin:
    if line!="":
      prime_number = int(line)
      prime_numbers.append(prime_number)

prime_numbers = sorted(list(set(prime_numbers)))

for number in prime_numbers:
  print(number)