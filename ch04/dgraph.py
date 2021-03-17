# Basic graph implementation
# Future updates could includ:
# * use a map object to allow for additional payload data at the node level
# 

class graph_node():
    def __init__(self, data):
        self.data = data
        self.adjacent = []

class basic_graph():
    def __init__(self):
        self.nodes = []

    def add_node(self, data):        
        if self.search(data) is not None:
            raise ValueError(f"Node {data} already exists")
        self.nodes.append(graph_node(data))

    def add_adjacent(self, point_a, point_b, both_ways):
        # check if both nodes Exist
        node_a = self.search(point_a)
        if node_a is None:
            raise ValueError(f"point_a {point_a} doesn't exist")
        node_b = self.search(point_b)
        if node_b is None:
            raise ValueError(f"point_b {point_b} doesn't exist")
        # check if connection from A to B exists
        if self._is_adjacent(node_a, node_b):
            raise ValueError(f"connection btw {point_a} and {point_b} already exists")
        # create the connection
        node_a.adjacent.append(node_b)
        # verify the same if both_ways is True
        if both_ways:
            if self._is_adjacent(node_b, node_a):
                raise ValueError(f"connection btw {point_b} and {point_a} already exists")
            # create the connection
            node_b.adjacent.append(node_a)
        
    def print_graph(self):
        for node in self.nodes:
            print(f"Node {node.data}: ", end='')
            for neiborgh in node.adjacent:
                print(f"{neiborgh.data}, ", end='')
            print()

    def search(self, data):
        for node in self.nodes:
            if node.data == data:
                return node
        return None;

    def _is_adjacent(self, node_a, node_b):
        if node_a is None: return False;
        for neiborgh in node_a.adjacent:
            if neiborgh.data == node_b.data: return True
        return False;

    def dfsearch(self, from_point_a):
        node_a = self.search(from_point_a)
        visited_nodes = []
        indent = 0

        if node_a is not None:
            self._inner_dfsearch(node_a, visited_nodes, indent)
        
    def _inner_dfsearch(self, node, visited_nodes, indent):
        if node.data in visited_nodes: return
        
        visited_nodes.append(node.data)
        for _ in range(indent): print('  ', end='')
        
        print(node.data)
        
        for neiborgh in node.adjacent:
            self._inner_dfsearch(neiborgh, visited_nodes, indent + 2)

    
    # Iterative solution with a queue ;)
    def bfsearch_iterative(self, from_point_a):
        node_a = self.search(from_point_a)
        if node_a is None: return
        
        visited_nodes = []
        queue = []

        queue.append(node_a)
        
        while len(queue) > 0:
             current_node = queue.pop()
             visited_nodes.append(current_node)
             print(f"touch: {current_node.data}")
             for neiborgh in current_node.adjacent:
                 if (neiborgh not in visited_nodes) and (neiborgh not in queue):
                    queue.insert(0, neiborgh)


    def bfsearch(self, from_point_a):
        node_a = self.search(from_point_a)
        visited_nodes = []
        indent = 0

        if node_a is not None:
            print(f"Touch {node_a.data}")
            self._inner_bfsearch(node_a, visited_nodes, indent + 2)

    def _inner_bfsearch(self, node, visited_nodes, indent):
        if node.data in visited_nodes: return
        
        visited_nodes.append(node.data)
        
        for neiborgh in node.adjacent:
            if neiborgh.data in visited_nodes: continue 
            for _ in range(indent): print('  ', end='')
            print(f"Touch {neiborgh.data}")
        
        for neiborgh in node.adjacent:
            self._inner_bfsearch(neiborgh, visited_nodes, indent + 2)

    def are_nodes_connected(self, point_a, point_b):
        raise NotImplementedError()

    def shortest_path(self, point_a, point_b):
        raise NotImplementedError()

    def remove_node(self, data):
        raise NotImplementedError()

    def remove_link(self, point_a, point_b, both_ways):
        raise NotImplementedError()
