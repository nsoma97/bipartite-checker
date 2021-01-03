from bipartite_checker import Graph, is_bipartite, draw_bipartite

edge_list = [[1, 2], [2, 3], [3, 4], [4, 1], [4, 5], [5, 6], [1, 6]]

g = Graph().from_edges(edge_list)

draw_bipartite(g)




