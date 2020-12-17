# python常用的数据类型
# python 基础学习参考：https://www.runoob.com/python
# 数字型和非数字型，
# 数字型包括：整型（int）, 浮点型（float）,布尔型(bool)
# 非数字型：    字符串(str)，列表(list)，元组(tuple)，字典(dict)
# 其中最常用的是字符串，列表，字典
# 一、字符串(str)
# 1、 字符串使用 + 拼接
print("我的名字" + "彭于晏")
# 我的名字彭于晏

# 2、字符串格式化输出
print("商品的价格 %06d" % 20)
# 商品的价格 000020
print("商品的价格 %.3f" % 20)
# 商品的价格 20.000
print("我的名字叫%s" % '彭于晏')
# 我的名字叫彭于晏

# 3、字符串查询
str1 = "hello"
print(str1[0])
# h

# 4、判断是否是纯数字或者纯字母
# 判断纯数字：String.isdecimal()
# 判断纯字母：String.isalpha()
# 5、字符串查找string.find
str1 = "hello"
print(str1.find('8'))
# -1 # 找不到返回-1
print(str1.find('h'))
# 0 # 找得到返回下标

# 6、字符串中字符的替换
str1 = 'hello'
print(str1.replace('ello', 'i'))
# hi

# 7、Str.split(“分割”)
str1 = '星期一,星期二,星期三'
list1 = str1.split(',')
print(list1)
# ['星期一', '星期二', '星期三']

# 8、去空白符
# str.lstrip，去掉左边（开始）的空白字符 返回一个新的字符
str1 = '  he llo  '
print(str1.lstrip())
# he llo
# str.rstrip, 去掉右边（末尾）的空白字符 返回一个新的字符
print(str1.rstrip())
# he llo
# str.strip ,去掉开始和末尾的空白字符  返回一个新的字符
print(str1.strip())
# he llo
# 去掉中间字符串的方法有三种
# 1、str.replace()
print(str1.replace(' ', ''))
# hello
# 2、''.join(str1.split())
print(''.join(str1.split()))
# hello
# re.sub(" ", str1)

# 9、字符串切片
str1 = "abcdefghijklmn"
print(str1[::-1])  # 倒序  步长值是负数  是倒序
# nmlkjihgfedcba
print(str1[0:4])  # 等价于print(str[:4])
# abcd
print(str1[4:])
# efghijklmn
print(str1[:])
# abcdefghijklmn
