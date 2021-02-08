"""
栈：一种容器，特点是只能从容器的一端（栈顶）储存元素和输出数据的运算，后进先出（Last in First out），
保证每次操作的都是最后一次储存的元素

"""


class Stack(object):
    """栈"""

    def __init__(self):
        self.__list = []

    def push(self, item):
        # 使用顺序表的尾部去压栈，原因append是时间复杂度为O(1)
        self.__list.append(item)

    def pop(self):
        return self.__list.pop()

    def peek(self):
        # 返回栈顶的元素
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        # return not self.__list
        return self.__list == []

    def size(self):
        return len(self.__list)


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.size())
    print(s.peek())
    s.pop()
    print(s.peek())
    s.pop()
    print(s.peek())
    s.pop()
    print(s.peek())
    s.pop()
