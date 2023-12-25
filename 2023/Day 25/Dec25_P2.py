import networkx as nx

file = "example_input.txt"
# file = "input.txt"


def solve() -> int:
    global graph

    nodes_to_remove = nx.minimum_edge_cut(graph)
    for bad_node, bad_neighbour in nodes_to_remove:
        graph.remove_edge(bad_node, bad_neighbour)

    component1_length, component2_length = map(len, nx.connected_components(graph))

    return component1_length * component2_length


if __name__ == "__main__":
    # reading in the input
    graph = nx.Graph()
    with open(file, "r") as f:
        for line in f.read().splitlines():
            node, neighbours = line.split(": ")

            for neighbour in neighbours.split(" "):
                graph.add_edge(node, neighbour)

    print(solve())
