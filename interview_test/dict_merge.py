d1 = {'name': 'revotu', 'age': 99}
d2 = {'age': 24, 'sex': 'male'}
d1.update(d2)
print(d1)
# 合并两个列表成一个字典
keys = ['A', 'B', 'C']
values = [1, 2, 3]
print(dict(zip(keys, values)))
# 字典推倒式
new_dict = {k:v for k, v in zip(keys, values)}
print(new_dict)

map_dict = dict(map(lambda k,v : (k,v), keys, values))
print(map_dict)