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
