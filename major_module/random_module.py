import random

print(random.randint(1, 10))
print(random.random())
print(random.uniform(0, 1))
print(random.randrange(1, 10, 2))
str1 = "helloworld"
list1 = [1, 3, 4, 6, 9]
tuple1 = (1, 3, 4, 5)
print(random.choice(str1))
print(random.choice(list1))
print(random.choice(tuple1))

list2 = [1, 2, 3, 4, 5, 6]
random.shuffle(list2)
print(list2)
