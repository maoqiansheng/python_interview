"""

1、python的数据类型
string, list, dict, int， float, bool， set, tuple
2、python的dir('a')
输出字符串型的内置属性和方法
3、3. 给定两个list，A 和B，找出相同元素和不同元素？

相同元素：set(A) &s et(B)
不同元素： set(A) ^ set(B)

4、字符串反转

"""
list1 = [1, 3, 5, 7]
list2 = [3, 5, 7, 9]
print(set(list1) & set(list2))
print(set(list1) ^ set(list2))
print(dir('a'))
str1 = 'abcdefg'
print(str1[::-1])

# 用select语句输出每个城市中心距离市中心大于20km 酒店数？(
# select city, count(*) from hotel_table group by city having distance > 20;

# 给定一个有序列表，请输出要插入值k 所在的索引位置？


def insert_index(list3, key):
    if key < list3[0]:
        position = 0
    elif key > list3[-1]:
        position = len(list3)
    else:
        for index in range(list3):
            if key > list3[index] and list3[index] > key:
                position = index
    return position

print(insert_index([1, 2, 4, 5], 3))

# a = ('a', 'b', 'c', 'd')  # 元组不可变类型，不支持修改删除
# del a[2]

