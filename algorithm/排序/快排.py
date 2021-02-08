"""
快排的思想：
    把数组分成两部分，每个部分再递归排序
步骤：
1、从数列中挑出一个基准（mid）
2、重新排序数列，比基准小的放前面， 比基准大的放后面
3、递归的排序前后两个数列

"""


def quick_sort(alist, start, end):
    # 1、递归退出的条件
    if start >= end:
        return
    # 2、设定起始元素就是我们的基准元素,low为序列左端由左到右移动的游标high为序列右端由右到左移动的游标
    mid = alist[start]
    low = start
    high = end
    # 3、执行排序逻辑
    while low < high:
        # 当alist[high]不小于mid时，右端游标向左移动
        while low < high and mid <= alist[high]:
            high -= 1
        # 否则将high指向的元素放到low的位置上，不是交换
        alist[low] = alist[high]
        # 当alist[low]小于mid时，左端游标向右移动
        while low < high and mid > alist[low]:
            low += 1
        # 否则将low指向的元素放到high的位置
        alist[high] = alist[low]
    # 4、退出循环，也就是low==high
    alist[low] = mid
    # 5、对基准左边的子序列进行快速排序
    quick_sort(alist, start, low-1)
    # 对基准右边的子序列进行快速排序
    quick_sort(alist, low+1, end)
    return alist


if __name__ == '__main__':
    alist = [54, 226, 93, 17, 77, 31, 44, 55, 20]
    print(alist)
    print(quick_sort(alist, 0, len(alist)-1))