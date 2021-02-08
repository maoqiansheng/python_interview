"""

冒泡排序：排序算法的基本思想

"""


def bubble_sort(alist):
    for i in range(len(alist)-1, 0, -1):
        for j in range(i):
            if alist[i] < alist[j]:
                alist[i], alist[j] = alist[j], alist[i]
    return alist


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(alist)
    print(bubble_sort(alist))
