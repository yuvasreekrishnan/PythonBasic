from abc import ABC, abstractmethod 

class mainAbstractClass(ABC):
    @abstractmethod
    def perform_action(self):
        pass

    @abstractmethod
    def another_action(self):
        pass


class concreteClass(mainAbstractClass):
    def perform_action(self):
        print("Performing action in concrete class")

    def another_action(self):
        print("Another action in concrete class")

data = concreteClass()
data.perform_action()
data.another_action()