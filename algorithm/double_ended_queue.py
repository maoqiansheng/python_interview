"""

双端队列：是一种具有队列和栈性质的数据结构
双端队列中的元素可以从两端弹出，其限定插入和删除操作在表的两端进行。双端队列可以在队列任意一端入队和出队。


"""


class DoubleEndQueue(object):
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        self.__list.insert(0, item)

    def add_end(self, item):
        self.__list.append(item)

    def pop_front(self):
        return self.__list.pop(0)

    def pop_end(self):
        return self.__list.pop()

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)
