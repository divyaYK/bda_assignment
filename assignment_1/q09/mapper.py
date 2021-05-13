from __future__ import print_function, division
import sys
import random

total_doors = 3
total_tries = int(sys.argv[1])

"""When door 1 is the answer"""
for trial in range(0, total_tries):
  picked_door = random.randint(1, 3)
  if picked_door == 1:
    print(1, "lost")
  else:
    print(1, "won")

"""When door 2 is the answer"""
for trial in range(0, total_tries):
  picked_door = random.randint(1, 3)
  if picked_door == 2:
    print(2, "lost")
  else:
    print(2, "won")

"""When door 3 is the answer"""
for trial in range(0, total_tries):
  picked_door = random.randint(1, 3)
  if picked_door == 3:
    print(3, "lost")
  else:
    print(3, "won")