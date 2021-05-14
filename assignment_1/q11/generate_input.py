import random
import sys

number_of_input_entries = int(sys.argv[1])
file_name = sys.argv[2]

inputFile = open(file_name, 'w')
random.seed(15)

for i in range(number_of_input_entries):
  inputFile.write(str(random.randint(0, number_of_input_entries))+"\n")

inputFile.close()