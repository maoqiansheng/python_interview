"""
现有字典d={‘a’:24，’g’:52，’l’:12，’k’:33}请按字典中的value 值进
行排序？
"""

d = {"a": 24, "g": 52, "l": 12, "k": 33}

print(d.items())


def in_value(x):
    return x[1]


def order_in_value(d):
    # new_dict = sorted(d.items(), key=lambda x: x[1], reverse=True)
    # python中sorted函数有三个参数，(iterable, key=函数名， reverse=False)默认reverse=False
    new_dict = sorted([('a', 24), ('g', 52), ('l', 12), ('k', 33)], key=in_value, reverse=False)
    return new_dict


print(order_in_value(d))
