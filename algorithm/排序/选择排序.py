
"""

选择排序的实现逻辑：
    先从列表中找到最小值，把它放到列表的第一位，然后从剩余的元素中再找到最小值，放到第二位，以此类推
"""


def select_sort(alist):
    n = len(alist)
    # 最后一个元素不需要遍历比较，所有遍历0～n-2
    for i in range(n-1):
        # 假设第一个元素是最小值的下标
        min_index = i
        # 从第二个元素到最后一个元素跟alist[i]比较，目的是找到后续列表中最小的元素
        for j in range(i+1, n):  # i+1~n-1
            # 如果有比alist[i]更小的值，最小值的下标就是该值alist[j]的下标j
            if alist[j] < alist[min_index]:
                min_index = j
        # 如果最小值下标不是我们假设的那样，则交换两个元素的位置
        if min_index != i:
            alist[i], alist[min_index] = alist[min_index], alist[i]
    return alist


if __name__ == '__main__':
    alist = [33, 27, 38, 77, 35, 66, 49, 99, 87]
    print(alist)
    print(select_sort(alist))