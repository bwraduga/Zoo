from abc import ABC, abstractmethod


class BaseAnimal(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return self.my_name_is()

    def my_name_is(self):
        return f"I am {self.my_family()} {self.name} and my weight is {self.weight}"

    @abstractmethod
    def my_family(self):
        pass
