from __future__ import print_function, division
import random
import sys

random.seed(15)

n = int(sys.argv[1])
m = int(sys.argv[2])
number_of_experiment_tries = int(sys.argv[3])

def computeFibonacciTerms(f0, f1, n):
  if n>=sys.getrecursionlimit():
    sys.setrecursionlimit(2*n)
  fn_prev = fibonacciRecursion(f0, f1, n-1)
  fn = fibonacciRecursion(f0, f1, n)
  return fn_prev, fn

def fibonacciRecursion(f0, f1, n):
  if n==0:
    return f0

  if n == 1:
    return f1
  
  return (fibonacciRecursion(f0, f1, n-1) + fibonacciRecursion(f0, f1, n-2))


for _ in range(number_of_experiment_tries):
  f0 = random.randint(0, m)
  f1 = random.randint(0, m)

  fn_prev, fn = computeFibonacciTerms(f0, f1, n)
  
  try:
    print(fn/fn_prev)
  except ZeroDivisionError():
    continue