"""
给一个不定长的列表，把它分成7组，可以为空[]

"""

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
new_list = [[] for _ in range(7)]
for i, v in enumerate(list1):
    new_list[i % 7].append(v)
print(new_list)