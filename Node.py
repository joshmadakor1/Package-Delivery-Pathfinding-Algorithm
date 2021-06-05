from HashMap import HashMap
from Edge import Edge


class Node():
    def __init__(self, name, edges):
        self.name = name
        #self.address = address
        self.edges = edges

    def __str__(self):
        return f"{self.name}"

    def add_edge(self, target_node, weight):
        self.edges.add(target_node, Edge(from_node=self.name,
                       to_node=target_node, weight=weight))

    def get_neighbors(self):
        return self.edges
