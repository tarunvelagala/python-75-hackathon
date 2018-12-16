from abc import *

class absclass():
    @abstractmethod
    def car(self):
        raise NotImplementedError
    def speed(self):
        print('Its speed is 460kmph')

class Ferrari(absclass):
    def car(self):
        print('Its a Ferrari car')
    def speed(self):
        print("Its speed is 360kmph")

class Bugati(absclass):
    def car(self):
        print('Its a bugati')
    def speed(self):
        print("Its speed is 400kmph")

obj1 = Ferrari()
obj1.car()
obj1.speed()

obj2 = Bugati()
obj2.car()
obj2.speed()


