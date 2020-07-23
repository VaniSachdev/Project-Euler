# project euler 
# sum square difference
# problem 6 

def sum_square_difference():
    x = 0 
    y = 0 
    for i in range(1, 101):
        x = x + i**2 
        y = i + y 
    print (y**2 - x)

if __name__ == "__main__":
  sum_square_difference()