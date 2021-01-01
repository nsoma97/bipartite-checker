from typing import List, Tuple

from bipartite_checker.graph import Graph
from enum import Enum


class Color(Enum):
    """
    Class that represents node colors
    """
    NONE = "None"
    RED = "Red"
    GREEN = "Green"


def has_self_cycle(edge_list: List[Tuple[int, int]]) -> bool:
    """
    Checks whether a graph has a self loop
    :param edge_list: list of vertices determined by pair of nodes
    :return: True if has self cycle, False if not
    """
    for u, v in edge_list:
        if u == v:
            return True

    return False


def get_next_nodes(graph: Graph, current: int):
    """
    Returns neighbours of a node
    :param graph: class representing a graph
    :param current: the actual node
    :return: set of neighbouring nodes
    """
    nexts = set()
    for u, v in graph.edges:
        if u == current:
            nexts.add(v)
        elif v == current:
            nexts.add(u)

    return nexts


def get_opposite_color(c: Color) -> Color:
    """
    Returns opposite color
    :param c: Current color
    :return: Opposite color
    """
    if c == Color.RED:
        return Color.GREEN
    elif c == Color.GREEN:
        return Color.RED
    else:
        return Color.NONE


def is_bipartite(graph: Graph):
    """
    Determines whether a graph is bipartite
    :param graph: class representing a graph
    :return: True if bipartite, False if not
    """

    if has_self_cycle(graph.edges):
        return False

    nodes = list(graph.nodes)
    node_colors = [Color.RED] + ([Color.NONE] * (len(graph.nodes) - 1))

    traversal_queue = {nodes[0]}
    visited = {nodes[0]}
    while traversal_queue:
        current = traversal_queue.pop()
        neighbours = get_next_nodes(graph, current)

        traversal_queue = traversal_queue.union(neighbours).difference(visited)
        visited.add(current)

        for neighbour in neighbours:
            current_color = node_colors[nodes.index(current)]
            neighbour_color = node_colors[nodes.index(neighbour)]

            if neighbour_color == Color.NONE:
                node_colors[nodes.index(neighbour)] = get_opposite_color(current_color)

            if neighbour_color == current_color:
                return False

        if not traversal_queue:
            for node in nodes:
                if node_colors[nodes.index(node)] == Color.NONE:
                    node_colors[nodes.index(node)] = Color.RED
                    traversal_queue = {node}
                    break

    return True
