from abc import ABC


class Bird(ABC):
    def sound(self):
        print('Tsiv-Tsiv')

    def fly(self):
        print('I am flying')


class Parrot(Bird):
    pass


class Duck:
    def duck_sound(self):
        return 'airk airK'


class BirdAdapter(Duck):
    def sound(self):
        sound = self.duck_sound()
        print(sound[::-1])

    def fly(self):
        print('I can\'t flying')


parrot = Parrot()
parrot.sound()
parrot.fly()

duck = BirdAdapter()
duck.sound()
duck.fly()

print(duck.duck_sound())
