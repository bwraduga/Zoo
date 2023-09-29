
class IAddress:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.parent = None

    def get_full_address(self):
        if self.parent:
            return self.parent.get_full_address() + " -> " + self.name + ': ' + self.desc
        else:
            return self.name + ': ' + self.desc

    def __str__(self):
        return self.get_full_address()

    def get_type(self):
        pass


class AddressNode(IAddress):

    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parent = self

    def __init__(self, name, desc):
        super().__init__(name, desc)
        self.children = []

    def __str__(self):
        return super().__str__()

    def get_type(self):
        return "node"

class AddressLeaf(IAddress):
    def __init__(self, name, desc, resident=None):
        super().__init__(name, desc)
        self.resident = resident

    def __str__(self):
        address_str = super().__str__()
        return f"{address_str}, Resident: {self.resident}"

    def get_type(self):
        return "leaf"
