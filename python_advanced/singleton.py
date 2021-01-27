

class Singoton(object):
    _instance = None
    _singoton_flag = True
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
            return cls._instance
        else:
            return cls._instance

    def __init__(self, name):
        self.name = name
        if Singoton._singoton_flag:
            print('%s' % name)
            self.name = name
            Singoton._singoton_flag = False


a = Singoton('mao')
print(a._instance)
b = Singoton('qian')
print(b._instance)