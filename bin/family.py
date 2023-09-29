from enum import Enum, auto
from address import AddressLeaf


class Family(Enum):
    ELEPHANT = ("elephant", auto())
    RHINO = ("rhino", auto())
    GIRAFFE = ("giraffe", auto())

    def __str__(self):
        return self.value[0]

    @property
    def address(self):
#        address = {
#            Family.ELEPHANT: AddressLeaf(100, "Savanna", "huge area behind the entrance on the left"),
#            Family.RHINO: ZooAddressTreeNode(101, "Savanna", "in front of the penguin pool"),
#            Family.GIRAFFE: ZooAddressTreeNode(102, "Savanna", "behind the penguin pool"),
#        }
        return address[self]
