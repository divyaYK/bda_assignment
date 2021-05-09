"""mapper.py"""

from __future__ import print_function
import sys
import math

prime_numbers = []
numbers = []
numbers_to_send = []

for line in sys.stdin:
  numbers.append(int(line))

max_number = max(numbers)
if 1 in numbers:
  numbers.remove(1)
if 0 in numbers:
  numbers.remove(0)

isPrime = True
for i in range(2, max_number+1):
    for j in range(2, int(math.sqrt(i)) + 1):
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