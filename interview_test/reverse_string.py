# 用Python 语言写一个函数，输入一个字符串，返回倒序结果？
def reverse_string():
    input_str = input('请输入需要反转的字符串：')
    return input_str[::-1]

print(reverse_string())