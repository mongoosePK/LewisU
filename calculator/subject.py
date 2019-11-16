from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def update(self) -> None:
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

class ConcreteSubject():
    
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        print("detached an observer")
        self._observers.remove(observer)

    def notify(self):
        print("notifying observer")
        for observer in self._observers:
            observer.update()
