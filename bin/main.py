from ZooFactory import ZooFactory
from zoo import Zoo


my_zoo = ZooFactory().build("San Francisco Zoo")


# wrong - same for all zoos
print('\n', ">>GUIDE ", my_zoo.name)
print(my_zoo.dictionary)


print('\n', ">>GUIDE 2 ", my_zoo.name)
print(my_zoo.get_addresses())


# wrong - same for all zoos
print('\n', ">>FAMILIES<<")
print('\n'.join(map(str, my_zoo.dictionary.get_families())))


print('\n', ">>LIST ", my_zoo.name)
print(my_zoo.get_inventory())



