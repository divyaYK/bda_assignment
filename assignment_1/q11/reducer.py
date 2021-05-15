#!/usr/bin/python

"""reducer.py"""

from __future__ import print_function, division
import sys

number_n_occurrences = {}

# input comes from STDIN
for line in sys.stdin:
    if line != "":
        number, occurrence = line.split()
        number = int(number)
        occurrence = int(occurrence)

        if number in number_n_occurrences.keys():
            number_n_occurrences[number] += occurrence
        else:
            number_n_occurrences[number] = occurrence

max_occurrences = max(number_n_occurrences.values())
min_occurrences = min(number_n_occurrences.values())

for key, value in number_n_occurrences.items():
    if value == max_occurrences:
        print("Max occurred: ", key, value)

for key, value in number_n_occurrences.items():
    if value == min_occurrences:
        print("Min occurred: ", key, value)

