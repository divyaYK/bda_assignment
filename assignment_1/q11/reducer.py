#!/usr/bin/python

"""reducer.py"""

from __future__ import print_function, division
import sys


def MaxMinRepeating(arr, n):
    max_number = max(arr)
    arr.append(max_number + 1) # "dummy" one added to save the max number in case it occurs only once
    arr = sorted(arr)
    print(arr)
    result_max = []
    result_min = []
    count = 1
    maxCount = 1
    currentElement = arr[0]
    maxOccurredElement = arr[0]

    for i in range(1, n+1):
        if currentElement == arr[i]:
            count += 1
        else:
            if count>maxCount:
                maxCount = count
                maxOccurredElement = currentElement
                if len(result_max) != 0 :
                    result_max = []
                result_max.append(maxOccurredElement)
            elif count == maxCount :
                maxOccurredElement = currentElement
                result_max.append(maxOccurredElement)
            if count == 1:
                result_min.append(currentElement)
            currentElement = arr[i]
            count = 1

    return result_max, maxCount, result_min

number_n_occurrences = {}
numbers = []
# input comes from STDIN
for line in sys.stdin:
    if line != "":
        number, occurrence = line.split()
        number = int(number)

        numbers.append(number)

max_occurred_numbers, max_occurrences, min_occurred_numbers = MaxMinRepeating(numbers, len(numbers))
print("Max occurred numbers: ", max_occurred_numbers, " with ", max_occurrences, " occurrences")

min_occurrences = 1     # Among a million+ numbers minimum occurrence is 1 by default
print("Min occurred numbers: ", sorted(min_occurred_numbers, key=str), " with ", min_occurrences, " occurrences")
