from linked_list import linked_list, node

def palindrome(list):
    if not list.head:
        return True
    slow = fast = list.head
    stack = []
    while fast and fast.next:
        stack.append(slow.item)
        slow = slow.next
        fast = fast.next.next
    
    if fast:
        slow = slow.next

    while slow:
        if slow.item != stack.pop(len(stack)- 1):
            return False
        slow = slow.next
    return True

def is_palindrome_recursive(list):
    def get_len(node):
        if not node:
            return 0
        else:
            return 1 + get_len(node.next)    

    def recursive_transverse(node, length):
        if not node or length ==  0:  ## even list
            return True, node
        elif length == 1:  # odd list
            return True, node.next

        is_palindrome, fwd_node = recursive_transverse(node.next, length - 2)

        if not is_palindrome or not fwd_node:
            return False, None
        
        if node.item == fwd_node.item:
            return True, fwd_node.next
        else:
            return False, None        
        

    length = get_len(list.head)
    is_palindrome, node = recursive_transverse(list.head, length)
    return is_palindrome

myll1 = linked_list()

print(myll1)    
print(palindrome(myll1))
print(is_palindrome_recursive(myll1))



myll1 = linked_list()
myll1.add(6)
myll1.add(1)
myll1.add(7)
print(myll1)    
print(palindrome(myll1))
print(is_palindrome_recursive(myll1))

myll1 = linked_list()
myll1.add(6)
myll1.add(1)
myll1.add(7)
myll1.add(1)
myll1.add(6)
print(myll1)    
print(palindrome(myll1))
print(is_palindrome_recursive(myll1))

myll1 = linked_list()
myll1.add(6)
myll1.add(1)
myll1.add(7)
myll1.add(3)
myll1.add(1)
myll1.add(6)
print(myll1)    
print(palindrome(myll1))
print(is_palindrome_recursive(myll1))