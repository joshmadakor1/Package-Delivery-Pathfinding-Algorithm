import csv
from HashMap import HashMap


class Graph:

    # Default Constructor
    def __init__(self):
        self.location_names = [None] * 27
        self.raw_distance_data = []
        self.node_list = HashMap()
        self.adjacency_list = HashMap()

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
    def initialize_nodes_hashmap(self):
        for name in self.location_names:
            # name[1] -> Ex. "Western Governors University"
            # name[2] -> Ex. "4001 South 700 East"
            self.add_node(name[1], self.Node(name[1], name[2]))

    # Builds the hashmap which contains all the edges
    # O(V^2); where V = number of verticies
    def initialize_edges_hashmap(self):
        for i in range(len(self.raw_distance_data)):
            for j in range(len(self.raw_distance_data)):

                # Add distance entries horizontally
                if j < i:
                    self.add_edge(
                        from_node=self.location_names[i][1], to_node=self.location_names[j][1], weight=self.raw_distance_data[i][j])
                # Add distance entries vertically, to account for 2 way mapping
                elif j > i:
                    self.add_edge(
                        from_node=self.location_names[i][1], to_node=self.location_names[j][1], weight=self.raw_distance_data[j][i])
                    # list.append([self.location_names[j][1], self.raw_distance_data[j][i]])

   # O(1)
    def add_node(self, name, address):
        self.node_list.add(name, self.Node(name, address))

    # O(1)
    def add_edge(self, from_node, to_node, weight):
        edge = self.adjacency_list.get(from_node)
        if edge != None:
            edge.append(
                self.Edge(from_node, to_node, weight))
            self.adjacency_list.add(from_node, edge)
            # print(self.adjacency_list.get(from_node)[0].from_node)
            # p rint(self.adjacency_list.get(from_node)[0])
            # self.adjacency_list.print(from_node)

        else:
            self.adjacency_list.add(
                from_node, [self.Edge(from_node, to_node, weight)])
            # self.adjacency_list.print(from_node)

    # O((V-1)^2); where V = number of verticies
    def print_adjacency_list(self):
        for from_vertex in self.location_names:
            connected_verticies = []
            # vertex[1] -> Ex. "Western Governors University"
            for edge in self.adjacency_list.get(from_vertex[1]):
                connected_verticies.append(
                    f"{edge.from_node}->{edge.to_node}")
            print(f"{edge.from_node} is connected to {connected_verticies}")

    class Node():
        def __init__(self, name, address):
            self.name = name
            self.address = address

        def __str__(self):
            return f"{self.name}"

    class Edge():
        def __init__(self, from_node, to_node, weight):
            self.from_node = from_node
            self.to_node = to_node
            self.weight = weight

        def __str__(self):
            #  -> {self.weight}
            return f"{self.from_node} -> {self.to_node}"
