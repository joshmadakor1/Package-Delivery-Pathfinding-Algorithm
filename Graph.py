import csv
from HashMap import HashMap


class Graph:

    # Default Constructor
    def __init__(self):
        self.location_names = [None] * 27
        self.distance_map = HashMap()
        self.node_list = HashMap()
        self.adjacency_list = HashMap()
        self.raw_distance_data = []

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

    # Populates the hashmap with distance data for each address
    def populate_hashmap_with_distance_data_for_each_adress(self):
        for i in range(len(self.raw_distance_data)):
            list = []
            for j in range(len(self.raw_distance_data)):

                # Add distance entries horizontally
                if j < i:
                    list.append([self.location_names[j][1],
                                self.raw_distance_data[i][j]])
                # Add distance entries vertically, to account for 2 way mapping
                elif j > i:
                    list.append([self.location_names[j][1],
                                self.raw_distance_data[j][i]])

            # Create an entry in the hash map for for all the distances to that address
            self.distance_map.add(self.location_names[i][1], list)

   # O(1)
    def add_node(self, name, address):
        print(address)
        return

    # O(V); where V = number of verticies
    def initialize_nodes_hashmap(self):
        for name in self.location_names:
            # name[1] -> Ex. "Western Governors University"
            # name[2] -> Ex. "4001 South 700 East"
            self.node_list.add(name[1], self.Node(name[1], name[2]))

    # O(1)
    def add_edge(self, from_node, to_node, weight):
        # print(f"{from_node}, {to_node}, {weight}")
        self.adjacency_list.add(
            f"{from_node}:{to_node}", self.Edge(from_node, to_node, weight))

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

    class Node():
        def __init__(self, name, address):
            self.name = name
            self.address = address

        def __str__(self):
            return f"{self.name} -> {self.address}"

    class Edge():
        def __init__(self, from_node, to_node, weight):
            self.from_node = from_node
            self.to_node = to_node
            self.weight = weight

        def __str__(self):
            return f"{self.from_node} -> {self.to_node} -> {self.weight}"
