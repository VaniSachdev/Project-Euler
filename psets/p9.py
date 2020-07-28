# project euler 
# special pythagorean triplet
# problem 9


def triplet():
    triplet_list = []
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = 1000-a-b
            if a**2 + b**2 == c**2:
                answer = a*b*c

    print (answer)
if __name__ == "__main__":
    triplet()