from family import Family


class Dictionary:
    def __init__(self):
        self.inventory = {}

    def __str__(self):
        return '\n'.join(map(str, self.get()))

    @staticmethod
    def get():
        result = []
        for member in Family:
            result.append(f"{member}: {member.address}")
        return result

    @staticmethod
    def get_families():
        result = []
        for member in Family:
            result.append(f"{member}")
        return result

    def add_to_inventory(self, member):
        if member is not None:
            self.inventory.setdefault(member.my_family(), set()).add(member)

    def add_list_to_inventory(self, member_list):
        for member in member_list:
            self.add_to_inventory(member)


# INVENTORY MAP KEY FAMILY - PROPERTY
# список zoo_address принадлежит zoo, в каждый адрес поселяем жителей(family)
# сделать инит для секций и их описаний
