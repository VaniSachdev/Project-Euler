# project euler 
# number letter counts
# problem 17

#imported num2words 
from num2words import num2words

def numbers_in_words():
    total = 0 
    char = ['-', ' ']

    for i in range(1, 1001):   
        original = num2words(i)
        for leave in char:
            original = original.replace(leave, "")
        total = total + len(original)

    print (total)

if __name__ == "__main__": 
    numbers_in_words()