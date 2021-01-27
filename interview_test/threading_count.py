# coding=utf-8
import threading
from time import sleep, ctime


def sing():
    for i in range(3):
        print("正在唱歌...%d" % i)
        print(threading.current_thread())
        sleep(1)


def dance():
    for i in range(3):
        print("正在跳舞...%d" % i)
        print(threading.current_thread())
        sleep(1)


if __name__ == '__main__':
    print('---开始---:%s' % ctime())
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    while True:
        length = len(threading.enumerate())
        print(threading.current_thread())
        print('当前运⾏的线程数为：%d' % length)
        if length <= 1:
            break
        sleep(0.5)
# 查看当前的线程数量，len(threading.enumerate())
