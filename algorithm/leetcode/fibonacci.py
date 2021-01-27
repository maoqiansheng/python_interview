# 斐波那契数列是一个非常经典的数列
# 斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13,
# 特别指出：第0项是0，第1项是第一个1。从第三项开始，每一项都等于前两项之和。

# python中斐波那契数列的写法

# 1、最简单的写法，也能看出其中的逻辑,代码易读


class Fibonacci(object):
    def __init__(self):
        self.n1 = 0
        self.n2 = 1
        self.count = 2

    def fib(self, n):
        fib_list = []
        if not isinstance(n, int):
            return "n必须是整数"
        elif n <= 0:
            return "n必须是正整数"
        elif n == 1:
            fib_list.append(self.n1)
            fib_list.append(n)
            return fib_list
        else:
            fib_list.append(self.n1)
            fib_list.append(self.n2)
            while self.count < n:
                nth = self.n1 + self.n2
                fib_list.append(nth)
                self.n1 = self.n2
                self.n2 = nth
                self.count += 1
        return fib_list


fibs = Fibonacci()
print(fibs.fib(8))

# 2斐波那契数列,输出了第10个斐波那契数列


def fib(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a


print(fib(10))


# 3、列表实现
def fibonacci(num):
    fibos = [0, 1]
    for i in range(num - 2):
        fibos.append(fibs[-2] + fibs[-1])  # 倒数第二个+倒数第一个数的结果，追加到列表
    print(fibs)

# 4、迭代器实现斐波那契数列


class FibItetator(object):
    def __init__(self, n):
        """指明生成数列的前n个数"""
        self.n = n
        self.current_num = 0
        self.num1 = 0
        self.num2 = 1

    def __next__(self):
        """被next()函数调用来获取下一个数"""
        if self.current_num < self.n:
            num = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            self.current_num += 1
            return num
        else:
            raise StopIteration

    def __iter__(self):
        """迭代器的__iter__返回自身即可"""
        return self


fibite = FibItetator(8)
fibs_list = []
for i in fibite:
    fibs_list.append(i)
print(fibs_list)

# 5、生成器实现斐波那契数列


def fib(n):
    current, num1, num2 = 0, 0, 1
    while current < n:
        num = num1
        num1, num2 = num2, num1 + num2
        current += 1
        yield num
    return 'done'


#

def fib(num):
    fib_list = [0, 1]
    for i in range(num-2):
        fib_list.append(fib_list[-2] + fib_list[-1])
    return fib_list


print(fib(10))















