
class ZooAddressTreeNode:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.children = []

    def __str__(self): # переписать вывод адреса ( по дереву )
        return f"Zoo Address: {self.name}, {self.desc}"

    def add_child(self, child_node):
        self.children.append(child_node)
