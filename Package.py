import csv


class Package:

    # Default Constructor
    def __init__(self, id, delivery_address, deadline, delivery_city, delivery_zip, weight, status):
        self.id = id
        self.delivery_address = delivery_address
        self.deadline = deadline
        self.delivery_city = delivery_city
        self.delivery_zip = delivery_zip
        self.weight = weight
        self.status = status

    def __str__(self):
        return f"{self.id}, {self.delivery_address}, {self.deadline}, {self.delivery_city}, {self.delivery_zip}, {self.weight}, {self.status}"

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status
