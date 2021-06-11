# Nnamdi Joshua Madakor, ID: 000214961
import csv
from HashMap import HashMap
from Edge import Edge
from Node import Node

'''
************************************************************************************************
                            Graph Class Pseudocode with BIG-O Analysis
                                TOTAL CLASS COMPLEXITY: O(N^2)
************************************************************************************************
        


        __init__ is used to initialize the class properties
************************************************************************************************       
        __init__
        METHOD COMPLEXITY: O(3) -> O(1)
            INITIALIZE LOCATION NAMES:     O(1) - self.location_names = [None] * 27 
            INITIALIZE RAW DISTANCE ARRAY: O(1) - self.raw_distance_data = [] 
            INITIALIZE ADJACENCY MATRIX:   O(1) - self.adjacency_matrix = HashMap() 


        initialize_location_name_data reads in location data from the csv
************************************************************************************************* 
        initialize_location_name_data
        METHOD COMPLEXITY: O(3N) -> O(N)
            READ NAMES IN FROM CSV:  O(N) - names_reader = csv.reader(file)
            PLACE NAMES INTO LIST:   O(N) - raw_distance_names = list(names_reader)
            STORE NAMES IN 2D ARRAY: O(N) - for entry in (names): location_names[i] = entry


        initialize_location_distance_data reads in distance data from the csv
************************************************************************************************* 
        initialize_location_name_data
        METHOD COMPLEXITY: O(2N) -> O(N)
            READ DISTANCE IN FROM CSV:  O(N) - reader = csv.reader(file)
            PLACE DISTANCES INTO ARRAY: O(N) - self.raw_distance_data = list(reader)


        initialize_nodes_hashmap is used to create adjacency_matrix
************************************************************************************************* 
        initialize_nodes_hashmap
        METHOD COMPLEXITY: O(2N^2) -> O(N^2)
            GET DISTANCE BETWEEN EVERY LOCATION: O(N^2) - 2x nested "for-loop"
            STORE EDGES IN ADJACENCY MATRIX:     O(N)   - self.add_node('data')


        add_node is used to assist initialize_nodes_hashmap in creating adjacency_matrix
************************************************************************************************* 
        add_node
        METHOD COMPLEXITY: O(1+2N) -> O(N)
            ATTEMPT TO RETRIEVE A NODE:         O(1) - adjacency_matrix.get(from_node)
            IF NODE EXISTS, APPEND A NEW EDGGE: O(N) - adjacency_matrix.add(from_node, node)
            IF NODE NOT EXISTS, ADD A NEW NODE: O(N) - node.edges.append(node, [(new edge)])         
'''


class Graph:

    # Default Constructor
    def __init__(self):
        self.location_names = [None] * 27
        self.raw_distance_data = []
        self.adjacency_matrix = HashMap()

    # Time-complexity: O(n)
    # This method reads-in and stores the location name data
    def initialize_location_name_data(self):

        with open("./data/distance_names.csv") as file:
            names_reader = csv.reader(file)
            raw_distance_names = list(names_reader)
            i = 0
        for entry in raw_distance_names:
            # Populate location_names - Example:
            #   self.location_names[0] -> ['0', 'Western Governors University', '4001 South 700 East']
            #   self.location_names[1] -> ['1', 'International Peace Gardens', '1060 Dalton Ave S']
            self.location_names[i] = entry
            i += 1

    # Time-complexity: O(n)
    # This method reads-in and stores the package distance data.
    # This data is later used to create the complete graph
    def initialize_location_distance_data(self):
        with open("./data/distance_data.csv") as file:
            reader = csv.reader(file)
            self.raw_distance_data = list(reader)

    # Time-complexity: O(n^2)
    # This method takes the raw_distance_data read in from distance_data.csv
    #   and organizes it into a hashmap containing all of the possible nodes and
    #   their corresponding edges
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

    # Time-complexity: O(1)
    # This method adds a node to adjacency_matrix
    def add_node(self, from_node, to_node, weight):
        node = self.adjacency_matrix.get(from_node)
        if node != None:
            # If the node alreay exists, append the new edge to it and update hashmap
            node.edges.append(
                Edge(from_node, to_node, weight))
            # Add the new node with newly appended edge back to the hashmap
            self.adjacency_matrix.add(from_node, node)
        else:
            # Add a new node, ensure the value is an array. Will be used to hold multiple edges
            self.adjacency_matrix.add(
                from_node, Node(from_node, [Edge(from_node, to_node, weight)]))

    # O((V-1)^2); where V = number of verticies
    # USED FOR TESTING ONLY
    # This method prints all the nodes in the adjacency list
    def print_nodes(self):
        for from_vertex in self.location_names:
            connected_verticies = []
            # vertex[1] -> Ex. "Western Governors University"
            for edge in self.adjacency_matrix.get(from_vertex[1]).get_edges():
                connected_verticies.append(
                    f"{edge.from_node}-({edge.weight})->{edge.to_node}")
            print(f"{edge.from_node} is connected to {connected_verticies}")
