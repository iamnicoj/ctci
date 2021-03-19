class node():
    def __init__(self, data):
        self.item = data
        self.left = None
        self.right = None
class tree():
    def __init__(self):
        self.head = None
    
    def create_tree(self, sorted_array):
        if sorted_array is None: return None

        self.head = self._inner_create(sorted_array, 0, len(sorted_array) -1)

    
    def _inner_create(self, sorted_array, left, right):        
        if left == right:
            return node(sorted_array[right])

        middle = int((right - left) / 2)
        leftover = (right - left) % 2
        middle_node = node(sorted_array[middle])

        if(middle - 1 > 0):
            middle_node.left = self._inner_create(sorted_array[::middle], 0, middle - 1)        
            middle_node.right = self._inner_create(sorted_array[middle + 1::], 0, middle - 1 - leftover)

        else:
            middle_node.right = self._inner_create(sorted_array[1::], 0, 0)

        return middle_node

    def __str__(self):
        self._inner_print_inorder(self.head, 1)
    
    def _inner_print_inorder(self, current, level):
        if current is None: return 0
        self._inner_print_inorder(current.left, level + 1)
        current.print_node(level)
        self._inner_print_inorder(current.right, level + 1)
        
    
#####################
mylist = [0]
mytree = tree()
mytree.create_tree(mylist)
print(mylist)

mylist = [0,1]
mytree = tree()
mytree.create_tree(mylist)
print(mylist)

mylist = [0,1,2]
mytree = tree()
mytree.create_tree(mylist)
print(mylist)

mylist = [0,1,2,3]
mytree = tree()
mytree.create_tree(mylist)
print(mylist)

mylist = [0,1,2,3,4]
mytree = tree()
mytree.create_tree(mylist)
print(mylist)

mylist = [0,1,2,3,4,5]
mytree = tree()
mytree.create_tree(mylist)
print(mylist)

mylist = [0,1,2,3,4,5,6]
mytree = tree()
mytree.create_tree(mylist)
print(mylist)
