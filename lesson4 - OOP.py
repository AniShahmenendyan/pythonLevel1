'''Exceptions'''


class MyException(Exception):
    pass


def check(n):
    if n == 12:
        raise MyException
    return n


def devide(a, b):
    try:
        res = a / b
        check(res)
        # return res
    except ZeroDivisionError as err:
        print('division by zero')
        res = -1
    except TypeError:
        res = -1
        print('unsupported operand types')
    except MyException:
        res = -1
        print('result can not be 12')
    # except Exception:
    #     res = -1
    #     print('other cases')
    # else:
    #     print('function run without exception')
    # finally:
    #     print('finally')

    return res


# print(devide(36, 3))

'''OOP basics'''

a = int()
s = str()
l = list()


class A:
    pass


a = A()
a_2 = A()


# print(a)
# print(a_2)


class Car:
    car_total_numbers = 0
    wheels = 4

    def __init__(self, model_name, color, age_year):
        self.model = model_name
        self.color = color
        self.age = age_year

        self.speed = 0

        Car.car_total_numbers += 1

    def add_speed(self):
        if self.speed > 250:
            print('max speed limit')
        else:
            self.speed += 20

    def down_speed(self):
        if self.speed < 0:
            print('min speed limit')
        else:
            self.speed -= 20

    def __del__(self):
        Car.car_total_numbers -= 1


bmw = Car('bmw', 'black', 2022)
ww = Car('ww', 'green', 2021)
# print(bmw.color)
# print(bmw.model)
# print(bmw.age)
# print(bmw.wheels)
print(id(Car.car_total_numbers))
print(id(bmw.car_total_numbers))


# bmw.car_total_numbers = 12
# print(Car.car_total_numbers)
# print(bmw.car_total_numbers)

# bmw.add_speed()
# bmw.add_speed()
# bmw.add_speed()
# print(bmw.speed)


class Animal:
    kingdom = 'Animalia'

    def __init__(self, name, age, color, has_tail=True):
        self.name = name
        self.age = age
        self.color = color
        self.has_tail = has_tail
        self.energy = 100

    def speak(self):
        self.energy -= 10
        if self.energy < 0:
            print('Go to eat')

    def eat(self):
        self.energy = 100

    def alert(self):
        print('alert')


a = Animal('Bob', 12, 'white')
print(a.__dict__)
print(a.energy)


class Bird(Animal):
    def __init__(self, name, age, color, has_tail=True, can_fly=True):
        super().__init__(name, age, color, has_tail)
        self.can_fly = can_fly

    def speak(self):
        super().speak()
        print('Hello')

    def alert(self):
        super().alert()
        print('bird alert')

parrot = Bird('Kesha', 1, 'yellow')
parrot.speak()


class Parrot(Bird):
    def alert(self):
        print('Parrot alert')


p = Parrot('Kesha', 2, 'blue')
p.alert()