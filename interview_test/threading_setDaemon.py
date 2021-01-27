import threading
import time
def work1():
    for i in range(10):
        print("正在执⾏...", i)
        time.sleep(0.5)
if __name__ == '__main__':
    #
    # 创建⼦线程
    t1 = threading.Thread(target=work1)
    # 设置⼦线程 t1 为守护线程
    t1.setDaemon(True)
    # 启动⼦线程
    t1.start()
    # 睡2秒
    time.sleep(2)
    print("Game Over")
    # 让程序退出
    # 当主线程睡眠2秒，开始结束字节的时候，但是⼦线程还没有结束，默认情况下，⼦线程继续执⾏
    # exit() 退出⽆效
    # 如果想让主线程结束的时候，没有执⾏完成的⼦线程也⼀起结束，这就是 线程守护
    exit()