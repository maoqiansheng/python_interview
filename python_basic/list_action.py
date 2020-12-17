# 二、列表（list）
# 列表是python中重要的数据类型，一般存放相同类型的元素
# 1、查
list1 = [1, 2, 3, 4]
print(list1[0])
# 1

# 2、增
# 末尾增加append
nums = [1, 2, 3, 4, 5]
print(nums)
# [1, 2, 3, 4, 5]
# 增加列表extend([])
list1.extend([6, 7, 8])
print(list1)
# [1, 2, 3, 4, 5, 6, 7, 8]
# insert(8, 9)
list1.insert(8, 9)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3、删
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# del list1[index]
del list1[0]
print(list1)
# [2, 3, 4, 5, 6, 7, 8, 9]
# 列表.remove(数据)
list1.remove(9)
print(list1)
# [2, 3, 4, 5, 6, 7, 8]
# 列表.pop(),删除列表中的最后一个元素  有返回值，删除的元素
list1.pop()
print(list1.pop())
# 8
# 列表.pop(索引) 删除指定索引数据
list1.pop(0)
print(list1)
# [3, 4, 5, 6, 7]
# 列表.clear(), 清空列表
list1.clear()
print(list1)
# []

# 4、改

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list1[0] = 0
print(list1)
# [0, 2, 3, 4, 5, 6, 7, 8, 9]

# 5、列表的长度，len(列表）
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(list1))
# 9

# 6、列表排序:
# 升序：列表.sort()
# 降序：列表.sort(reverse=True)
list1 = [2, 1, 4, 3]
list1.sort()
print(list1)
# [1, 2, 3, 4]

# 7、判断元素是否在列表中：if  元素  in 列表：
list1 = [1, 2, 3, 4]
if 1 in list1:
    print(True)
# True
