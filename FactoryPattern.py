from abc import ABC, abstractmethod


class Toy(ABC):
    def assemble(self):
        print(f'{self.__class__} assemble')

    def pack(self):
        print(f'{self.__class__} pack')


class RCCar(Toy):
    pass


class RCBoat(Toy):
    pass


class ModelCar(Toy):
    pass


class ModelBoat(Toy):
    pass


class ToySimpleFactory:
    def create_toy(self, toy_type):
        toy = None
        if toy_type == 'Car':
            toy = RCCar()
        elif toy_type == 'Boat':
            toy = RCBoat()
        return toy


class ToyStore:

    def __init__(self, factory: ToySimpleFactory):
        self.toy_factory = factory

    def order(self, toy_type) -> Toy:
        toy = self.toy_factory.create_toy(toy_type)
        toy.assemble()
        toy.pack()

        return toy

    def set_factory(self, factory):
        self.toy_factory = factory


# toy_store = ToyStore(ToySimpleFactory())
# toy_store.order('Car')

'''Factory method'''


class ToyFactory(ABC):
    @abstractmethod
    def create_toy(self, toy_type):
        pass

    def order(self, toy_type) -> Toy:
        toy = self.create_toy(toy_type)
        toy.assemble()
        toy.pack()
        return toy


class RCToyFactory(ToyFactory):
    def create_toy(self, toy_type) -> Toy:
        if toy_type == 'Car':
            toy = RCCar()
        elif toy_type == 'Boat':
            toy = RCBoat()
        return toy


class ModelToyFactory(ToyFactory):
    def create_toy(self, toy_type) -> Toy:
        if toy_type == 'Car':
            toy = ModelCar()
        elif toy_type == 'Boat':
            toy = ModelBoat()
        return toy


if __name__ == '__main__':
    toy1 = ModelToyFactory().order('Car')
    toy2 = RCToyFactory().order('Car')
    print(toy1)
    print(toy2)
