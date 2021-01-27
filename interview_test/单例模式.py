


class Sington(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
            return cls._instance
        else:
            return cls._instance

sington1 = Sington()
sington2 = Sington()

print(sington1)
print(sington2)

"""共享属性"""
class Blog(object):

    _state = {"name": "maoqiansheng"}
    def __new__(cls, *args, **kwargs):
        ob = super(Blog, cls).__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        return ob

a = Blog()
b = Blog()

print(a._state)
print(b._state)
