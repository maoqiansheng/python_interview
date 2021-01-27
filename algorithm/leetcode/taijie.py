

def fib(n):
    a, b = 0, 1
    list1 = [0]
    for _ in range(n):
        a, b = b, a + b
        list1.append(b)
    return list1


print(fib(8))


def fibonacii(n):
    alist = [0, 1]
    for i in range(n-2):
        alist.append(alist[-2] + alist[-1])
    return alist

print(fibonacii(8))