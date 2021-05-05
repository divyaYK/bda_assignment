# Prepare input
import random
import sys

print(sys.getrecursionlimit())
inputFile = open('./input.txt', 'w')

number_of_mapped_instances = int(input("Enter the number of mapped instances:\n"))

# Make sure you have the same seed number to get same input.txt file as the one in repo
random.seed(5)

for i in range(number_of_mapped_instances):
    number_of_computation_steps = random.randint(int(number_of_mapped_instances/2), number_of_mapped_instances)
    x0 = random.randint(1, 9)
    if i <= number_of_mapped_instances-1:
        inputFile.write(f"{number_of_computation_steps}, {x0}\n")
    else:
        inputFile.write(f"{number_of_computation_steps}, {x0}")
inputFile.close()