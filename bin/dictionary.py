from address import IAddress
from family import Family


class Dictionary:
    def __init__(self):
        self.inventory = {}
        self.addresses = IAddress("zoo", "")
        self.address_book = {}

    def __str__(self):
        return '\n'.join(map(str, self.get()))

    @staticmethod
    def get():# для каждой family должен возвращать адрес / не работает
        result = []
        for member in Family:
           # result.append(f"{member}: {member.address}")
            result.append(f"{member}:")
        return result

    @staticmethod
    def get_families(): #не работает ( должен возвращать список семейств данного zoo
        result = []
        for member in Family:
            result.append(f"{member}")
        return result

    def add_to_inventory(self, member): # add one animal
        if member is not None:
            self.inventory.setdefault(member.my_family(), set()).add(member)

    def add_list_to_inventory(self, member_list): # add set of animals
        for member in member_list:
            self.add_to_inventory(member)

   # def add_to_address(self, address_node):
    #    self.addresses.add_child(address_node)

# TODO fix
    # def add_resident(self, address_node, resident_name):
        # Assuming each resident name is unique
    #     self.address_book[resident_name] = address_node
    #    address_node.resident = resident_name

    def get_address_by_resident_name(self, resident_name):
        node = self.address_book.get(resident_name)
        if node:
            return node
        return None
