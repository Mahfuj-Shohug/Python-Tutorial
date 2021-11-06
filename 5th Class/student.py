#Abstraction
#Priroty
#need to import laibrary
from abc import ABC, abstractmethod, abstractproperty

class Student(ABC):
    @abstractmethod
    #to define this abstractmethod for call student class must be genarate those method 
    def getName(self):
        pass
    @abstractmethod
    def setName(self, name):
        pass
    @abstractmethod
    def getDept(self):
        pass
    @abstractmethod
    def setDept(self, name):
        pass