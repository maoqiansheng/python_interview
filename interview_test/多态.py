# 定义一个肉类
# 调用父类的方法，也可以调用子类的方法
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
