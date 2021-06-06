from Package import Package
from HashMap import HashMap
from queue import Queue
from Graph import Graph
import sys


class Truck:

    def __init__(self, id):
        SPEED_MPH = 18
        self.id = id
        self.packages = list()
        self.delivery_nodes = set()
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
                        #print(f"New shortest distance: {shortest_distance}")
            nodes_remaining.discard(current_node)
            # print(f"{shortest_distance}")
            total_distance += shortest_distance
            self.delivery_route.put(current_node)

        # Must drive back to the hub
        edges = node_list.get(current_node).edges
        for edge in edges:
            if (edge.to_node == "Western Governors University"):
                total_distance += float(edge.weight)
                break
        self.delivery_route.put("Western Governors University")
        return(total_distance)
