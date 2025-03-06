'''
from abc import ABC,abstractmethod

class Vehical(ABC):

    @abstractmethod
    def speed(self,speed):
        pass

    def show(self):
        print("this is vehical class")

class Bike(Vehical):

    def show(self):
        print("this is bike class")
    def speed(self,speed):
        print("i am bike. my max speed is",speed)

class Car(Vehical):

    def show(self):
        print("this is car class")
    def speed(self,speed):
        print("i am cart. my max speed is",speed)

b1=Bike()
b1.show()
b1.speed(140)

c1=Car()
c1.show()
c1.speed(240)
'''


from abc import ABC,abstractmethod

class Rbi(ABC):

    
    @abstractmethod
    def ROI(self,intrest):
        pass

    def show(self):
        print("this is Rbi class")

class SBI(Rbi):
    def show(self):
        print("this is SBI class")
    def ROI(self,intrest):
        print("i am SBI.my max intrest is",intrest)

s1=SBI()
s1.show()
s1.ROI(10)
