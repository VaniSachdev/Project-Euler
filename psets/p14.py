# project euler 
#longest collatz sequence
# problem 14

# a little slow; to be optimized in the future when i learn more about dynamic programming lol 

def collatz():
    counter = 0 
    longest = 1 
    for i in range(3, int(1e6)):
        x = i 
        while i > 1:
            if i%2 == 0:
                i = i/2 
                counter += 1
               
            else:
                i = 3*i + 1 
                counter += 1
             
        if counter > longest:
            highest_i = x
            longest = counter 
        
        counter = 0 
    print (highest_i)

if __name__ == "__main__": 
    collatz()
    # practice (13)