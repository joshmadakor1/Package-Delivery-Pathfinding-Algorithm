from time import time
from queue import Queue
from datetime import timedelta
import sys


class Truck:

    def __init__(self, id):
        self.SPEED_MPH = 18
        self.id = id
        self.packages = list()
        self.delivery_nodes = set()

        # delivery_route (example): ['Western Governors University', '10.9']
        self.delivery_route = Queue()
        self.package_count = 0

    def __str__(self):
        return f"Truck{self.id} has {self.package_count} packages remaining."

    def get_packages(self):
        return self.packages

    def add_package(self, package):
        self.packages.append(package)
        self.package_count += 1
        self.delivery_nodes.add(package.address_name)

    def remove_package(self, package):
        self.packages.remove(package)
        self.package_count -= 1
        self.delivery_nodes.discard(package.address_name)

    def calculate_best_delivery_route(self, node_list):
        current_node = "Western Governors University"
        self.delivery_route = Queue()
        next_node_for_delivery_route = None
        total_distance = 0
        nodes_remaining = set()
        nodes_remaining = self.delivery_nodes.copy()
        while (len(nodes_remaining) > 0):
            edges = node_list.get(current_node).edges
            shortest_distance = sys.maxsize

            for edge in edges:
                if edge.to_node in nodes_remaining:
                    if float(edge.weight) < shortest_distance:
                        shortest_distance = float(edge.weight)
                        current_node = edge.to_node
                        next_node_for_delivery_route = [
                            edge.to_node, edge.weight]

                        # print(f"New shortest distance: {shortest_distance}")
            nodes_remaining.discard(current_node)
            # print(f"{shortest_distance}")
            total_distance += shortest_distance
            self.delivery_route.put(next_node_for_delivery_route)

        # Must drive back to the hub
        edges = node_list.get(current_node).edges
        for edge in edges:
            if (edge.to_node == "Western Governors University"):
                total_distance += float(edge.weight)
                next_node_for_delivery_route = [edge.to_node, edge.weight]
                break
        self.delivery_route.put(next_node_for_delivery_route)
        return(total_distance)

    def get_packages_currently_being_delivered(self, delivery_location_name):
        current_packages = list()
        for package in self.packages:
            if (package.address_name == delivery_location_name):
                current_packages.append(package.id)
        return current_packages

    # O(N)
    # Args: Departure Time
    # Returns: [return_time, drive_time, drive_distance]
    def deliver_packages(self, departure_time):
        return_time = None
        drive_distance = 0
        print(f"Departure:    {departure_time}")

        while (self.delivery_route.qsize() > 0):
            # next_delivery entries contain an array as folows:
            # next_delivery[0] = 'Western Governors University'
            # next_delivery[1] = '10.9'
            next_delivery = self.delivery_route.get()

            # next_delivery entries contain an array as folows:
            # next_delivery[0] = 'Western Governors University'
            # next_delivery[1] = '10.9'
            # get current packages being delivered
            current_packages = self.get_packages_currently_being_delivered(
                next_delivery[0])

            # next_delivery entries contain an array as folows:
            # next_delivery[0] = 'Western Governors University'
            # next_delivery[1] = '10.9'
            # calculate running distnce
            drive_distance += float(next_delivery[1])

            # Calculate drive time
            drive_time_in_hours = drive_distance / self.SPEED_MPH

            # Calculate current time
            current_time = departure_time + timedelta(hours=drive_time_in_hours)
            #print(f"Package ({current_packages}) delivered")
            #print(f"Current time: {current_time}")

        #nine_hours_from_now = datetime.now() + timedelta(hours=9)
        return_time = departure_time + timedelta(hours=drive_time_in_hours)
        print(f"({self.id}) Departure: {departure_time}")
        print(f"({self.id}) Return:    {return_time}")
        print(f"({self.id}) Distance:  {round(float(drive_distance),2)} miles")
        print(f"({self.id}) Time:      {round(float(drive_time_in_hours),2)} hours")
        print("")
        return([return_time, drive_time_in_hours, drive_distance])
