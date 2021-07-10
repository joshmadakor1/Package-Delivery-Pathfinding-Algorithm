# Nnamdi Joshua Madakor, ID: 000214961
import csv


class Package:

    # Time-complexity: O(7) -> O(1)
    # Default Constructor
    def __init__(self, id, address_name, delivery_address, deadline, delivery_city, delivery_zip, weight, status):
        self.id = id
        self.address_name = address_name
        self.delivery_address = delivery_address
        self.deadline = deadline
        self.delivery_city = delivery_city
        self.delivery_zip = delivery_zip
        self.weight = weight
        self.status = status

    # Time-complexity: O(1)
    # Returns information about the package. If the package has not been delivered,
    #   returnt he status as "IN TRANSIT"
    def __str__(self):
        # if "DELIVERED" not in self.status:
        #    return f"{self.id}, {self.status}IN TRANSIT, {self.address_name}, {self.delivery_address}, {self.deadline}, {self.delivery_city}, {self.delivery_zip}, {self.weight}"
        # else:
        return f"{self.id}, {self.status}, {self.address_name}, {self.delivery_address}, {self.deadline}, {self.delivery_city}, {self.delivery_zip}, {self.weight}"

    # Time-complexity: O(5) -> O(1)
    # Updates a package based on supplied parameters
    def update(self, new_delivery_address, new_address_name, new_city, new_zip, new_status):
        self.delivery_address = new_delivery_address
        self.address_name = new_address_name
        self.delivery_city = new_city
        self.delivery_zip = new_zip
        self.status = new_status

    # Time-complexity: O(1)
    # Sets the status of a package
    def set_status(self, status):
        self.status = status

    # Time-complexity: O(1)
    # Returns the status of a package
    def get_status(self):
        return self.status

    # Time-complexity: O(1)
    # Returns the id of a package
    def get_id(self):
        return self.id
