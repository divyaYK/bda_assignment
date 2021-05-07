"""mapper.py"""

from __future__ import print_function
from __future__ import division
import sys
import random

def recursive_calculation(x0, n):
    base = x0
    if n == 0:
        return base
    else:
        xn_prev = recursive_calculation(x0, n-1)
        return 1+(1/xn_prev)

if __name__ == "__main__":
  
  number_of_computation_steps = sys.argv[1]
  x0 = random.randint(1, 10)
  number_of_computation_steps = float(number_of_computation_steps)
  x0 = float(x0)

  ratio = recursive_calculation(x0, number_of_computation_steps)
  print(x0, ratio)

