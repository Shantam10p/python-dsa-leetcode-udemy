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

