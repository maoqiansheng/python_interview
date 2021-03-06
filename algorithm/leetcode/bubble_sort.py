"""
冒泡排序思想：通过无序区中相邻记录的关键字间的比较和位置的交换，使关键字最小的记录像气泡一
样逐渐向上漂至水面。整个算法是从最下面的记录开始，对每两个相邻的关键字进行比较，把关键字较
小的记录放到关键字较大的记录的上面，经过一趟排序后，关键字最小的记录到达最上面，接着再在剩
下的记录中找关键字次小的记录，把它放在第二个位置上，依次类推，一直到所有记录有序为止
复杂度：时间复杂度为O（n2）,空间复杂度为O(1)

"""


def bubble_sort(alist):
    for j in range(len(alist) - 1, 0, -1):
        # j 表示每次遍历需要比较的次数，是逐渐减小的
        for i in range(j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(li)
print(li)
