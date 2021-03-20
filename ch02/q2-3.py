from linked_list import linked_list            

# It can be the first of the last
def delete_a_node_from_head(the_list, item):
    if the_list.head is None or the_list.head.next is None:
        return None
    
    current = the_list.head

    while current is not None and current.next is not None:
        if current.next.item == item and current.next.next is not None:
            current.next = current.next.next
        
        current = current.next

########################
myll = linked_list()

myll.add(2)
myll.add(4)
myll.add(0)
myll.add(10)

print(myll)
delete_a_node_from_head(myll, 4)
print(myll)

delete_a_node_from_head(myll, 2)
print(myll)

delete_a_node_from_head(myll, 10)
print(myll)

delete_a_node_from_head(myll, 0)
print(myll)

delete_a_node_from_head(myll, 2)
print(myll)

delete_a_node_from_head(myll, 10)
print(myll)


#################################
def get_me_the_middle(the_list):
    size = 0
    current = the_list.head

    while current is not None:
        size += 1
        current = current.next
    
    if size == 0: return None

    current = the_list.head

    for i in range(int(size / 2)):
        current = current.next

    return current

def delete_middle(the_list, middle_node ):
    if middle_node is None or middle_node.next is None: return

    temp = middle_node.next

    middle_node.item = temp.item
    middle_node.next = temp.next


########################
myll = linked_list()

myll.add(2)
myll.add(4)
myll.add(0)
myll.add(10)

########################
print('real middle')
print(myll)
thanode = get_me_the_middle(myll)
print(thanode.item)

thanode = delete_middle(myll,thanode)
print(myll)



# delete_a_node_from_head(myll, 2)
# print(myll)

# delete_a_node_from_head(myll, 10)
# print(myll)

# delete_a_node_from_head(myll, 0)
# print(myll)

# delete_a_node_from_head(myll, 2)
# print(myll)

# delete_a_node_from_head(myll, 10)
# print(myll)
