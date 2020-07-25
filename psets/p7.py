# project euler 
# 10001st prime
# problem 7

#uses approximations for the nth prime number + sieve of eratosthenes (including optimization of starting from a prime's square)

import math 

def calculate_upper_limit_for_nth_prime(nth_prime):
    limit = int(nth_prime * (math.log(nth_prime) + math.log(math.log(nth_prime-1))))+1
    calc_nth_prime (limit, nth_prime)
   
def calc_nth_prime(limit, nth_prime):
    composite_list = []
    prime_list = []
    for i in range(2, limit+1):
        if i not in composite_list:
            prime_list.append(i)
            for j in range(i*i, limit+1, i):
                composite_list.append(j)
    print(prime_list[nth_prime-1])

if __name__ == "__main__":  
    calculate_upper_limit_for_nth_prime(10001)