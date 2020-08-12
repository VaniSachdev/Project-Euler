# project euler 
# factorial digit sum
# problem 19

import math
from functools import reduce

def factorial_sum(n):
    n_exclamation  = list(map(int, str(math.factorial(n))))
    n_sum = reduce(lambda j,k: j+k, n_exclamation)
    print (n_sum)



if __name__ == "__main__":
    factorial_sum(100)