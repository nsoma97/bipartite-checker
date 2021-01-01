from typing import List, Tuple
from itertools import chain


class Graph:
    """
    Class representing a graph
    """

    def __init__(self):
        self.nodes = {}
        self.edges = None

    def from_edges(self, edge_list: List[Tuple[int, int]]):
        """
        Initializes a graph with list of edges
        :param edge_list: list of vertices determined by pair of nodes
        :return: initialized graph object
        """
        self.nodes = set(list(chain(*list(zip(*edge_list)))))
        self.edges = edge_list

        return self
