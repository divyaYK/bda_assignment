from mrjob.job import MRJob

def recursive_calculation(x0, n):
    base = x0
    if n==0:
        return base
    else:
        xn_prev = recursive_calculation(n-1, x0)
        return 1+(1/xn_prev)

class GoldenRatio(MRJob):

    def mapper(self, _, line):
        if line!='\n':
            number_of_computation_steps, x0 = line.split(',')
            number_of_computation_steps = int(number_of_computation_steps)
            x0 = float(x0)
            yield x0, number_of_computation_steps

    def reducer(self, x0, computation_terms):
        ratio = recursive_calculation(x0, max(computation_terms))
        yield x0, ratio

if __name__=='__main__':
    GoldenRatio.run()
