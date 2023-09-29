from dictionary import Dictionary


class Zoo:
    def __init__(self, name):
        self.dictionary = Dictionary()
        self.name = name

    def get_catalog(self):
        return self.dictionary.get()

    def get_inventory(self):
        result = []
        for key, values in self.dictionary.inventory.items():
            result.append(f"{key}: {', '.join(map(str, values))}")
        return '\n'.join(result)

    def get_addresses(self, node=None, level=0):

        if node is None:
            node = self.dictionary.addresses

        result = "\t" * level + node.name + ': '+ node.desc + "\n"

        if node.get_type() == "node":
            for child in node.children:
                result += self.get_addresses(child, level + 1)
        return result
