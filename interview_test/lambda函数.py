g = lambda x:x[1]


def func(x):
    return x[0]
print(g([1,2,3]))
print(func([1, 2, 3]))

d = {'a': 30, 'g': 17, 'b': 25, 'c': 18, 'd': 50, 'e': 36, 'f': 57, 'h': 25}
dd = dict(sorted(d.items(), key=lambda x: x[1]))
print(dd)


