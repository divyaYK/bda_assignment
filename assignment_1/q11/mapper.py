"""mapper.py"""

from __future__ import print_function
import sys

inputFile = open(sys.argv[1], 'r')

for line in inputFile: 
  number = int(line)
  print(number, '1')

inputFile.close()