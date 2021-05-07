"""mapper.py"""

from __future__ import print_function
import sys

inputFile = open(sys.argv[1], 'r')

# To decrease computations
prime_numbers = [2, 3, 5, 7]

for line in inputFile:
  number = int(line)
  isPrime = True
  if number > 1:
    for i in prime_numbers:
       if (number % i) == 0:
         isPrime = False

    if isPrime:
      prime_numbers.append(number)
      print(number)

inputFile.close()
