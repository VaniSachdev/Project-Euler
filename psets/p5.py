# project euler 
# smallest multiple
# problem 5

def is_divisble(n):
    for i in range(2, 21):
        if n % i != 0:
            return False
    
    return True 

def calculate():
    number = 20;
    while True:
        if is_divisble(number):
            break
        else:
            number += 20
    print (number)

if __name__ == "__main__":
    calculate()
