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


def amicable_numbers():
    a = 200
    b_sum = 0 
    total_sum = set()

    while a < 10000:
        a_sum = factors(a)
        if a_sum != 1:
            b_sum = factors(a_sum)
            if a == b_sum and a != a_sum:
                total_sum.add(a)
                total_sum.add(a_sum)
        a += 1
    total_sum = list(total_sum)
    total = reduce(lambda j,k: j+k, total_sum)

    print(total)
   
if __name__ == "__main__":
    amicable_numbers()
  