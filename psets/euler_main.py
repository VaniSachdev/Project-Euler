import os
import p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14


def load_answer(n):
    if n == 1:
        p1.math()
    elif n == 2:
        p2.fib()
    elif n == 3:
        p3.largest_prime_v2 (600851475143)
    elif n == 4:
        p4.large_pal_v2()
    elif n == 5:
        print ("this one takes a while -- sorry!")
        p5.calculate()
    elif n == 6:
        p6.sum_square_difference()
    elif n == 7:
        print ("this one takes a while -- sorry!")
        p7.calculate_upper_limit_for_nth_prime(10001)
    elif n == 8:
        p8.product_in_series()
    elif n == 9:
        p9.triplet()
    elif n == 10:
        print ("this one takes a while -- sorry!")
        p10.summation()
    elif n == 11:
        p11.largest_product()
    elif n == 12:
        p12.triangle()
    elif n == 13:
        p13.large_sum()
    elif n == 14:
        print ("this one takes a while (~15 sec) -- sorry!")
        p14.collatz()
    else:
        print("sorry, looks like something is wrong. please try again!")

def total_files():
    list = os.listdir("/Users/vanisachdev/Desktop/github/Project-Euler/psets") 
    number_files = len(list) -1
    return number_files

def user_input():
    user_input = input("what problem do you want the answer for? ")
    try:
        val = int(user_input)
        if val > 0 and val <= total_files():
              print("problem #"+ str(val) + " loading!")
              load_answer(val)
        elif val == 0:
            print("there is no question zero oops!")
        else:
            print("sorry, not at that question yet!")

            
    except ValueError:
        try:
            val = float(user_input)
            print("enter a integer pls, not a float!")
        except ValueError:
            print("invalid input!")
    
if __name__ == "__main__":
    user_input()
    