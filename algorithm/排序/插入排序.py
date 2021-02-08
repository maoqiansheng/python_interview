"""
alist = [54,226,93,17,77,31,44,55,20]
插入排序和选择排序的思想类似，都是把原有的数组分成有序和无序的两部分
插入排序是通过从无序的数组中，依次取出一个元素插入到有序数组的合适的位置

"""


def insert_sort(alist):
    n = len(alist)
    # 从第二个元素开始向前插入
    for i in range(1, n):
        # 比较的次数为i向前的元素的个数
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
    return alist


if __name__ == '__main__':
    alist = [54, 226, 93, 17, 77, 31, 44, 55, 20]
    print(alist)
    print(insert_sort(alist))
