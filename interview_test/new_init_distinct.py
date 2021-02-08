"""
object这个类对象的id为4496300080
Person这个类对象的id为140325150803904
__new__被调用， cls的id为140325150803904
创建对象的id为4499084912
__init__被调用，self对象的id为4499084912
p1实例子对象的id4499084912
1、 用法不同
    new用于创建实例，在实例创建之前被调用。是类级别的方法，是静态方法
    init是初始化实例方法，在实例创建之后先被调用，是实例级别的方法，用于设置对象属性的一些初始值。

2、传参不同
    new()至少有一个参数cls,表示当前类，此参数在实例化时由python解释器自动识别
    init()的至少又一个参数self,就是这个new方法的返回实例，init在new的基础上做一系列的操作
3、返回值不同
    new方法返回的是一个实例
    init一般没有返回值
"""

class Person(object):
    def __new__(cls, *args, **kwargs):
        print('__new__被调用， cls的id为{}'.format(id(cls)))
        obj = super().__new__(cls)
        print('创建对象的id为{}'.format(id(obj)))
        return obj

    def __init__(self, name, age):
        print('__init__被调用，self对象的id为{}'.format(id(self)))
        self.name = name
        self.age = age


print('object这个类对象的id为{}'.format(id(object)))
print('Person这个类对象的id为{}'.format(id(Person)))

p1 = Person('张三', 20)
print('p1实例子对象的id{}'.format(id(p1)))

