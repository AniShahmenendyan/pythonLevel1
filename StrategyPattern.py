import abc


class SoundBehaviourInterface(abc.ABC):
    @abc.abstractmethod
    def sound(self):
        pass


class BarkableBehaviour(SoundBehaviourInterface):
    def sound(self):
        print('I\'m barking')


class NoSoundBehaviour(SoundBehaviourInterface):
    def sound(self):
        print('No sound')


class MoveBehaviourInterface(abc.ABC):
    @abc.abstractmethod
    def move(self):
        pass


class WalkinBehaviour(MoveBehaviourInterface):

    def move(self):
        print('I am walking')


class NoWalkingBehaviour(MoveBehaviourInterface):
    def move(self):
        print('I can\'t walk')


class Dog:
    _move_behaviour = None
    _sound_behaviour = None

    def sound(self):
        self._sound_behaviour.sound()

    def move(self):
        self._move_behaviour.move()

    def set_sound_behaviour(self, behaviour):
        self._sound_behaviour = behaviour


class Doberman(Dog):

    def __init__(self):
        self._move_behaviour = WalkinBehaviour()
        self._sound_behaviour = BarkableBehaviour()


class GermanShepard(Dog):
    def __init__(self):
        self._move_behaviour = WalkinBehaviour()
        self._sound_behaviour = BarkableBehaviour()


class ToyDog(Dog):
    def __init__(self):
        self._move_behaviour = NoWalkingBehaviour()
        self._sound_behaviour = NoSoundBehaviour()


class ToyDogWithBattery(Dog):
    def __init__(self):
        self._move_behaviour = NoWalkingBehaviour()
        self._sound_behaviour = BarkableBehaviour()


# dog1 = Doberman()
# dog1.sound()
# dog1.move()
# dog2 = ToyDog()
# dog2.sound()
# dog2.move()
# dog2.set_sound_behaviour(BarkableBehaviour())
# dog2.sound()

# dog3 = ToyDogWithBattery()
# dog3.sound()
# dog3.move()


