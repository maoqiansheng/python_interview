"""
队列（queue）是只允许在一端进行插入操作，而在另一端进行删除操作的线性表。
队列是先进先出（First in First out）的线性表
顺序表中无论从哪一端添加，另一端获取，总有一端是O(n)

"""


class Queue(object):
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        self.__list.append(item)
        # self.__list.insert(0, item)

    def dequeue(self):
        return self.__list.pop(0)
        # return self.__list.pop()
        pass

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)

if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())