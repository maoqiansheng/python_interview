import copy

lst = [0, 1, 2, 3, 4, 5, 6, 7]

print(lst[1:3])  # [1, 2]

print(lst[1:-1])  # [1, 2, 3, 4, 5, 6]
print(lst[-4:])   # [4, 5, 6, 7]
print(lst[::1])  # [0, 1, 2, 3, 4, 5, 6, 7]
print(lst[::-1])  # [7, 6, 5, 4, 3, 2, 1, 0]

print([1, 2] in [1, 2, 3])
print(('hello') * 3)
print(['hello'] * 3)

print([_ for _ in range(10)])
lst = [lambda x: x*x, [x for x in range(10)]]
print(lst)
print(type(lst))
print(type(lst[1]))
print(lst[1])

name = "lzl"


def f1():
    print(name)


def f2():
    name = "eric"
    f1()
f2()

aaa = {"a": 10, "b": 34, "c": 11, "d": 22}
bbb = {value: key for key, value in aaa.items()}
print(bbb)

ccc = dict(zip(aaa.values(), aaa.keys()))
print(ccc)

ddd = tuple(zip(aaa.keys(), aaa.values()))
print(ddd)
# 深浅拷贝
a = [1, 2, "hello", ['python', 'C++']]
b = a[:]
c = [x for x in a]
print(b)
print(c)
d = list(a)
print(d)
e = copy.copy(a)
print(e)
f = copy.deepcopy(a)
print(f)
a[3].append('java')
print(e)
print(f)
# 现有字符串"1a_aa_bbb_aaa_aaaa_aaaaa_aaaaaa"，如何按照规则a->1, aa->2 aaa->3
# aaaa->4 … 如何对字符串进行处理，输出11_2_bbb_3_4_5_6 ?

string1 = "1a_aa_bbb_aaa_aaaa_aaaaa_aaaaaa"
list1 = string1.split('_')
print(list1)
list2 = []
for i in list1:
    a = i.count('a')
    if a != 0:
        str1 = i.replace(i, str(a))
        list2.append(str1)
    else:
        list2.append(i)
print(list2)
str2 = "_".join(list2)
print(str2)
"""
设计一组符合RESTful规范的HTTP API，用于实现以下功能：
a. 创建学校，查看学校列表、更新学校信息、删除学校
b. 添加学生到某个校区、查看指定校区的学生列表、查看所有学生列表、更新学生信息、删除学生
例: 创建学校 POST /api/schools/

"""

"""
a:
创建学校 POST /api/schools/
查看学校列表： GET /api/schools/
更新学校信息: PUT /api/schools/
删除学校: DELETE /api/schools/

b:
添加学生到某个校区:POST /api/schools/school_id/
查看指定校区的学生列表 GET /api/schools/school_id/students
查看所有学生列表 GET /api/schools/students
更新学生信息 PUT /api/schools/student_id
删除学生 DELETE /api/schools/student_id
 
"""

a = 1
def fun(a):
    a = 2
fun(a)
print(a)  # 1



