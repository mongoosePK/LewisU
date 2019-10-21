from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def update(self):
        '''callback to be called when subject changes state'''
        pass

class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        '''used by observers to register for state changes'''
        pass

    def detach(self, observer:Observer)->None:
        '''used by observers to de-register'''
        pass

    def notify(self) -> None:
        
        '''must be overriden to notify observers'''
        pass

class ConcreteSubject(Subject):
    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)