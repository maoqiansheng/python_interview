import socket
import threading
import time


def sing():
    for i in range(10):
        print("------------------------------")
        time.sleep(0.5)


def dance():
    for i in range(10):
        print("-----")
        time.sleep(0.5)


if __name__ == '__main__':
    # 创建两个⼦线程
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    # 启动⼦线程
    t1.start()
    t2.start()

# 由此可见，线程的执行顺序是不确定的，无关的
