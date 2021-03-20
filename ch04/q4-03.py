from avl_tree import avl_tree
from random import randint

def list_of_a_depth(tree, level):
    if tree is None or tree.head is None:
        return None

    return _list_inner_level(tree.head, level, 1)

def _list_inner_level(node, level, actual):
    if node is None: return []
    if level == actual:
        return [node.data]

    left_array = _list_inner_level(node.left, level, actual + 1)
    right_array = _list_inner_level(node.right, level, actual + 1)

    return left_array[::] + right_array[::]

#########################

def list_of_all_depths(tree):
    if tree is None and tree.head is None:
        return [[]]

    all_depths =[]

    _inner_level_transverse(tree.head, all_depths, 1)

    return all_depths

def _inner_level_transverse(node, all_depths, level):
    if node is None: return

    if len(all_depths) < level:
        all_depths.append([])
    
    all_depths[level - 1].append(node.data)
    _inner_level_transverse(node.left, all_depths, level + 1)
    _inner_level_transverse(node.right, all_depths, level + 1)

    

    

#########################
my_tree = avl_tree()

for _ in range(0, 100):
    my_tree.add(randint(0,100))

#########################

my_tree.print_avl_tree()

print(list_of_a_depth(my_tree, 5))

print(list_of_all_depths(my_tree))

 