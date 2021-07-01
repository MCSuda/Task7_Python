import random
a = random.sample(range(0,100), random.randint(1,25)) #generating random list
print(a) #debug print
l = [num for num in a if num % 2 == 0] #this one line
print(l) #debug print
