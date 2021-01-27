"""

求两个字符串的公共字符串
str1 = "abcdefg"
str2 = "efghijk"
"""


# 自己的实现思路
def get_common_string(str1, str2):
    list1 = [x for x in str1]
    list2 = [x for x in str2]
    common = set(list1) & set(list2)
    commons = list(common)
    common_string = ','.join(commons)
    return common_string


print(get_common_string("abcdefg", "efghijk"))

# 标准的思路


def getLCSstring(str1, str2):
    maxlen = len(str1) if len(str1) < len(str2) else len(str2)
    example = str1 if len(str1) < len(str2) else str2
    other = str2 if str1 == example else str1
    for i in range(maxlen):
        for j in range(maxlen, 0, -1):
            if other.find(example[i:j]) != -1:
                return example[i:j]


print(getLCSstring('abcdefg', 'efghijklmn'))