# 1. Create a custom integer class. The class should have one instance attribute as its value. Now, your class must
# satisfy the following criteria:
#    a) we can use Python arithmetic operators to add, subtract, multiply and divide the values.
#    b) create another class called Inf. For the sake of consistency, this class may inherit from int class.
#    c) if we divide by zero, we don't get an exception. Instead, we get inf, which was implemented in our previous step
#    d) when we print our class, we want it to be represented as nicely as possible. As our class represents an integer
#    number, we want to see the value when we print it or cast it to a string.
#    e) as with every number, we want to be able to compare our integer instances using the logical operators.
#    Implement those as well.
#    f) finally, there is one thing that all Python objects have in common. If we neglect 0, '', None, False etc., then
#    every object holds a value of True when casted to bool. We want our Integer to behave as a normal integer in this
#    sense. When we cast an Integer to bool, we must get False, if the value of our object is 0. True otherwise.


class Integer(int):
    def __init__(self, val):
        if type(val) != int:
            raise TypeError('Integer value must be int')
        self.val = val

    def __add__(self, other):
        self.type_check(other)
        return Integer(self.val + other.val)

    def __sub__(self, other):
        self.type_check(other)
        return Integer(self.val - other.val)

    def __mul__(self, other):
        self.type_check(other)
        return Integer(self.val * other.val)

    def __truediv__(self, other):
        self.type_check(other)
        if other.val == 0:
            return Inf()

        return self.val / other.val

    def __bool__(self):
        return False if self.val == 0 else True

    @staticmethod
    def type_check(second_operand):
        if not isinstance(second_operand, Integer):
            raise TypeError('instances must be Integer')

    def __str__(self):
        return str(self.val)


class Inf(Integer):
    def __init__(self, val=0):
        super().__init__(val)

    def __str__(self):
        return 'inf'


# x = Integer(True)
# y = Integer(0)
#
# print(x)


# print(x / y)
#
# print(x + z)
# 2. Create a Color class. This will hold 3 instance variables, red, green, blue (RGB).
# Each parameter (red, green, and blue) defines the intensity of the color as an integer between 0 and 255. We want to be able to get new
# colors if we add instances of the color class. I'm not sure how much sense it will make to also subtract the colors,
# but lets do it for fun! In summary, we can add 2 or more colors and get a new color object with added RGB values
# (don't forget about the boundaries!), subtract them to get a new color object with subtracted values. When printed,
# we want to have a nice representation of our color (maybe even the color itself?). One more fun thing! As colors
# are quite often represented in hexadecimals, lets override the corresponding function such that when hex() is called
# on our class, we get the hex color code for our color.

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    # def r_getter(self):
    #     return self._r
    #
    # def r_setter(self, r):
    #     if r in range(0, 256):
    #         self._r = r
    #     else:
    #         raise ValueError
    #
    # r = property(r_getter, r_setter)

    # @property
    # def rgb(self):
    #     return self.__red, self.__green, self.__blue
    #
    # @rgb.setter
    # def rgb(self, rgb):
    #     r, g, b = rgb
    #
    #     self.__red = self.color_range(r)
    #     self.__green = self.color_range(g)
    #     self.__blue = self.color_range(b)

    @property
    def r(self):
        return self.__red

    @r.setter
    def r(self, r):
        self.__red = self.color_range(r)

    @property
    def g(self):
        return self.__green

    @g.setter
    def g(self, g):
        self.__green = self.color_range(g)

    @property
    def b(self):
        return self.__blue

    @b.setter
    def b(self, b):
        self.__blue = self.color_range(b)

    def __add__(self, other):
        self.type_check(other)
        return Color(self.r + other.r, self.g + other.g, self.b + other.b)

    def __sub__(self, other):
        self.type_check(other)
        return Color(self.r - other.r, self.g - other.g, self.b - other.b)

    @staticmethod
    def type_check(second_operand):
        if not isinstance(second_operand, Color):
            raise TypeError('instances must be Color')

    @staticmethod
    def color_range(v):
        return max(0, min(v, 255))

    def rgb_hex(self):
        return '#{:02x}{:02x}{:02x}'.format(self.r, self.g, self.b)

    # def __hex__(self):

    def __str__(self):
        return f'r:{self.r}, g:{self.g}, b:{self.b}'


c = Color(10, 20, 30)
c_2 = Color(20, 30, 250)
print(c + c_2)
# c.r_setter(300)
# c.r = 300
# c.g = -200
print(c)
