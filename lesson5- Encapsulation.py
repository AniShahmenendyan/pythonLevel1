class Thermometer(object):

    counter = 0

    def __new__(cls, *args, **kwargs):
        Thermometer.counter += 1
        print('new call')
        print(f'class name is {cls}')
        inst = object.__new__(cls)
        return inst

    def __init__(self, t):
        print('init call')
        self.t = t

    def increase_t(self, a):
        self.__t += a

    @property
    def t(self):
        print('call getter')
        return self.__t

    @t.setter
    def t(self, t):
        if t > -273.15:
            self.__t = t
        else:
            raise ValueError

    def __str__(self):
        return f'Thermomether with {self.t}C'

    def __add__(self, other):
        if isinstance(other, Thermometer):
            return Thermometer(self.t + other.t)
        else:
            raise ValueError

    def __sub__(self, other):
        if isinstance(other, Thermometer):
            return Thermometer(self.t - other.t)
        else:
            raise ValueError

    def __mul__(self, other):
        if isinstance(other, Thermometer):
            return Thermometer(self.t * other.t)
        else:
            raise ValueError

    def __eq__(self, other):
        return self.t == other.t

    def __int__(self):
        return self.t

    def __del__(self):
        Thermometer.counter -= 1


t_instance = Thermometer(123)
t_instance_1 = Thermometer(123)
t_instance_2 = Thermometer(123)
t_instance_3 = Thermometer(123)


print(Thermometer.counter)
del t_instance
print(Thermometer.counter)

# t_instance_2 = Thermometer(123)
# print(int(t_instance))
