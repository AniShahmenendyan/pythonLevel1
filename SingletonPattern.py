# import single
#
# Single.increment()
# print(single.x)
# single.increment()
# single.increment()
# single.increment()
# print(single.x)

class Singleton:
    _instance: object = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is not None:
            return cls._instance
        cls._instance = super().__new__(cls, *args, **kwargs)
        cls._instance.x = 0
        return cls._instance

    def increment(self):
        self.x += 1

    def decrement(self):
        self.x -= 1

    def __str__(self):
        return str(self.x)

# a = Singleton()
# a.increment()
# a.increment()
# print(a)
# a.decrement()
# print(a)
#
# b = Singleton()
# b.increment()
# b.increment()
# b.increment()
# b.increment()
# print(b)
