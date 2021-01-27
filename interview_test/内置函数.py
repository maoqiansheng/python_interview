print(divmod(7, 2))

list1 = ["a", "b", "c", "d"]
print(list(enumerate(list1)))
from functools import reduce


def add(x, y):  # 两数相加
    return x + y


sum1 = reduce(add, [1, 2, 3, 4, 5])  # 计算列表和：1+2+3+4+5
sum2 = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
print(sum1)
print(sum2)
