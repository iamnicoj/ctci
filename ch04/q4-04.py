from avl_tree import avl_tree
from random import randint

def is_balance(tree):
    
    if tree.head is None: 
        return True

    return _is_balanced(tree.head)
    

def _is_balanced(node):
    if node is None:
        return True
    if node.left is None and node.right is None:
        return True
    
    value_left = tree_depth(node.left) 
    value_right = tree_depth(node.right)
    
    value = value_right - value_left
    if value > 1 or value < -1 :
        return False
    
    temp_left = _is_balanced(node.left) 
    temp_right = _is_balanced(node.right)

    return temp_left and temp_right

def tree_depth(node):
    if node is None:
        return 0

    if node.left is None and node.right is None:
        return 1
    
    value_left = tree_depth(node.left) 
    value_right = tree_depth(node.right)
    
    return value_left + 1 if value_left >= value_right else value_right + 1


#########################
my_tree = avl_tree()

for _ in range(0, 100):
    my_tree.add(randint(0,100))

#########################

my_tree.print_avl_tree()

print(is_balance(my_tree))

my_tree.head.right.left = None

print(is_balance(my_tree))
