"""

请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""
import re
str1 = 'We Are Happy'
new_str = str1.replace(' ', '%20')
print(new_str)

sub_str = re.sub(r'\s+', '%20', str1)
print(sub_str)

"""
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串”+100”,”5e2”,”-123”,”3.1416”和”-1E-16”都表示数值。 
但是”12e”,”1a3.14”,”1.2.3”,”+-5”和”12e+4.3”都不是。
"""
def is_number(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True
print(is_number('5e2'))


"""
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
"""


list1 = [1, 2, 1, 2, 3, 4]
def one_time(l):
    list2 = []
    for i in l:
        if l.count(i) == 1:
            print(i)
            list2.append(i)
    return list2
print(one_time(list1))


"""
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
1 2 3
4 5 6
7 8 9
"""
# -*- coding:utf-8 -*-
# class Solution:
#     # array 二维列表
#     def Find(self, target, array):
#         row = 0
#         col = len(array[0]) - 1
#         while row < len(array) and col >= 0:
#             if array[row][col] == target:
#                 return True
#             elif array[row][col] < target:
#                 row += 1
#             else:
#                 col -= 1
#         return False
# a = Solution()
# b = a.Find(8, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(b)


def find(target, array):
    row = 0
    col = len(array[0]) - 1
    while row < len(array) and col >= 0:
        if array[row][col] == target:
            return True
        elif array[row][col] < target:
            row += 1
        else:
            col -= 1
    return False
print(find(8, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

