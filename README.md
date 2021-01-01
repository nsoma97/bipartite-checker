# Bipartite-checker
Short code to check whether a graph is biparite

## Usage
The usage is demonstrated in the tests. The graph is represented by a list of edges.

```python
from bipartite_checker import Graph, is_bipartite

edge_list = [[1, 2], [2, 3], [3, 1]]

graph = Graph().from_edges(edge_list)

print(is_bipartite(graph))
# output: False
```