"""

python彪悍的特性.
自省就是面向对象的语言所写的程序在运行时,所能知道对象的类型.简单一句就是运行时能够获得对象的类型.
比如type(),dir(),getattr(),hasattr(),isinstance().
"""
a = 'hello'

print(type(a))
print(dir(a))


class A(object):

    def eat(self):
        print('吃饭')


class_func = getattr(A, 'eat')
print(class_func)

if hasattr(A, 'eat'):
    print(True)
    

if isinstance(a, str):
    print(True)