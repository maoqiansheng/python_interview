import multiprocessing
import time
import os
# 定义函数
def work1():
    for i in range(10):
        print("work1----", i, multiprocessing.current_process().pid, os.getpid(), os.getppid())
        time.sleep(0.5)
if __name__ == '__main__':
    # 创建进程
    # 1. 导⼊ multiprocessing 模块
    # 2. multiprocessing.Process() 创建⼦进程
    # 3. start() ⽅法启动进程
    p1 = multiprocessing.Process(group=None, target=work1)
    p1.start()
    for i in range(10):
        print("这是主进程", i)
        time.sleep(0.5)
