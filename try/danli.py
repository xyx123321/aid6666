class Person(object):
    eat=None
    def __new__(cls, *args, **kwargs):
        if cls.eat==None:
            cls.eat=object.__new__(cls)
            return cls.eat
        else:
            return cls.eat


a=Person()
b=Person()
print(a is b)
