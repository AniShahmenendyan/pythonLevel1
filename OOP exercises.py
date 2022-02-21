""" OOP """
# 1. Create Animal class with three methods - make_noise(), walk() and fly(). The methods shall print what the animal is
# doing. Then, create a Bird and Feline classes which inherit from Animal. Override the superclass methods, so that
# a cat warns us that it can't fly and the bird only wants to fly as it is too lazy to walk.
# Ստեղծել Animal կլասս, որը կունենա երեք մեթոդ՝ make_noise(), walk() և fly()։ Այդ մեթոդները պետք է տպեն, թե ինչ է անում
# կենդանին։ Ապա ստեղծել Bird և Feline կլասեր, որոնք ժառանգում են Animal-ից։ Animal-ի մեթոդները իմպլեմենտացրեք
# այդ կլասերի մեջ, այնպես, որ եթե կատուն փորձի թռչել, կոնսոլում տպվի, որ նա չի կարող թռչել։ Իսկ եթե թռչնի վրա
# կիրառենք walk() մեթոդը, նա ասի, որ ալարում է և միայն կարող է թռչել։
import abc
from math import pi


class Animal:

    @staticmethod
    def make_noise():
        print('making noise')

    def walk(self):
        pass

    def fly(self):
        pass


class Bird(Animal):
    def walk(self):
        print('I am too lazy')

    def fly(self):
        print('I am flying')


b = Bird()
b.fly()
Animal.make_noise()
b.walk()


class Feline(Animal):

    def walk(self):
        print('I am walking')

    def fly(self):
        print('I can\'t fly. I only walk.')


f = Feline()
f.make_noise()
f.walk()
f.fly()


# 2. Create a calculator class. It will have 2 numerical instance attributes. Then declare 4 methods called add, sub,
# mult, div to respectively add, subtract, multiply and divide the attributes.
# Ստեղծել կալկուլատորի կլաս։ Այն պետք է ունենա երկու instance attribute։ Ապա ստեղծել չորս մեթոդ՝ add, sub,
# mult, div, որոնք համապատասխանաբար կգումարեն, կհանեն, կբազմապատկեն և կբաժանեն այդ ատրիբուտները։

class Calculator:
    def __init__(self, a, b):
        if type(a) in [int, float] and type(b) in [int, float]:
            self.a = a
            self.b = b
        else:
            raise ValueError("Must be an integer")

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b


c = Calculator(5, 10)


# print(c.mul())
# print(c.sub())
# print(c.divide())

# 3. Create a class called Shape. Define methods to calculate the shape's perimeter and the area.
# Ստեղծել Shape անունով կլաս։ Սահմանել մեթոդներ, սակայն չիմպլեմենտացնել (մեթոդի մեջ պարզապես գրել pass) երկու մեթոդ,
# դրանք անվանելով perimeter և area։

class Shape(abc.ABC):

    @abc.abstractmethod
    def perimeter(self):
        ...

    @abc.abstractmethod
    def area(self):
        ...


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Triangle(Shape):
    def __init__(self, a, b, c):
        if self.checkTriangle(a, b, c):
            self.a = a
            self.b = b
            self.c = c
        else:
            raise TypeError

    @staticmethod
    def checkTriangle(a, b, c):
        if a < b + c and b < a + c and c < a + b:
            return True
        else:
            return False

    def area(self):
        half = (self.a + self.b + self.c) / 2
        return (half * (half - self.a) * (half - self.b) * (half - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c


t = Triangle(6, 8, 10)
print(t.area())
print(t.perimeter())
# print(Triangle.checkTriangle(1, 5, 8))

# 4. Create a Circle class which will inherit from Shape. Implement the constructor and superclass methods to correctly
# calculate the perimeter and the area of the circle.
# Ստեղծել Circle կլաս, որը կժառանգի Shape-ից։ Իմպլեմենտ արեք կոնստրուկտորը (շրջանագծի դեպքում կունենանք մեկ instance
# attribute` շառավիղը) և Shape-ի երկու մեթոդներն այնպես, որ Circle տիպի օբյեկտի վրա կիրառենք perimeter-ը, կստանանք
# շրջանագծի երկարությունը, իսկ area-ն կիրառելու դեպքում՝ մակերեսը։

# 5. Create a Rectangle class which will inherit from Shape. Implement the constructor and superclass methods to
# correctly calculate the perimeter and the area of the circle.
# Ստեղծել Rectangle կլաս, որը կժառանգի Shape-ից։ Իմպլեմենտ արեք կոնստրուկտորը և Shape-ի երկու մեթոդները ուղղանկյան համար

# 6. Create a Triangle class which will inherit from Shape. Implement the constructor and superclass methods to
# correctly calculate the perimeter and the area of the circle. Note, that you must check whether a triangle with the
# given lengths can exist.
# Ստեղծել Triangle կլաս, որը կժառանգի Shape-ից։ Իմպլեմենտ արեք կոնստրուկտորը և Shape-ի երկու մեթոդները եռանկյան համար։
# Եռանկյուն օբյեկտը ստեղծելուց անպայման ստուգել, թե արդյո՞ք տրված կողմերով եռանկյուն կարող է գոյություն ունենալ։

# 7. a) Create a Vehicle class. The class should have the following instance attributes: name, mileage (defaults to 0),
#    condition, price, max_speed, current_speed and engine_on (defaults to False). It should also have
#    unimplemented methods called start_engine, accelerate (takes a number as an argument), stop.
#    b) Create 2 classes called ElectricVehicle and PetrolVehicle. These classes inherit from the Vehicle class.
#    ElectricVehicle should have the following instance attributes: driving_range, charging_time. PetrolVehicle has the
#    following instance attributes: engine (the volume in litres), transmission, num_of_gears, current_gear. Of course,
#    these classes should call the parent class constructor in their constructor.
#    c) Implement the methods from Vehicle class in each of the child classes accordingly. start_engine should notify us
#    that the engine is on and change the engine_on attribute to True. accelerate method should accelerate the car
#    with the amount of its acceleration attribute and accordingly change the velocity of the car. stop method reduces
#    the speed to 0 and stops the engine. You should also do some checks, e.g. the speed can't be more than max_speed
#    of the car, the car can't start with its engine off etc.
#    d) For the PetrolCar, you should be able to change the transmission gears as well. If the transmission is manual,
#    you should increase the current_gear as the speed increases (current_gear can't be more than the number_of_gears).
#    e) Finally, create some petrol and electric vehicle objects and test your methods.
#
#    a) Ստեղծել Vehicle կլաս։ Կլասը պետք է ունենա հետևյալ instance attribute-ները - name, mileage (նախնական 0 է),
#    condition, price, max_speed, current_speed and engine_on (նախնական False է)։ Կլասը պետք է ունենա նաև երեք
#    չիմպլեմենտացված մեթոդ՝ start_engine, accelerate (ունի մեկ արգումենտ), stop.
#    b) Ստեղծել երկու կլաս՝ ElectricVehicle և PetrolVehicle։ Այս կլասերը ժառանգում են Vehicle—ից։ Էլեկտրական մեքենան
#    պետք է ունենա հետևյալ ատրիբուտները - driving_range, charging_time։ Իսկ վառելիքայինը՝ engine (ծավալը լիտրերով),
#    transmission, num_of_gears, current_gear։ Այս կլասերը պետք է նաև կանչեն Vehicle-ի __init__-ը (super()-ի միջոցով):
#    c) Իմպլեմենտ անել Vehicle-ից ժառանգված բոլոր մեթոդները։ start_engine-ը պետք է զգուշացնի, որ շարժիչը միացված է և
#    engine_on ատրիբուտը դարձնի True. accelerate-ը պետք է բարձրացնի մեքենայի արագությունը, իսկ stop-ը պետք է
#    արագությունն իջեցնի 0-ի և անջատի շարժիչը։ Պետք է նաև կատարել որոշակի վալիդացիա։ Օրինակ՝ արագութոյւնը չի կարող
#    գերազանցել max_speed-ը, մեքենան չի կարող արագանալ, եթե դրա շարժիչը անջատված է և այլն։
#    d) Վառելիքային մեքենայի համար պետք է նաև ներառել որոշակի տրամաբանություն փոխանցման տուփի հետ կապված։ Եթե այն
#    մեխանիկական է, կախված արագությունից պետք է փոխել current_gear-ը (current_gear-ը չի կարող գերազանգել
#    number_of_gears-ը):
#    e) Վերջապես ստեղծել մի քանի էլեկտրական և վառելիքային մեքենա օբյեկտներ և թեստավորել բոլոր մեթոդները։


class Vehicle:
    def __init__(self,name, condition, price, max_speed,current_speed, mileage=0, engine_on=False):
        self.name=name
        self.mileage=mileage
        self.condition=condition
        self.price=price
        self.max_speed=max_speed
        self.current_speed=current_speed
        self.engine_on=engine_on
    def start_engine(self):
        pass
    def accelerate(self,a):
        pass
    def stop(self):
        pass
class ElectricVehicle(Vehicle):
    def __init__(self,name, condition, price, max_speed,current_speed, driving_range, charge_time,mileage=0, engine_on=False):
        super().__init__(name, condition, price, max_speed,current_speed,mileage, engine_on)
        self.driving_range=driving_range
        self.charge_time=charge_time
        if self.current_speed > self.max_speed:
            raise AttributeError('error current speed attributes')
    def start_engine(self):
        print(f'{self.name} engine is ON')
        self.engine_on=True
    def accelerate(self, a):
        if self.engine_on and self.current_speed + a <= self.max_speed:
            self.current_speed += a
    def stop(self):
        self.current_speed=0
        self.engine_on = False
        print(f'{self.name} engine is OFF')

class PetrolVehicle(Vehicle):
    def __init__(self, name, condition, price, max_speed, current_speed,transmission,num_gears,current_gear,mileage=0, engine_on=False):
        super().__init__(name, condition, price, max_speed,current_speed, mileage, engine_on)
        self.transmission = transmission
        self.num_gears = num_gears
        self.current_gear=current_gear
        if self.current_gear>self.num_gears:
            raise AttributeError ('error current gear attributes')
        self.current_gear=int((self.num_gears)/((self.max_speed+2)/(self.current_speed+1)))+1
    def start_engine(self):
        print(f'{self.name} engine is ON')
        self.engine_on=True

    def accelerate(self, a):
        if self.engine_on and self.current_speed+a<=self.max_speed:
            self.current_speed+=a
            if self.transmission=='manual':
                self.current_gear=int((self.num_gears)/((self.max_speed+2)/(self.current_speed+1)))+1
            else:
                self.current_gear='D'

    def stop(self):
        self.current_speed=0
        self.engine_on = False
        print(f'{self.name} engine is OFF')

tesla=ElectricVehicle('tesla','new',25000,240,230,80,12,10)
tesla.start_engine()
tesla.accelerate(5)
#tesla.stop()
tesla.accelerate(30)
print(tesla.current_speed)

bmw=PetrolVehicle('bmw', 'used', 5000, 250, 32, 'manual', 6, 6, 9500, False)
bmw.start_engine()
bmw.accelerate(17)
#bm.stop()
print(bmw.current_speed, bmw.current_gear)
