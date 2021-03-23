from linked_list import linked_list, node

def sum_lists(list1, list2):
    num1 = get_num(list1)
    num2 = get_num(list2)

    total = num1 + num2
    result = linked_list()
    temp = result.head
    while total > 0:
        new_node = node(total % 10)
        if temp is None:
            result.head = new_node
            temp = result.head
        else:
            temp.next = new_node
            temp = temp.next
        total //= 10
    return result

def get_num(list):
    temp = list.head
    total = 0
    counter = 0
    while temp is not None:
        total += temp.item * (10 ** counter)
        counter += 1
        temp = temp.next
    return total

def sum_lists_reversed(list1, list2):
    num1 = get_num_reversed(list1)
    num2 = get_num_reversed(list2)

    total = num1 + num2
    result = linked_list()
    while total > 0:
        result.add(total % 10)
        total //= 10
    return result

def get_num_reversed(list):
    temp = list.head
    total = 0
    while temp is not None:
        total *=  (10)
        total += temp.item
        temp = temp.next
    return total


#####
myll1 = linked_list()

# partition(myll1, 1)
print(myll1)


#####
myll1 = linked_list()

myll1.add(6)
myll1.add(1)
myll1.add(7)

# partition(myll1, 1)
print(myll1)

myll2 = linked_list()

myll2.add(2)
myll2.add(9)
myll2.add(5)

# partition(myll1, 1)
print(myll2)

print(sum_lists(myll1, myll2))
print(sum_lists_reversed(myll1, myll2))