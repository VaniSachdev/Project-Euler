import os
import p1, p2, p3, p4, p5


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
        p5.calculate()
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
    