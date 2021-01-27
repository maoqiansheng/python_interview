import time


def times(func):
    def warpper():
        start_time = time.time()
        i, j = func()
        end_time = time.time()
        print(end_time-start_time)
        return i, j
    return warpper


@times
def two_sum():
    for i in range(5001):
        for j in range(5001):
            if i + j == 10000:
                return i, j


print(two_sum())