from abc import ABC,abstractmethod
class main(ABC):
    @abstractmethod
    def calculate(self,x,y):
        pass
class sub1(main):
    def calculate(self,x,y):
        print("area of rectangle:",x*y)

class sub2(main):
    def calculate(selfself,x,y):
        print("area of traingle",0.5*x*y)

s1=sub1()
s1.calculate(10,12)
s2=sub2()
s2.calculate(10,20)