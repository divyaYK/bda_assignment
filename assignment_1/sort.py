"""sort.py"""

from __future__ import print_function

import sys

sorted_dict = {}
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    if line!="":
      x0, ratio = line.split()
      x0 = float(x0)
      ratio = float(ratio)

      if x0 in dict.keys(sorted_dict):
        sorted_dict[x0].append(ratio)
      else:
        sorted_dict[x0] = []
        sorted_dict[x0].append(ratio)

      sorted_dict[x0] = sorted(sorted_dict[x0])

keys = sorted(dict.keys(sorted_dict))

for key in keys:
  print(key, *sorted_dict[key])