from linked_list import linked_list

def partition(list, item):
    partition = linked_list()
    current = list.head
    past = None
    while current is not None:
        if current.item >= item:
            # remove item from this position and added it to a parallel thread
            temp = current
            # first item on the head
            if past is None:
                list.head = current.next
            # middle of the list
            else:
                past.next = current.next
            # add item to partition
            current = current.next
            temp.next = partition.head
            partition.head = temp
        else:
            past = current 
            current = current.next

    # merge
    if list.head is None and partition.head is not None:
        list.head = partition.head
    elif past is not None and partition.head is not None:
        past.next = partition.head
    return list


#####
myll = linked_list()

partition(myll, 1)
print(myll)


#####
myll = linked_list()

myll.add(2)

partition(myll, 1)
print(myll)


#####
myll = linked_list()

myll.add(62)
myll.add(21)
myll.add(50)
myll.add(30)
myll.add(44)

partition(myll, 45)
print(myll)


#####
myll = linked_list()

myll.add(62)
myll.add(21)
myll.add(50)
myll.add(30)
myll.add(44)

partition(myll, 2)
print(myll)

#####
myll = linked_list()

myll.add(21)
myll.add(62)
myll.add(50)
myll.add(30)
myll.add(44)

partition(myll, 45)
print(myll)
