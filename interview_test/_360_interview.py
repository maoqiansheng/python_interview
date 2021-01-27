# 1、拿出两个表中相同的数据
'''select * from table1 inner join table2 on table1.name=table2.name'''

# 2、a = “abbbccc”，用正则匹配为abccc,不管有多少b，就出现一次？
import re

string1 = "1a_aa_bbb_aaa_aaaa_aaaaa_aaaaaa"
list1 = string1.split('_')
print(list1)  # ['1a', 'aa', 'bbb', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa']
list2 = []
for i in list1:
    a = i.count('a')
    if a != 0:
        str1 = re.sub(r'a+', str(a), i)
        list2.append(str1)
    else:
        list2.append(i)
print(list2)  # ['11', '2', 'bbb', '3', '4', '5', '6']
str2 = "_".join(list2)
print(str2)  # 11_2_bbb_3_4_5_6

# 3、redis中内容的长度， len key_name

# 4、多线程交互，访问数据怎样避免重读
# 创建一个已经访问数据的列表，用于储存已经访问过的数据，并且加上互斥锁， 在多线程访问的时候，先去列表中查询，如果已经访问过，就直接跳过

# mysql怎样限制ip访问

# grant all privileges on 数据库名 to '用户名'@'ip' identified by '密码'

# 创建用户并授权
# grant 权限列表 on 数据库名 to '用户名'@'ip' identified by '密码'
# grant 权限列表 on 数据库 to '用户名'@'访问主机' identified by '密码';

