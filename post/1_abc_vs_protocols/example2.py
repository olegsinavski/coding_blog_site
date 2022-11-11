
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self, food) -> float:
        pass

    @abstractmethod
    def sleep(self, hours) -> float:
        pass


from zope.interface import Interface

class Animal(Interface):
    def eat(self, food) -> float:
        pass

    def sleep(self, hours) -> float:
        pass



from typing import Protocol

class Animal(Protocol):
    def eat(self, food) -> float:
        pass

    def sleep(self, hours) -> float:
        pass
