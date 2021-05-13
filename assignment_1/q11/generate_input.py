import random
import sys

number_of_input_entries = int(sys.argv[1])

inputFile = open('input.txt', 'w')
random.seed(15)

for i in range(number_of_input_entries):
  inputFile.write(str(random.randint(0, number_of_input_entries))+"\n")

inputFile.close()