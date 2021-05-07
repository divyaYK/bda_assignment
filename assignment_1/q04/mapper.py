"""mapper.py"""

from __future__ import print_function
import sys

inputFile = open(sys.argv[1], 'r')

for line in inputFile:
  number = int(line)
  isPrime = True
  if number > 1:
    for i in range(2, number):
       if (number % i) == 0:
         isPrime = False

    if isPrime:
      print(number)

inputFile.close()
