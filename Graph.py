import csv
import sys
from HashMap import HashMap
from Edge import Edge
from Node import Node
from queue import Queue


class Graph:

    # Default Constructor
    def __init__(self):
        self.location_names = [None] * 27
        self.raw_distance_data = []
        self.node_list = HashMap()

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
    def add_node(self, from_node, to_node, weight):
        node = self.node_list.get(from_node)
        if node != None:
            node.edges.append(
                Edge(from_node, to_node, weight))
            self.node_list.add(from_node, node)
        else:
            self.node_list.add(
                from_node, Node(from_node, [Edge(from_node, to_node, weight)]))

    # O((V-1)^2); where V = number of verticies
    def print_nodes(self):
        for from_vertex in self.location_names:
            connected_verticies = []
            # vertex[1] -> Ex. "Western Governors University"
            for edge in self.node_list.get(from_vertex[1]).get_edges():
                connected_verticies.append(
                    f"{edge.from_node}-({edge.weight})->{edge.to_node}")
            print(f"{edge.from_node} is connected to {connected_verticies}")

    def get_shortest_distance_to_all_nodes(self, start, nodes_remaining):
        current_node = start
        total_distance = 0

        while (len(nodes_remaining) > 0):
            edges = self.node_list.get(current_node).edges
            shortest_distance = sys.maxsize

            for edge in edges:
                if edge.to_node in nodes_remaining:
                    if float(edge.weight) < shortest_distance:
                        shortest_distance = float(edge.weight)
                        current_node = edge.to_node
                        #print(f"New shortest distance: {shortest_distance}")
            nodes_remaining.discard(current_node)
            print(f"{shortest_distance}")
            total_distance += shortest_distance
        return(total_distance)

    #### DEPRECATED ####
    def get_shortest_path_brute_force(self, current_node, remaining_nodes, total_distance):
        # remaining_nodes is a set that contains nodes that have not been visited yet

        remaining_nodes.discard(current_node)
        if (len(remaining_nodes) == 0):
            print(f"Total Distance: {total_distance}")
            return
        edges = self.node_list.get(current_node).edges

        for edge in edges:
            if edge.to_node in remaining_nodes:

                self.get_shortest_path_brute_force(
                    edge.to_node, remaining_nodes, total_distance + float(edge.weight))

    #### DEPRECATED ####
    def breadth_first_iterative(self, current_node):
        q = Queue()
        visited = set()
        q.put(current_node)
        while(q.qsize() != 0):
            current_node = q.get()
            visited.add(current_node)
            print(current_node)
            edges = self.node_list.get(current_node).edges
            for edge in edges:
                if not edge.to_node in visited:
                    q.put(edge.to_node)

    #### DEPRECATED ####
    def traverse_depth_first(self, root):
        node = self.node_list.get(root)
        distance = 0
        neighbor_weight = 0
        if (node == None):
            return
        stack = []
        visited_nodes = set()
        stack.append(node.name)

        iterations = 0
        while(len(stack) != 0):
            iterations += 1
            current_node = stack.pop()
            # print("popping")

            if (current_node in visited_nodes):
                neighbor_weight = 0.0
                continue
            distance += float(neighbor_weight)
            print(f"Visiting: {current_node}")

            visited_nodes.add(current_node)

            neighbors = self.node_list.get(current_node).edges
            for neighbor in neighbors:
                if (not neighbor.to_node in visited_nodes):
                    stack.append(neighbor.to_node)
                    neighbor_weight = neighbor.weight
                    # print("pushing")

        print(f"Iterations: {iterations}")
        print(f"Distance: {distance}")
