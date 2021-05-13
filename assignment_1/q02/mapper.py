#!/usr/bin/python

from __future__ import print_function, division
import sys
import math

def compute_term(n):
  term = 0
  if n==1:
    term = math.sqrt(2)
  else:
    prev_term = compute_term(n-1)
    term = math.sqrt((2 + prev_term))
  
  return term

multiplication_terms = int(sys.argv[1])
recursion_limit = sys.getrecursionlimit()

for ith_term in range(1, multiplication_terms):
  if ith_term >= recursion_limit:
    sys.setrecursionlimit(2 * ith_term)
  print(compute_term(ith_term)/2)

