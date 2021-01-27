# 使用父类的地方，使用子类
class Meat(object):
    def __init__(self):
        self.name = "肉"
        self.weight = 2
        self.color = "红"


# 火腿
class Ham(Meat):
    def __init__(self):
        # 父类名,方法名(self)
        Meat.__init__(self)  # 使用父类的方法  调用被重写的父类
        self.name = "火腿"


# 地瓜
class Potato(object):
    def __init__(self):
        self.name = "地瓜"
        self.color = "黄色"
        self.type = "蔬菜"


class Persion:
    def eat(self, obj):
        print("吃%s" % obj.name)


rou = Meat()
ham = Ham()
dg = Potato()
luhan = Persion()
luhan.eat(dg)  # 对象的地址 给obj     ,obj引用该空间的数据
# 鸭子类型，长得像鸭子类型  ，可以没有继承关系
luhan.eat(rou)
luhan.eat(ham)