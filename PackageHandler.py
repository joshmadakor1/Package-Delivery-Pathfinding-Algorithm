import csv
from Package import Package


class PackageHandler:

    # Default Constructor
    # This will build a hashmap containing all the package data
    def __init__(self):
        self.packages = {}
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
        with open("./data/packages.csv") as file:
            packages_reader = csv.reader(file)
            raw_package_data = list(packages_reader)

        for entry in raw_package_data:
            if len(entry) > 1:
                self.insert(Package(id=entry[0], delivery_address=entry[1], deadline=entry[5],
                                    delivery_city=entry[2], delivery_zip=entry[4], weight=entry[6], status=entry[7]))

    # O(1)
    def get_package_by_id(self, id):
        package = self.packages.get(id)
        if package:
            # The specified package id exists
            return self.packages[id]
        else:
            # The specified package id does not exist
            return None

    # O(N)
    # Returns a collection of packages
    def get_packages_by_address(self, address):
        packages = list()
        for id, package in self.packages.items():
            if package.delivery_address == address:
                packages.append(package)
        return packages

    # O(N)
    def get_packages_by_city(self, city):
        packages = list()
        for id, package in self.packages.items():
            if package.delivery_city == city:
                packages.append(package)
        return packages

    # O(N)
    def get_packages_by_deadline(self, deadline):
        packages = list()
        for id, package in self.packages.items():
            if package.deadline == deadline:
                packages.append(package)
        return packages

    # O(N)
    def get_packages_by_zip(self, zip):
        packages = list()
        for id, package in self.packages.items():
            if package.delivery_zip == zip:
                packages.append(package)
        return packages

    # O(N)
    def get_packages_by_weight(self, weight):
        packages = list()
        for id, package in self.packages.items():
            if package.weight == weight:
                packages.append(package)
        return packages

    # O(N)
    def get_packages_by_status(self, status):
        packages = list()
        for id, package in self.packages.items():
            if package.status == status:
                packages.append(package)
        return packages
