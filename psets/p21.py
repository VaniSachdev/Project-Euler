# project euler 
# amicable numbers
# problem 21


from functools import reduce

#adds factors of number, n 
def add_factors(all_factors):
    add = reduce(lambda j, k: j+k, all_factors)
    return add

#returns all factors of a number 
def factors(n):    
    all_factors =  set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    all_factors.remove(n)
    t = add_factors(all_factors) 
    return t 


def triangle():
    total = 0

    for n in range(2, 10000):
        x = factors(n)
    total += x 
    
    print (total)
 
  
   
if __name__ == "__main__":
    triangle()
  