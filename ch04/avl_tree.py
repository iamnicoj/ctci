class node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
    def print_node(self, level):
        print(level, self.data)

    def node_levels(self, current):
        if current is None:
            return 0;
        if current.left is None and current.right is None:
            return 1;
        left_levels = self.node_levels(current.left)
        right_levels = self.node_levels(current.right)

        return (1 + left_levels) if (left_levels > right_levels) else (1 + right_levels)
    
    def node_balance(self):
        return self.node_levels(self.right) - self.node_levels(self.left)

class avl_tree:

    def __init__(self):
        self.head = None
        
    def add(self, data):
        if self.head is None:
            self.head = node(data)
        else:
            self.head = self._inner_add(self.head, data)
    
    def _inner_add(self, current, data):
        if current.data > data:
            if current.left is None:
                current.left = node(data)
            else: 
                current.left = self._inner_add(current.left, data)
        else:
            if current.right is None:
                current.right = node(data)
            else: 
                current.right = self._inner_add(current.right, data)

        return self._balance_tree(current)
           
    def search(self, data):
        return self._inner_binary_search(self.head, data)
    
    def _inner_binary_search(self, current, data):
        if current is None: return False
        if current.data == data: return True
        if current.data > data: return self._inner_binary_search(current.left, data)

        return self._inner_binary_search(current.right, data)

    def remove(self, data):
        if self.head is None: return 
        self.head = self._inner_remove(self.head, data)
        
    def _inner_remove(self, current, data):
        if current is None: return None
        if current.data == data :
            if current.left is None and current.right is None:
                return None
            balance = current.node_balance()
            # check balance
            if balance > 0:
                # swap with highest balance
                current.data = self._swap_with_leaf(current.right, data, True)
                # remove leave
                current.right = self._remove_extreme_node(current.right, True)
            
            # check balance
            elif balance <= 0:
                # swap with highest balance
                current.data = self._swap_with_leaf(current.left, data, False)
                # remove leave
                current.left = self._remove_extreme_node(current.left, False)
                
        elif current.data > data:
            current.left = self._inner_remove(current.left, data)
        else:
            current.right = self._inner_remove(current.right, data)
        return current

    def _swap_with_leaf(self, current, data, lowest):
        if current is None:
            raise IndexError('Wrong AVL structure. Node was expected.')
        if current.left is None and current.right is None:
            temp = current.data
            current.data = data
            return temp
        if lowest:
            if current.left is None:
                temp = current.data
                current.data = data
                return temp
            return self._swap_with_leaf(current.left, data, True)
        else:
            if current.right is None:
                temp = current.data
                current.data = data
                return temp
            return self._swap_with_leaf(current.right, data, False)

    def _remove_extreme_node(self, current, lowest):
        if current is None: return None
        if current.left is None and current.right is None: return None
        if lowest:
            if current.left is None:
                # TODO remove redundency
                current = current.right
                return current
            current.left = self._remove_extreme_node(current.left, True)
        else:
            if current.right is None:
                current = current.left
                return current
            current.right = self._remove_extreme_node(current.right, False) 
        current = self._balance_tree(current)
        return current

    def levels(self):
        if self.head is None:
            return 0        
        return self.head.node_levels(self.head)
    
    def _balance_tree(self, current):    
        balance = current.node_balance()
        # Check Balance
        # Rotate Left - Balance 2
        if balance == 2 and current.right.node_balance() == 1:
            temp = current
            current = temp.right
            temp.right = current.left
            current.left = temp
        # Rotate Right - Balance -2
        elif balance == -2 and current.left.node_balance() == -1:
            temp = current
            current = temp.left
            temp.left = current.right
            current.right= temp
        # Rotate Left Right 2, -1
        elif balance == 2 and current.right.node_balance() == -1:
            temp = current
            current = temp.right.left
            temp.right.left = current.right
            current.right = temp.right
            temp.right = current.left
            current.left = temp
        # Rotate Right Left -2, 1f
        elif balance == -2 and current.left.node_balance() == 1:
            temp = current
            current = temp.left.right
            temp.left.right = current.left
            current.left = temp.left
            temp.left = current.right
            current.right = temp
        return current

    def print_avl_tree(self):
        self._inner_print_inorder(self.head, 1)
    
    def _inner_print_inorder(self, current, level):
        if current is None: return 0
        self._inner_print_inorder(current.left, level + 1)
        current.print_node(level)
        return self._inner_print_inorder(current.right, level + 1)