from mrjob.job import MRJob
# import sys

def recursive_calculation(x0, n):
    base = x0
    if n==0:
        return base
    else:
        xn_prev = recursive_calculation(x0, n-1)
        return 1+(1/xn_prev)

class GoldenRatio(MRJob):

    def mapper(self, _, line):
        if line!='\n':
            number_of_computation_steps, x0 = line.split(',')
            number_of_computation_steps = int(number_of_computation_steps)
            x0 = float(x0)
            # sys.setrecursionlimit(number_of_computation_steps)
            ratio = recursive_calculation(x0, number_of_computation_steps)
            yield x0, ratio

    def reducer(self, x0, ratios):
        total = 0
        numRatios = 0
        for ratio in ratios:
            total += ratio
            numRatios += 1
        yield x0, total/numRatios

if __name__=='__main__':
    GoldenRatio.run()
