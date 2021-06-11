# Nnamdi Joshua Madakor, ID: 000214961
from Edge import Edge


class Node():
    def __init__(self, name, edges):
        self.name = name
        self.edges = edges

    # Time-complexity: O(n)
    # Returns the name of the node
    def __str__(self):
        return f"{self.name}"

    # Time-complexity: O(n)
    # Adds an edge to this node
    def add_edge(self, target_node, weight):
        self.edges.add(target_node, Edge(from_node=self.name,
                       to_node=target_node, weight=weight))

    # Time-complexity: O(n)
    # Returns edges for this node
    def get_edges(self):
        return self.edges
