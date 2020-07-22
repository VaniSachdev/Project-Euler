
# project euler 
# largest palindrome product
# problem 4

#take two!
# indexing a number can get complicated,
# v2 uses the definition of a palindrome (same backwards and forwards)

def large_pal_v2():
    max_pal_2 = 0
    for i in range (100,1000):
        for j in range (100,1000):
            reverse = (str(i * j)[::-1])
            product = i * j 
            if product == int(reverse):
                if i*j > max_pal_2:
                    (max_pal_2) = i*j 
    print (max_pal_2)
    

#take one! 
#this solution works for the problem
#that is, the product of all 3 digit numbers with themsleves produce a six digit number, 
# allowing for indexing like this. (not v modular) 
 
def large_pal():  
    max_pal = 0
    for i in range (100,1000):
        for j in range (100,1000):
            product = str(i*j)
            if len(product) == 6:
                if product[0] == product[5] and product[1] == product[4] and product[2] == product[3]:
                    if int(product) > max_pal:
                        max_pal = int(product)

    print (max_pal) 
                

if __name__ == "__main__":
    large_pal()
    large_pal_v2()
