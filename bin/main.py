from ZooFactory import ZooFactory
from zoo import Zoo


san_francisco_zoo = ZooFactory().build("San Francisco Zoo")


# wrong - same for all zoos
print('\n', ">>GUIDE san_francisco_zoo<<")
print(san_francisco_zoo.dictionary)


# wrong - same for all zoos
print('\n', ">>FAMILIES<<")
print('\n'.join(map(str, san_francisco_zoo.dictionary.get_families())))


print('\n', ">>LIST ", san_francisco_zoo.name)
print(san_francisco_zoo.get_inventory())



