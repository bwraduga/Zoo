from zoo import Zoo
from giraffe import Giraffe
from elephant import Elephant
from rhino import Rhino


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, value=None):
        if not hasattr(self, "initialized"):
            self.value = value
            self.initialized = True


class ZooFactory:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ZooFactory, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def build(self, name):
        result = Zoo(name)
        my_list = {}

        if name == "San Francisco Zoo":
            my_list = {Elephant("Masha", 1001),
                       Elephant("Dasha", 2002),
                       Elephant("Pasha", 500),
                       Rhino("Dima", 2002),
                       Giraffe("Mark", 1500)}
        elif name == "Oakland Zoo":
            my_list = {Elephant("Igor", 2000),
                       Elephant("Ilya", 3000),
                       Rhino("Sara", 600),
                       Rhino("Ian", 1200)}
        elif name == "San Diego Zoo":
            my_list = {Elephant("Bella", 1379),
                       Elephant("Max", 2568),
                       Elephant("Charlie", 3110),
                       Rhino("Daisy", 1923),
                       Rhino("Buddy", 3487),
                       Rhino("Lucy", 2761),
                       Rhino("Molly", 1532),
                       Giraffe("Rocky", 3999),
                       Giraffe("Coco", 2145),
                       Giraffe("Oliver", 3300),
                       Giraffe("Luna", 3682)}

        result.dictionary.add_list_to_inventory(my_list)
        return result
