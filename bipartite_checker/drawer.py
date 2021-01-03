import networkx as nx
import matplotlib.pyplot as plt

from bipartite_checker import Graph, is_bipartite


def draw_bipartite(graph: Graph):
    """
    Draws bipartite coloring.
    :param graph: Graph object.
    """
    is_bipartite(graph)
    nx_graph = nx.Graph()

    for u_v, v_v in graph.edges:
        nx_graph.add_edge(u_v, v_v)

    nx.draw(nx_graph, node_color=[c.value.lower() for c in graph.node_colors], with_labels=True)
    plt.savefig('readme_out.png', format='PNG')
