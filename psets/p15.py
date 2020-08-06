# project euler 
#lattice paths
# problem 15

#lots of research ty wiki 
# https://en.wikipedia.org/wiki/Binomial_coefficient

#assumes start pos @ (0,0)
import time
import math 
def path(gridx, gridy):
    start = time.time()
    answer = (math.factorial(gridx+gridy)) / (math.factorial(gridx) * math.factorial(gridy))
    print (int(answer))
    end = time.time()
    print (end-start)

if __name__ == "__main__": 
    path(20, 20)

  