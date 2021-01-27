import re  # 面试宝典312
# 一旦匹配上返回的是一个match对象，
print(re.match(r'super', 'supermarket'))  # <re.Match object; span=(0, 5), match='super'>
print(re.match(r'super', 'supermarket').start())  # 返回匹配开始的位置
print(re.match(r'super', 'supermarket').end())    # 返回匹配结束的下标
print(re.match(r'super', 'supermarket').span())  # 返回开始和结束的元组
print(re.match(r'super', 'supermarket').group())  # 返回re匹配的字符串

# 邮箱匹配
print(re.match(r'\w{4,20}@163.com| 100', '18137803201@163.com').group())
print(re.match(r'\w{4,20}@163.com|100', '100').group())
print(re.match(r'\w{4,20}@(163|126|qq).com', '18137803201@163.com').group())
print(re.match(r'\w{4,20}@(163|126|qq).com', '18137803201@126.com').group())
print(re.match(r'\w{4,20}@(163|126|qq).com', '18137803201@qq.com').group())
# 手机号匹配,尾号不是4和7
print(re.match(r'1\d{9}[0-35-68-9]', '18137803201').group())

# 分组匹配
# 提取区号和电话号码
result = re.match("(\d{3,4})-(\d{7,8})", "010-12345678")
# 判断匹配结果
if result:
    print(result.group(1))
    print(result.group(2))

# serach
import re
print(re.search(r'\d+', '阅读次数为9999').group())
# findall
print(re.findall(r'\d+', '阅读次数:9999次,转发次数:883次,评论次数:3次'))
# sub
ret = re.sub(r"\d+", "10000", "阅读次数:9999次,转发次数:883次,评论次数:3次")
print(ret)

# split
# 按：和空格切割成一个列表
ret = re.split(r":| ","info:xiaoZhang 33 shandong")
print(ret)
# 按空格切割成一个列表
rets = re.split(r"\s+", "info:xiaoZhang 33 shandong")
print(rets)

# 贪婪和非贪婪
# 匹配多个数字
result = re.match(r"aaa(\d?)", "aaa123456")
if result:
    print(result.group())
else:
    print("匹配失败～！")

# r 字符串前加r表示原生字符串
