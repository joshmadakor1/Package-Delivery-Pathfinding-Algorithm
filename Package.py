import csv


class Package:

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

    def __str__(self):
        if "DELIVERED" not in self.status:
            return f"{self.id}, {self.status}IN TRANSIT, {self.address_name}, {self.delivery_address}, {self.deadline}, {self.delivery_city}, {self.delivery_zip}, {self.weight}"
        else:
            return f"{self.id}, {self.status}, {self.address_name}, {self.delivery_address}, {self.deadline}, {self.delivery_city}, {self.delivery_zip}, {self.weight}"

    # Updates a package based on supplied parameters
    def update(self, new_delivery_address, new_address_name, new_city, new_zip, new_status):
        self.delivery_address = new_delivery_address
        self.address_name = new_address_name
        self.delivery_city = new_city
        self.delivery_zip = new_zip
        self.status = new_status

    # Sets the status of a package
    def set_status(self, status):
        self.status = status

    # Returns the status of a package
    def get_status(self):
        return self.status
