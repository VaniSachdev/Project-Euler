# project euler 
#power digit sums 
# problem 16


from functools import reduce 


def sum_of_digits():
    number = 2 ** 1000
    number = list(map(int, str(number)))
    number_sum = reduce(lambda j,k: j+k, number) 
    print (number_sum)   

if __name__ == "__main__": 
    sum_of_digits()

  