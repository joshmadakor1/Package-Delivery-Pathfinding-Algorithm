import csv
from Package import Package
from HashMap import HashMap


class PackageHandler:

    # Default Constructor
    # This will build a hashmap containing all the package data
    def __init__(self):
        self.TOTAL_PACKAGES = 40
        self.packages = {}
        self.packages_hash_table = HashMap()
        self.build_packages_table_from_csv()

    def __iter__(self):
        return iter([package for id, package in self.packages.items()])

    # Method to get size
    def __len__(self):
        return len(self.packages)

    # Method to insert item
    def insert(self, item):
        self.packages[item.id] = item

    # O(N)
    def build_packages_table_from_csv(self):
        location_address_to_names = HashMap()

        with open("./data/distance_names.csv") as file:
            names_reader = csv.reader(file)
            raw_distance_names = list(names_reader)
            for entry in raw_distance_names:
                # Example
                # entry[1] -> 'Western Governors University'
                # entry[2] ->'4001 South 700 East'
                location_address_to_names.add(entry[2], entry[1])

        with open("./data/packages.csv") as file:
            packages_reader = csv.reader(file)
            raw_package_data = list(packages_reader)

        for entry in raw_package_data:
            if len(entry) > 1:
                self.insert(Package(id=entry[0], address_name=location_address_to_names.get(entry[1]), delivery_address=entry[1], deadline=entry[5],
                                    delivery_city=entry[2], delivery_zip=entry[4], weight=entry[6], status=entry[7]))
                self.packages_hash_table.add(entry[0], Package(id=entry[0], address_name=location_address_to_names.get(entry[1]), delivery_address=entry[1], deadline=entry[5],
                                                               delivery_city=entry[2], delivery_zip=entry[4], weight=entry[6], status=entry[7]))

    # O(1)
    def get_package_by_id(self, id):
        return self.packages_hash_table.get(id)

    # O(N)
    # Returns a collection of packages
    def get_packages_by_address(self, address):
        packages = list()
        for id in range(1, self.TOTAL_PACKAGES + 1):
            package = self.get_package_by_id(str(id))
            if (package.delivery_address == address):
                packages.append(package)
        return packages

    # O(N)
    def get_packages_by_city(self, city):
        packages = list()
        for id in range(1, self.TOTAL_PACKAGES + 1):
            package = self.get_package_by_id(str(id))
            if (package.delivery_city == city):
                packages.append(package)
        return packages

    # O(N)
    def get_packages_by_deadline(self, deadline):
        packages = list()
        for id in range(1, self.TOTAL_PACKAGES + 1):
            package = self.get_package_by_id(str(id))
            if (package.deadline == deadline):
                packages.append(package)
        return packages

    # O(N)
    def get_packages_by_zip(self, zip):
        packages = list()
        for id in range(1, self.TOTAL_PACKAGES + 1):
            package = self.get_package_by_id(str(id))
            if (package.delivery_zip == zip):
                packages.append(package)
        return packages

    # O(N)
    def get_packages_by_weight(self, weight):
        packages = list()
        for id in range(1, self.TOTAL_PACKAGES + 1):
            package = self.get_package_by_id(str(id))
            if (package.weight == weight):
                packages.append(package)
        return packages

    # O(N)
    def get_packages_by_status(self, status):
        packages = list()
        for id in range(1, self.TOTAL_PACKAGES + 1):
            package = self.get_package_by_id(str(id))
            if (package.status == status):
                packages.append(package)
        return packages
