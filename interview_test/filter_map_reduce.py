from functools import reduce
def is_odd(n):
    return n % 2 == 1

b = filter(is_odd, [1, 2, 3, 4, 5, 6])
print(list(b))

c = map(lambda x:x*2,[1,2,3])
print(list(c))

d = reduce(lambda x,y:x*y,range(1,4))
print(list(range(1,4)))
print(d)
