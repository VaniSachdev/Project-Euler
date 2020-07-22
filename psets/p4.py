
# project euler 
# largest palindrome product
# problem 4

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
