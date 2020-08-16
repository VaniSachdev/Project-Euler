# project euler 
# 1000-digit fibonacci number
# problem 25

def fib():
    x, y = 1, 1
    count = 2 

    while True:
        z = str(y + x)
        x = y 
        y = int(z)
        count += 1 

        if len(z) > 999:
            print (count)
            return False 
        

if __name__ == "__main__":
    fib()