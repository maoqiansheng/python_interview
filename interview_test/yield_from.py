# 下面a()和b()是等价的
def a():
    yield from [1, 2, 3, 4, 5]


def b():
    for i in [1, 2, 3, 4, 5]:
        yield i


for i in a():
    print(i)
for i in b():
    print(i)
