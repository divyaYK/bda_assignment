from __future__ import print_function, division
import sys

totalRatio = 0
ratioCount = 0

for line in sys.stdin:
  ratio = float(line)
  totalRatio += ratio
  ratioCount+=1

print(totalRatio/ratioCount)
