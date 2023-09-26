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
        san_francisco_animals = {Elephant("Masha", 1001),
                       Elephant("Dasha", 2002),
                       Elephant("Pasha", 500),
                       Rhino("Dima", 2002),
                       Giraffe("Mark", 1500)}
        oakland_animals = {Elephant("Igor", 2000),
                       Elephant("Ilya", 3000),
                       Rhino("Sara", 600),
                       Rhino("Ian", 1200)}
        san_diego_animals = {Elephant("Bella", 1379),
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

        zoo_animals_mapping = {
            "San Francisco Zoo": san_francisco_animals,
            "Oakland Zoo": oakland_animals,
            "San Diego Zoo": san_diego_animals,
        }

        if name not in zoo_animals_mapping:
            raise ValueError(f"Unknown zoo name: {name}")

        result.dictionary.add_list_to_inventory(zoo_animals_mapping[name])

        return result
