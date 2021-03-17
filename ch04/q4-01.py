from dgraph import basic_graph, graph_node

# O(E*V)
# Implemented using a BFS iterative approach
def are_nodes_connected(graph, point_a, point_b):
    visited = []
    queue = []

    node_a = graph.search(point_a)
    node_b = graph.search(point_b)

    if node_a is None or node_b is None: return False

    queue.insert(0, node_a)

    while len(queue) > 0:
        current_node = queue.pop()
        visited.append(current_node)

        for neiborgh in current_node.adjacent:
            if neiborgh == node_b: return True

            if neiborgh not in visited and neiborgh not in queue:
                queue.insert(0, neiborgh)
        
    return False

###############################

my_graph = basic_graph()
my_graph.add_node("walk")
my_graph.add_node("with")
my_graph.add_node("me")
my_graph.add_node("to")
my_graph.add_node("the")
my_graph.add_node("park")
my_graph.add_node("other")
my_graph.add_node("random")
my_graph.add_node("island")
my_graph.add_adjacent("walk", "with", False)
my_graph.add_adjacent("me", "with", False)
my_graph.add_adjacent("with", "to", False)
my_graph.add_adjacent("to", "the", False)
my_graph.add_adjacent("the", "me", True)
my_graph.add_adjacent("the", "walk", True)
my_graph.add_adjacent("the", "other", True)
my_graph.add_adjacent("the", "random", True)

my_graph.print_graph()

print(are_nodes_connected(my_graph, 'walk', 'with')) # true
print(are_nodes_connected(my_graph, 'walk', '1234')) # false
print(are_nodes_connected(my_graph, 'walk', 'island')) # false
print(are_nodes_connected(my_graph, 'walk', 'random')) # true

