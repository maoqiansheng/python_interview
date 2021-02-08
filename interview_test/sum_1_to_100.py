def sums():
    i = 1
    sums = 0
    while i <= 100:
        sums = sums + i
        i += 1
    return sums



print(sums())


from functools import reduce
sum_100 = reduce(lambda x, y: x+y, list(range(0, 101)))
print(sum_100)