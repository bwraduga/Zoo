from address import IAddress, AddressNode, AddressLeaf
from family import Family
from zoo import Zoo
from giraffe import Giraffe
from elephant import Elephant
from rhino import Rhino

#todo class DB


class ZooFactory:
    _instance = None
    # inventory
    san_francisco_animals = {Elephant("Masha", 1001),
                             Elephant("Dasha", 2002),
                             Elephant("Pasha", 500),
                             Rhino("Dima", 2002),
                             Giraffe("Mark", 1500)}
    oakland_animals = {Elephant("Igor", 2000),
                       Elephant("Ilya", 3000),
                       Rhino("Sara", 600),
                       Rhino("Ian", 1200)}
    san_diego_animals = {Elephant("Bella", 1379),
                         Elephant("Max", 2568),
                         Elephant("Charlie", 3110),
                         Rhino("Daisy", 1923),
                         Rhino("Buddy", 3487),
                         Rhino("Lucy", 2761),
                         Rhino("Molly", 1532),
                         Giraffe("Rocky", 3999),
                         Giraffe("Coco", 2145),
                         Giraffe("Oliver", 3300),
                         Giraffe("Luna", 3682)}

    zoo_animals_mapping = {
        "San Francisco Zoo": san_francisco_animals,
        "Oakland Zoo": oakland_animals,
        "San Diego Zoo": san_diego_animals,
    }

    zoo_residents_mapping = {}

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ZooFactory, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def build(self, name):

        result = Zoo(name)

        # Addresses
        result.dictionary.addresses = self.build_addresses(name)

        result.dictionary.address_book = self.zoo_residents_mapping

        # inventory
        if name not in self.zoo_animals_mapping:
            raise ValueError(f"Unknown zoo name: {name}")

        result.dictionary.add_list_to_inventory(self.zoo_animals_mapping[name])

        return result

    def build_addresses(self, name):

        sf_zoo_residents_mapping = {}
        oa_zoo_residents_mapping = {}
        sd_zoo_residents_mapping = {}


        san_francisco_addresses = AddressNode("zoo", "San Francisco Zoo")
        sf_safari = AddressNode("Safari section", "on the left from entrance")
        sf_arctic = AddressNode("Arctic section", "on the right from entrance")
        sf_elephant_place = AddressLeaf("Place 1", "A", Family.ELEPHANT)
        sf_zoo_residents_mapping[Family.ELEPHANT] = sf_elephant_place
        sf_rhino_place = AddressLeaf("Place2", "B", Family.RHINO)
        sf_zoo_residents_mapping[Family.RHINO] = sf_rhino_place
        sf_giraffe_place = AddressLeaf("Place 3", "C", Family.GIRAFFE)
        sf_zoo_residents_mapping[Family.GIRAFFE] = sf_giraffe_place

        sf_safari.add_child(sf_elephant_place)
        sf_safari.add_child(sf_rhino_place)
        sf_safari.add_child(sf_giraffe_place)

        san_francisco_addresses.add_child(sf_safari)
        san_francisco_addresses.add_child(sf_arctic)

        # Oakland
        oakland_addresses = AddressNode("zoo", "Oakland Zoo")
        oa_safari = AddressNode("Safari section OA", "on the left from entrance")
        oa_arctic = AddressNode("Arctic section OA", "on the right from entrance")
        oa_elephant_place = AddressLeaf("Place 1 OA", "A", Family.ELEPHANT)
        oa_zoo_residents_mapping[Family.ELEPHANT] = oa_elephant_place
        oa_rhino_place = AddressLeaf("Place 2 OA", "B", Family.RHINO)
        oa_zoo_residents_mapping[Family.RHINO] = oa_rhino_place

        oa_safari.add_child(oa_elephant_place)
        oa_safari.add_child(oa_rhino_place)

        oakland_addresses.add_child(oa_safari)
        oakland_addresses.add_child(oa_arctic)

        # San Diego
        san_diego_addresses = AddressNode("zoo", "San Diego Zoo")
        san_diego_safari = AddressNode("Safari section SD", "on the left from entrance")
        san_diego_elephant_place = AddressLeaf("Place 1 SD", "A", Family.ELEPHANT)
        sd_zoo_residents_mapping[Family.ELEPHANT] = san_diego_elephant_place
        san_diego_rhino_place = AddressLeaf("Place 2 SD", "B", Family.RHINO)
        sd_zoo_residents_mapping[Family.RHINO] = san_diego_rhino_place
        san_diego_giraffe_place = AddressLeaf("Place 3 SD", "C", Family.GIRAFFE)
        sd_zoo_residents_mapping[Family.GIRAFFE] = san_diego_giraffe_place

        san_diego_safari.add_child(san_diego_elephant_place)
        san_diego_safari.add_child(san_diego_rhino_place)
        san_diego_safari.add_child(san_diego_giraffe_place)

        san_diego_addresses.add_child(san_diego_safari)

        # map for fast search the family(resident) address
        if name == "San Francisco Zoo":
            self.zoo_residents_mapping = sf_zoo_residents_mapping
        if name == "Oakland Zoo":
            self.zoo_residents_mapping = oa_zoo_residents_mapping
        if name == "San Diego Zoo":
            self.zoo_residents_mapping = sd_zoo_residents_mapping

        # fill zoo addresses tree
        zoo_addresses_mapping = {
            "San Francisco Zoo": san_francisco_addresses,
            "Oakland Zoo": oakland_addresses,
            "San Diego Zoo": san_diego_addresses,
        }

        if name not in zoo_addresses_mapping:
            raise ValueError(f"Unknown zoo name: {name}")

        result = zoo_addresses_mapping[name]
        return result
