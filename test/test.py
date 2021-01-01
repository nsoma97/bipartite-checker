import pytest

from bipartite_checker.checker import is_bipartite
from bipartite_checker.graph import Graph

expected = [
    ([[1, 2], [2, 3], [3, 1]], False),
    ([[1, 2], [2, 3], [3, 4], [4, 1]], True),
    ([[1, 2], [2, 3], [3, 4], [4, 1], [5, 5]], False),
    ([[1, 2], [2, 3], [3, 4], [4, 1], [5, 6], [6, 7], [7, 5]], False),
    ([[1, 2], [2, 3], [3, 4], [4, 1], [5, 6], [6, 7], [7, 8], [8, 5]], True),
    ([[1, 2], [1, 3], [1, 4]], True),
    ([[1, 2], [1, 3], [1, 4], [2, 5], [3, 5], [4, 5], [5, 6]], True),
    ([[1, 2], [1, 3], [1, 4], [2, 5], [3, 5], [4, 5], [5, 1]], False),
    ([[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [5, 6]], False),
    ([[1, 2], [2, 3], [3, 4], [4, 1], [4, 5], [5, 6], [1, 6]], True),
    (list(zip(list(range(1000)), list(range(1, 1001)))), True)
]


@pytest.mark.parametrize("edge_list,expected", expected)
def test_is_bipartite(edge_list, expected):
    g = Graph().from_edges(edge_list)
    assert expected == is_bipartite(g)
