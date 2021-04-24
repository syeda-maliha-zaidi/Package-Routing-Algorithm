import csv
from package import Package
from hash_table import HashTable

address_data_path = "data/address_data.csv"
distance_data_path = "data/distance_data.csv"
packages_data_path = "data/packages_data.csv"

# Loads address data from csv into python dictionary (address_dict[address_location] = [address_id, address_name])
# Complexity is O(n)
def load_address_data():
    with open(address_data_path, 'r') as address_data_file:
        address_dict = {}
        for address_data_row in csv.reader(address_data_file, delimiter=','):

            address_id = address_data_row[0]
            address_name = address_data_row[1]
            address_location = address_data_row[2]

            address_dict[address_location] = [address_id, address_name]

        return address_dict        


# Loads distance data from csv into python list using list comprehension
# Complexity is O(n)
def load_distance_data():
    with open(distance_data_path, 'r') as distance_data_file:
        return list(csv.reader(distance_data_file, delimiter=','))


# Complexity is O(n)
def load_package_data():
    with open(packages_data_path, 'r') as packages_data_file:
        package_data_list = list(csv.reader(packages_data_file, delimiter=','))

        package_hash_table = HashTable(len(package_data_list))

        for package_data_row in package_data_list:
            package = Package( package_data_row )
            package_hash_table.insert(package)
        return package_hash_table