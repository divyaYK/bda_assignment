from __future__ import print_function, division
import sys

success_trial = 0
total_tries = 0

for line in sys.stdin:
  if line!="":
    outcome = line.split()[1]
    if outcome == 'won':
      success_trial += 1
    total_tries += 1

print(100 * success_trial/total_tries)