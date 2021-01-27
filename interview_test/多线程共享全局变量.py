import threading
import time

# 定义全局变量
num = 0


def work1():
    # 使⽤ global 声明全局变量，表示后续的操作，都是操作去全局变量num
    global num
    for i in range(10):
        mutex.acquire()
        num += 1
        mutex.release()
        print("work1 num = %d" % num)


def work2():
    print("work2 num = %d" % num)


mutex = threading.Lock()
if __name__ == '__main__':
    # 创建⼦线程
    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)
    # 启动⼦线程
    t1.start()
    #t1.join()
    t2.start()
    # while 循环的作⽤是：能保证⼦线程运⾏完毕，再去输出 num
    while len(threading.enumerate()) != 1:
        time.sleep(1)
    print("num = ", num)
# 结论：全局变量可以在多个线程中进⾏共享使⽤
# 缺点就是，线程是对全局变量随意遂改可能造成多线程之间对全局变量的混乱（即线程⾮安全）
