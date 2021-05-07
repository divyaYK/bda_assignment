"""reducer.py"""

from __future__ import print_function, division
import sys

number_n_occurrences = {}
max_list = []
min_list = []

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    if line!="":
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
    max_list.append(key)
  if value == min_occurrences:
    min_list.append(key)

print("Maximum numbers and their number of occurrences")
for number in max_list:
  print(number, max_occurrences)

print("Minimum numbers and their number of occurrences")
for number in min_list:
  print(number, min_occurrences)