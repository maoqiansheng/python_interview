import time


def timeit(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        return t2 - t1

    return wrapper

@timeit
def func_test():
    list1 = []
    for i in range(0, 100000):
        print(i)
        list1.insert(0, i)

print(func_test())