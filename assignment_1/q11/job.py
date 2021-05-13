#!usr/bin/python

from __future__ import print_function, division
from mrjob.job import MRJob

class MaxMinOccurrences(MRJob):
    occurrences_dict = {}
    max_list = []
    min_list = []

    def mapper(self, _, line):
        yield int(line), 1

    def reducer(self, key, value):
        if key in self.occurrences_dict.keys():
            self.occurrences_dict[key] += value
        else:
            self.occurrences_dict[key] = value

        max_occurrences = max(self.occurrences_dict.values())
        min_occurrences = min(self.occurrences_dict.values())

        for key, value in self.occurrences_dict.items():
            if value == max_occurrences:
                self.max_list.append(key)
            if value == min_occurrences:
                self.min_list.append(key)

        for number in self.max_list:
            yield number, max_occurrences
        # for number in self.min_list:
        #     yield number, min_occurrences
