from linked_list import linked_list            

# O(n) time and space
def kth_to_the_last(list, k):
    if list is None or list.head is None: return None

    count, item = _kth_tothelast_recursive(list.head, k)

    return item;

def _kth_tothelast_recursive(node, k):
    if node.next is None:
        if k == 0:
            return (0, node.item)
        else:
            return (1, None)
    else:
        count, downstream_result = _kth_tothelast_recursive(node.next, k)
        if downstream_result is None and k == count:
            return ((count + 1),node.item)        
        return (count + 1, None)       



##############################
myll = linked_list()

print(kth_to_the_last(myll, 1))

#####
myll = linked_list()

myll.add(2)

print(kth_to_the_last(myll, 0))

#####
myll = linked_list()

myll.add(2)

print(kth_to_the_last(myll, 1))

#####
myll = linked_list()

myll.add(2)
myll.add(3) #

print(kth_to_the_last(myll, 1))

#####
myll = linked_list()

myll.add(2)
myll.add(4)
myll.add(0)
myll.add(10)

print(kth_to_the_last(myll, 3))

####
myll = linked_list()
myll.add(1)
myll.add(2)
myll.add(3)
myll.add(4)
myll.add(5)
myll.add(6)
myll.add(7)

print(kth_to_the_last(myll, 6))