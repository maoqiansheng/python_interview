A = [1, 2, 3, [4, 1, ['j1', 1, [1, 2, 3, 'aa']]]]


# def my_print(lis):
#     for i in lis:
#         if type(i)==list:
#             my_print(i)
#         else:
#             print(i)
# my_print(A)

def print_elem(li):
    for i in li:
        if type(i) == list:
            print_elem(i)
        else:
            print(i)


print_elem(A)

a = list(range(10))
print(a[::-3])
lst = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 32769, 65536, 4294967296]


def merge_dict(lst):
    new_dict = dict()
    for i in lst:
        nums = len(str(i))
        new_dict.setdefault(nums, []).append(i)
    return new_dict


print(merge_dict(lst))

shuffle_list = [7, -8, 5, 4, 0, -2, -5]
new_list = sorted(shuffle_list, key=lambda x: (x < 0, abs(x)))
print(new_list)

