# project euler 
# largest prime factor
# problem 3

import math 

#take 2! 
# making it faster by using the "2 way table" technique used to factor bigger numbers 

def largest_prime_v2(n):

    counter = 2
    term = 1
    while counter < n:
        if n % counter == 0:
            term += 1
            print (term, n, counter)
            n = n/counter
            counter -= 1
            print (term, n, counter)
        counter += 1

    print(n)



# first try was too verbose & took too long 
# 
# def is_prime(factors):
#     prime_factors = []
#     print (factors)
#     for x in factors:
#        for y in range(2, x):
#             if (x% y == 0):
#                 prime_factors.append(x)
#                 break
#     print (prime_factors)
#     for i in factors[:]:
#         if i in prime_factors:
#             factors.remove(i)
#     print (factors)
#     factors.sort(reverse=True)
#     print (factors[0])         
        
# def largest_prime(n):
#     all_factors = []
#     for i in range(2,n):
#         if (n % i == 0):
#             all_factors.append(i)
            
#     is_prime(all_factors)    
#     # print (all_factors)

if __name__ == "__main__":
    # largest_prime(600851475)
    largest_prime_v2 (600851475143)

