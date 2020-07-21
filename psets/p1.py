
#  project euler 
# multiples of 3 & 5
# problem 1 

def math():
  list = []
  for x in range(1000):
    if x%3 == 0 or x%5 == 0:
      list.append(x)
  print(sum(list))

if __name__ == "__main__":
  math()
