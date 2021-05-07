"""mapper.py"""

from __future__ import print_function
import sys

inputFile = open(sys.argv[1], 'r')


prime_numbers = []
numbers = []
numbers_to_send = []

for line in inputFile:
  numbers.append(int(line))

max_number = max(numbers)
numbers.remove(1)
numbers.remove(0)

isPrime = True
for i in range(2, max_number+1):
    for j in range(2, i):
      if i%j==0:
        isPrime = False
    if isPrime:
      prime_numbers.append(i)
    isPrime = True

for number in numbers:
  for prime_number in prime_numbers:
    if prime_number >= number:
      break
    elif number%prime_number == 0:
      isPrime = False

  if isPrime:    
    if number in numbers_to_send:
      continue
    else:
      numbers_to_send.append(number)
  else:
    isPrime = True


for number in numbers_to_send:
  print(number)

inputFile.close()
