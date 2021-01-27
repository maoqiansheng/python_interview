# 单线程执行，
# import time
#   def saySorry():
#   print("亲爱的，我错了，我能吃饭了吗？")
#   time.sleep(1)
# if __name__ == '__main__':
#   for i in range(5):
#       saySorry()
import time
import threading


def saySorry():
    print("亲爱的，我错了，我能吃饭了吗？\n")
    time.sleep(1)


if __name__ == '__main__':
    for i in range(5):
        # 创建⼦线程的的⽅法
        # 1、导⼊ threading 模块
        # 2、使⽤ threading.Tread() ⽅法，创建⼦线程对象
        # threading.Thread(target=函数名, args=(参数列表，元组))
        t1 = threading.Thread(target=saySorry)
        # 3、使⽤⼦线程对象调⽤start() ⽅法，可以开启⼦线程（⼦线程将同时执⾏）
        t1.start()
    print("我是主线程")

"""
1、多线程执行耗费时间更短
2、当调用start（）时候才真正创建了线程
3、每个线程都有唯一标识符，来区分主次
4、主线程:mainThread,Main函数或者程序主⼊⼝，都可以称为主线程
5、⼦线程:Thread-x 使⽤ threading.Thread() 创建出来的都是⼦线程
6、线程数量：主线程数 + ⼦线程数
"""