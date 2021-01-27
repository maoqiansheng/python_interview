# coding=utf-8
import threading
from time import sleep, ctime


def sing(a, b, c):
    print(a)
    print("----sing----a = %d, b = %d,c = %d" % (a, b, c))
    for i in range(5):
        print("正在唱歌...%d" % i)
        sleep(1)


def dance():
    for i in range(5):
        print("正在跳舞...%d" % i)
        sleep(1)
if __name__ == '__main__':
    print('---开始---:%s' % ctime())
    t1 = threading.Thread(target=sing, args=(10,),kwargs={"b": 100, "c": 100})
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    while True:
        length = len(threading.enumerate())
        print('当前运⾏的线程数为：%d' % length)
        if length <= 1:
            break
        sleep(0.5)
