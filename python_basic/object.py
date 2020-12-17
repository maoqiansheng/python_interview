# 1、魔法方法
# __init__：当实例化一个对象的时候会自动调用该方法，在类的内部定义对象的属性
# __str__：打印类名会直接输出str的return结果


class Person():
    def __init__(self):
        self.name = 'maoqiansheng'
        self.age = 18
        self.gender = 'man'

    def __str__(self):
        return "我的名字是{}, 年龄{}， 性别{}".format(self.name, self.age, self.gender)


mao = Person()
print(mao)
# 我的名字是maoqiansheng, 年龄18， 性别man

# __del__：当对象被销毁前自动调用该方法
# 应用场景：做一些额外的工作，比如：垃圾回收(释放变量)、关闭文件或文件夹


class Persion():
    def __del__(self):
        print("我被干掉了")

    def __str__(self):
        return "此刻我还有用"
    # 删除 销毁一个对象的时候 自动调用该方法


lh = Persion()
print(lh)
print("*" * 40)
# 此刻我还有用
# ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
# 我被干掉了

# __repr__：repr()
# 函数将对象转化为供解释器读取的形式
# 直接调用类会输出repr的输出

class A():

    def __repr__(self):

        return 'repr'


    def __str__(self):

        return 'str'


a = A()
#>>> a  # 直接输出调用的是repr方法
# repr
print(a)  # print调用的是str方法
# str

# repr的使用场景：可以得出只有当repr再次作用在字符串上时会多一层引号，那么这一特性在拼接完字符串用eval执行时是特别有用的，如果不用repr而是采用str会报错
# >> > s = 'abdcf'
# >> > eval('[' + ','.join([repr(i) for i in s]) + ']')
# ['a', 'b', 'd', 'c', 'f']
# >> > eval('[' + ','.join([str(i) for i in s]) + ']')  # str报错
# Traceback(most recent call last):
# File
# "<stdin>", line
# 1, in < module >
# File
# "<string>", line
# 1, in < module >
# NameError: name
# 'b' is not defined

# 2、调用被重写的父类的方法
# super(类名， self).方法名（），super函数会查询继承链中指定类的下一个类
# super().方法名（），默认当前类的下一个类


class Dog(object):
    def dark(self):
        print("汪汪叫")


class Xtq(Dog):
    def dark(self):
        print("嗷嗷叫")

    # 看到了主人方法
    def see_host(self):
        # 当前类的下一个类的方法  查看继承连
        # super().dark()   # Dog.dark()  (<class '__main__.Xtq'>, <class '__main__.Dog'>, <class 'object'>)
        # super(类名,self).dark()
        super(Xtq, self).dark()  # 指定Xtq 类的下一个类的方法


god = Xtq()
god.see_host()
print(Xtq.__mro__)
# 汪汪叫
# (<class '__main__.Xtq'>, < class '__main__.Dog' >, < class 'object' > )

# 3、多继承的调用顺序
# 谁在前继承谁


# class Child(Father, Mother):
#     pass


# 如果多个父类的的方法名一样，哪个父类在前就继承哪个父类的方法

# 4、多态
# 使用父类的地方，使用子类也可以


# 定义一个肉类
class Meat(object):
    def __init__(self):
        self.name = "肉"
        self.weight = 2


class Ham(Meat):
    def __init__(self):
        super().__init__()
        self.name = "火腿"


class Persion:
    def eat(self, obj):
        print("我喜欢吃%s" % obj.name)


rou = Meat()
huo = Ham()
obj = Persion()
obj.eat(huo)
obj.eat(rou)
# 我喜欢吃火腿
# 我喜欢吃肉


