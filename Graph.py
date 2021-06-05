import csv
from HashMap import HashMap
from Node import Node
from Edge import Edge


class Graph:

    # Default Constructor
    def __init__(self):
        self.location_names = [None] * 27
        self.raw_distance_data = []
        self.node_list = HashMap()
        #self.adjacency_list = HashMap()

    # Populates the location name data
    # O(N); where N = number of rows of location name data

    def initialize_location_name_data(self):

        with open("./data/distance_names.csv") as file:
            names_reader = csv.reader(file)
            raw_distance_names = list(names_reader)
            # print(raw_distance_names)
            i = 0
        for entry in raw_distance_names:
            self.location_names[i] = entry
            i += 1

    # Populates the location distance data
    # O(N); where N = number of rows of location distance data
    def initialize_location_distance_data(self):
        with open("./data/distance_data.csv") as file:
            reader = csv.reader(file)
            self.raw_distance_data = list(reader)

    # Builds the hashmap which contains all the nodes (Addresses)
    # O(V); where V = number of verticies
    # def initialize_nodes_hashmap(self):
    #    for name in self.location_names:
    #        # name[1] -> Ex. "Western Governors University"
    #        # name[2] -> Ex. "4001 South 700 East"
    #        self.add_node(name[1], Node(name[1], name[2]))

    # Builds the hashmap which contains all the edges
    # O(V^2); where V = number of verticies
    def initialize_nodes_hashmap(self):
        for i in range(len(self.raw_distance_data)):
            for j in range(len(self.raw_distance_data)):

                # Add distance entries horizontally
                if j < i:
                    self.add_node(
                        from_node=self.location_names[i][1], to_node=self.location_names[j][1], weight=self.raw_distance_data[i][j])
                # Add distance entries vertically, to account for 2 way mapping
                elif j > i:
                    self.add_node(
                        from_node=self.location_names[i][1], to_node=self.location_names[j][1], weight=self.raw_distance_data[j][i])
                    # list.append([self.location_names[j][1], self.raw_distance_data[j][i]])

    # O(1)
    # def add_node(self, name, address):
    #    self.node_list.add(name, Node(name, address))

    # O(1)
    def add_node(self, from_node, to_node, weight):

        edge = self.node_list.get(from_node)
        if edge != None:
            edge.append(
                Edge(from_node, to_node, weight))
            self.node_list.add(from_node, edge)
        else:
            self.node_list.add(
                from_node, [Edge(from_node, to_node, weight)])

    # O((V-1)^2); where V = number of verticies
    def print_nodes(self):
        for from_vertex in self.location_names:
            connected_verticies = []
            # vertex[1] -> Ex. "Western Governors University"
            for node in self.node_list.get(from_vertex[1]):
                connected_verticies.append(f"{node.from_node}->{node.to_node}")
            print(f"{node.from_node} is connected to {connected_verticies}")

    # def print_nodes(self):
    #    for vertex in self.location_names:
    #        # vertex[1] -> Ex. "Western Governors University"
    #        # edge.from_node, to_node, weight
    #        edge = self.node_list.get(vertex[1])
    #        print(f"{vertex[1]}->{edge}")
