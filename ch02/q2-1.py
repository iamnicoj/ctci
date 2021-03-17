from linked_list import linked_list            

#O(N^2)
def remove_dups(linked_list):
    # I can use a sorting structure like a balanced binary search tree
    # I am going to be just working with the same list 

    if linked_list.count < 1: return True

    anchor = linked_list.head

    while anchor is not None:
        cursor = anchor
        while cursor is not None and cursor.next is not None:
            if anchor.item == cursor.next.item:
                cursor.next = cursor.next.next
                linked_list.count -= linked_list.count 

            cursor = cursor.next
        
        anchor = anchor.next


myll = linked_list()

remove_dups(myll)
myll.print_list()

#####
myll = linked_list()

myll.add(2)

remove_dups(myll)
myll.print_list()

#####
myll = linked_list()

myll.add(2)
myll.add(2) #

remove_dups(myll)
myll.print_list()

#####
myll = linked_list()

myll.add(2)
myll.add(4)
myll.add(0)
myll.add(10)

remove_dups(myll)
myll.print_list()

####
myll = linked_list()
myll.add(4)
myll.add(2)
myll.add(0)
myll.add(4)
myll.add(10)
myll.add(0)
myll.add(10)

remove_dups(myll)
myll.print_list()