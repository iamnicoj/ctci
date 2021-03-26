from binary_search_tree import BinarySearchTree


def successor(node):
    def min_value(node):
        if not node:
            return None
        if not node.left:
            return node
        return min_value(node.left)
    
    def succ_parent(node, value):
        if not node:
            return None
        if node.key > value:
            return node
        return succ_parent(node.parent, value)

    if not node:
        return None
    value = min_value(node.right)
    if value:
        return value
    return succ_parent(node.parent, node.key)


def test_in_order_successor():
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    bst.insert(11)
    bst.insert(14)

    # Test all nodes
    inputs = [5, 9, 11, 12, 14, 20, 25]
    outputs = inputs[1:]
    outputs.append(None)

    for x, y in zip(inputs, outputs):
        test = bst.get_node(x)
        succ = successor(test)
        if succ is not None:
            assert succ.key == y
        else:
            assert succ == y


if __name__ == "__main__":
    test_in_order_successor()
