#!/usr/bin/python

"""mapper.py"""

from __future__ import print_function
import sys

input_file = open(sys.argv[1], 'r')
for line in input_file:
    number = int(line)
    print(number, '1')
    
input_file.close()