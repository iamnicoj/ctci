from avl_tree import avl_tree
from random import randint


def validate_bst(tree):
    if tree.head is None:
        return True
    return _recursive_validate(tree.head.left, tree.head.data, True) and _recursive_validate(tree.head.right, tree.head.data, False) 

def _recursive_validate(node, parent_value, is_left):
    if node is None:
        return True
    
    if is_left and node.data > parent_value:
        return False
    if not is_left and node.data < parent_value:
        return False
    
    return _recursive_validate(node.left, node.data, True) and _recursive_validate(node.right, node.data, False) 

def validate_bst_2(tree):
    return _inner_v_2(tree.head)

def _inner_v_2(node, min = None, max = None):
    if node is None:
        return True
    
    if min and node.data < min or max and node.data > max:
        return False
    
    return _inner_v_2(node.left, min, node.data) and _inner_v_2(node.right, node.data, max) 



#########################
my_tree = avl_tree()

for _ in range(0, 100):
    my_tree.add(randint(0,100))

#########################

my_tree.print_avl_tree()

print(validate_bst_2(my_tree))

my_tree.head.right.left.data = 4

print(validate_bst_2(my_tree))
