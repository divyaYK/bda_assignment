"""reducer.py"""

from __future__ import print_function, division
# from operator import itemgetter
import sys

total = 0
numRatios = 0
# input comes from STDIN
for line in sys.stdin:

    if line != "":
        input_list = line.split()
        ratio = float(input_list[1])
        if ratio!=0:       
            total += ratio
            numRatios += 1

print(total/numRatios)
