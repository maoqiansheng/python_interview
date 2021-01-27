import multiprocessing
import time
def sub_process():
    for i in range(10):
        print("⼦进程运⾏中", i)
        time.sleep(0.5)
if __name__ == '__main__':
    # 创建⼦进程
    p1 = multiprocessing.Process(group=None, target=sub_process, name="p1")
    # 设置守护主进程
    # 第⼀种⽅式:
    # p1.daemon = True
    # 第⼆种⽅式(最好在退出exit()前⼀句使⽤):
    # p1.terminate()
    # 启动
    p1.start()
    time.sleep(2)
    print("OVER!")
    p1.terminate()
    exit()
