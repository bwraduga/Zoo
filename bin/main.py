from ZooFactory import ZooFactory
from family import Family
from zoo import Zoo


sf_zoo = ZooFactory().build("San Francisco Zoo")
oa_zoo = ZooFactory().build("Oakland Zoo")



print(sf_zoo.dictionary.get_address_by_resident_name(Family.ELEPHANT))

print('\n', ">>GUIDE", sf_zoo.name)
print(sf_zoo.get_addresses())


print('\n', ">>GUIDE", oa_zoo.name)
print(oa_zoo.get_addresses())

print('\n', ">>LIST ", sf_zoo.name)
print(sf_zoo.get_inventory())



