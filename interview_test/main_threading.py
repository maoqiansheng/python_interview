#coding=utf-8
import threading
from time import sleep,ctime
def sing():
    for i in range(3):
        print("正在唱歌...%d"%i)
        sleep(1)
def dance():
    for i in range(3):
        print("正在跳舞...%d"%i)
        sleep(1)
if __name__ == '__main__':
    print('---开始---:%s'%ctime())
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    # sleep(5) # 屏蔽此⾏代码，试试看，程序是否会⽴⻢结束？
    print('---结束---:%s'%ctime())