class Radio:
    def play(self):
        print('playing')


class RadioMixin:
    def __init__(self, *args, **kwargs):
        self.radio = Radio()
        print('mixin init')
        super().__init__(*args, **kwargs)

    def radio_play(self):
        Radio().play()


class Vehicle:

    def __init__(self, position):
        print('Vehicle init')
        self.position = position

    def travel(self, destination):
        print(f'Traveling from {self.position} to {destination}')


class Car(RadioMixin, Vehicle):
    pass


class Boat(Vehicle):
    pass


class Train(Vehicle):
    pass


car = Car('Yerevan')
print(Car.mro())
car.travel('Gyumri')
car.radio_play()

# boat = Boat('Sevan')
# boat.travel('')
