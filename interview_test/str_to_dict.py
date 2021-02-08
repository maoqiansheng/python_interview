"""
将字符串："k:1|k1:2|k2:3|k3:4"，处理成Python 字典：{k:1， k1:2， ... } # 字典
里的K 作为字符串处理
"""


def str_to_dict(s):
    l = s.split('|')
    item = dict()
    for i in l:
        k, v = i.split(':')
        item[k] = v
    return item


s = "k:1|k1:2|k2:3|k3:4"
print(str_to_dict(s))