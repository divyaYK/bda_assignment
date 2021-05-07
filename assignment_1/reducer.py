"""reducer.py"""

from __future__ import print_function, division
# from operator import itemgetter
import sys

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    if line!="":
      input_list = line.split()
      x0 = float(input_list[0])
      ratios = list(map(float, input_list[1:]))
      # ratios.remove(ratios[0])
      total = 0
      numRatios = 0
      for ratio in ratios:
          total += ratio
          numRatios += 1
      print(x0, total/numRatios)
