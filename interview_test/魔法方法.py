class Person():
    def __init__(self):
        self.name = 'maoqiansheng'
        self.age = 18
        self.gender = 'man'

    def __str__(self):
        return "我的名字是{}, 年龄{}， 性别{}".format(self.name, self.age, self.gender)


mao = Person()
print(mao)


class Persion():
    # def __del__(self):
    #     print("我被干掉了")

    def __str__(self):
        return "str"

    def __repr__(self):
        return "repr"


lh = Persion()
lh
print(lh)
