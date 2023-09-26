from enum import Enum, auto
from address import ZooAddress


class Family(Enum):
    ELEPHANT = ("elephant", auto())
    RHINO = ("rhino", auto())
    GIRAFFE = ("giraffe", auto())

    def __str__(self):
        return self.value[0]

    @property
    def address(self):
        address = {
            Family.ELEPHANT: ZooAddress(100, "Savanna", "huge area behind the entrance on the left"),
            Family.RHINO: ZooAddress(101, "Savanna", "in front of the penguin pool"),
            Family.GIRAFFE: ZooAddress(102, "Savanna", "behind the penguin pool"),
        }
        return address[self]
