"""

快排的基本思想：通过一躺排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比
另外一不部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可
以递归进行，以此达到整个数据变成有序序列。
复杂度：快速排序是不稳定的排序算法，最坏的时间复杂度是O（n2）,最好的时间复杂度是(nlogn),
空间复杂度为O(logn)
"""


def quick_sort(alist, start, end):
    """快速排序"""
    # 递归的退出条件
    if start >= end:
        return
    # 设定起始元素为要寻找位置的基准元素
    mid = alist[start]
    # low 为序列左边的由左向右移动的游标
    low = start
    # high 为序列右边的由右向左移动的游标
    high = end
    while low < high:
        # 如果low 与high 未重合，high 指向的元素不比基准元素小，则high 向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        # 将high 指向的元素放到low 的位置上
        alist[low] = alist[high]
        # 如果low 与high 未重合，low 指向的元素比基准元素小，则low 向右移动
        while low < high and alist[low] < mid:
            low += 1
        # 将low 指向的元素放到high 的位置上
        alist[high] = alist[low]
    # 退出循环后，low 与high 重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid

    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low-1)
    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low+1, end)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(alist, 0, len(alist)-1)
print(alist)
