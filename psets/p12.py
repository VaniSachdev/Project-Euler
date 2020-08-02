# project euler 
#highly divisible triangular number
# problem 12

from functools import reduce

#returns all factors of a number 
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def triangle():
    total = 1
    n = 1
    # print (factors(n))
    while len(factors(total)) < 500:
        total = n *(n+1) /2 #summation of natural numbers
        n += 1 
    
    print (int(total))

if __name__ == "__main__":
    triangle()
  