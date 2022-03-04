from abc import ABC


class Leaf():
    def __init__(self, position):
        self.position = position

    def showDetails(self):
        print('\t', end='')
        print(self.position)


class Composite():
    def __init__(self, position):
        self.position = position
        self.children: [Leaf] = []

    def add(self, leaf):
        self.children.append(leaf)

    def remove(self, leaf):
        self.children.remove(leaf)

    def get_children(self):
        return self.children

    def showDetails(self):
        print(self.position)
        for child in self.children:
            print('\t', end='')
            child.showDetails()


developer1 = Leaf('Developer 1')
developer2 = Leaf('Developer 2')
developer3 = Leaf('Developer 3')
developer4 = Leaf('Developer 4')

manager1 = Composite('Manager1')
manager1.add(developer1)
manager1.add(developer2)

manager2 = Composite('Manager2')
manager2.add(developer3)
manager2.add(developer4)

general_manager = Composite('General manager')
general_manager.add(manager1)
general_manager.add(manager2)

# manager1.showDetails()
# manager2.showDetails()
general_manager.showDetails()