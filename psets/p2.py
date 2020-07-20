
# project euler 
# even fibonacci numbers
# problem 2 

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#recursion was too slow 
# def r_fib(n):
# 	if n <= 2:
# 		return n 
# 	else: 
# 		return r_fib(n-1)+ r_fib(n-2) 
	
	 
def fib():
	fib_total = 0
	x, y = 1, 2  
	
	while x <= 4e6:
		if x % 2 == 0:
			fib_total += x
		x = y
		y = x + y

	return fib_total


if __name__ == "__main__":
	print(fib())