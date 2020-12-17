# 三、字典
# 1、增
# 字典[键] =数据，键不存在，会添加键值对；键存在，会修改键值对的值
dict1 = {"name": "彭于晏", "age": 18}
print(dict1)
dict1.setdefault("gender", "")
print(dict1)
# {"name": "彭于晏", "age": 18}
# {'name': '彭于晏', 'age': 18, 'gender': ''}

# 2、删
# 字典.pop(键), 删除指定键值对,返回被删除的值
dict1 = {'name': '彭于晏', 'age': 18}
print(dict1.pop("age"))
print(dict1)
# 18
# {'name': '彭于晏'}
# 字典.clear,清空字典
dict1 = {'name': '彭于晏', 'age': 18}
dict1.clear()
print(dict1)
# {}

# 3、改
# 字典[键]=数据
dict1 = {"name": "彭于晏"}
print(dict1)
# {"name": "彭于晏"}

# 4、查
dict1 = {'name': '彭于晏', 'age': 18, "gender": "男"}
print(dict1["name"])
# 彭于晏
print(dict1.keys())
# dict_keys(['name', 'age', 'gender'])
print(dict1.values())
# dict_values(['彭于晏', 18, '男'])
# dict_items([('name', '彭于晏'), ('age', 18), ('gender', '男')])
