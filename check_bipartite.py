import sys

from bipartite_checker import Graph, is_bipartite


def main():
    if len(sys.argv) > 1:

        try:
            arguments = [int(a) for a in sys.argv[1:]]

            edge_list = []
            for i in range(0, len(arguments) - 1, 2):
                edge_list.append([arguments[i], arguments[i+1]])

            g = Graph().from_edges(edge_list)

            if is_bipartite(g):
                print('The graph is bipartite.')
            else:
                print('The graph is not bipartite.')

        except:
            print('Error while running the program, please check your input!')

    else:
        print('Please specify a graph!')


if __name__ == "__main__":
    main()
