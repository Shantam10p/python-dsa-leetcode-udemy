#1 - O(n). n being the numer of operations/iterations.
def print_items(n):
  for i in range(n):
    print(i)

print_items(10)

#2 Simplyifying Big 0 . Normally since it is looped twice we think the big o should be O(2n) but to simplying big O,  we drop the the constant and write it simply as 0(n)
def print_items(n):
  for i in range(n):
    print(i)
  
  for j in range(n):
    print(j)

print_items(10)

#3- O(n^2).Loop inside of loop (nested). These algos are significantly less effecient in terms of time complexity
def print_items(n):
  for i in range(n):
    for j in range(n):
     print(i,j, end = "")

print_items(10)

#4 - Drop Non - Dominants. Since the first nested loop is O(n^2) and the second loop is O(n) . We can write it as O(n^2 + n). Since n^2 is the dominant one and the stand alone n is insignificant compared to n^2 , therefore we drop it and write is as O(n^2)

def print_items(n):
  for i in range(n):
    for j in range(n):
      print(i,j)

  for k in range(n):
   print(k)

print_items(10)

#5 - Big O: O(1) . (note - as n increases the number of operations remain constant in O(1).Hence it is called constant time) 

def add_items(n):
  return n+n

# 6 Different terms for inputs : You cannot write the time complexity as of O(n) in case of two parameters we express it as O(a+b) and in case of nested loops as O(a*b)

#O(a+b)
def print_items(a,b):
  for i in range(a):
    print(i)
  
  for j in range(b):
    print(j)

print_items(10,11)

#O(a*b)
def print_items(a,b):
  for i in range(a):
    for j in range(b):
      print(i,j)

print_items(5,5)