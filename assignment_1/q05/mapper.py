"""mapper.py"""

from __future__ import print_function, division
import sys
import random

random.seed(15)

number_of_computation_steps = sys.argv[1]
x0 = random.randint(1, 10)
number_of_computation_steps = int(number_of_computation_steps)
x0 = float(x0)

ratio = x0
for i in range(1, number_of_computation_steps+1):
    ratio = 1 + (1/ratio)

print(ratio)

