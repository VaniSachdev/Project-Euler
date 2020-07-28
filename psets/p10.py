# project euler 
# summation of primes
# problem 7

#v2
#sieve of eratosthene was actually slower than v1

# def calc_nth_prime(limit):
#     composite_list = []
#     prime_list = []
#     for i in range(2, limit+1):
#         if i not in composite_list:
#             prime_list.append(i)
#             for j in range(i*i, limit+1, i):
#                 composite_list.append(j)
#     print(sum(prime_list))

#v1 
def isPrime(n):
    if n < 2:
        return False  
    for i in range(2, int(n**0.5+1)):
        if n % i == 0:
            return False
    return True     

def summation():
    sum = 0 
    for i in range(2,2000000):
        if isPrime(i):
            sum += i 
    print (sum)


if __name__ == "__main__":
    summation()
    # calc_nth_prime(200000)
