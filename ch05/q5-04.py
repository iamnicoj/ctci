def next_number(num):
    # count the number of 1s
    print(bin(num))
    found_next = False
    next_largest = num
    next_smallest = num
    num_ones = count_ones(num)
    while not found_next:
        next_largest += 1
        next_num_ones = count_ones(next_largest)
        if next_num_ones == num_ones:
            found_next = True

    found_next = False
    # while not found_next:
    #     next_smallest -= 1
    #     next_num_ones = count_ones(next_smallest)
    #     if next_num_ones == num_ones:
    #         found_next = True

    return next_largest, 0  #next_smallest

def count_ones(num):
    count_ones = 0
    while (num > 0):
        if num & 1 == 1:
            count_ones += 1
        num >>= 1

    return count_ones


def get_next(num):
    c = num
    c0, c1 = 0, 0
    while c & 1 == 0 and c != 0:
        c0 += 1
        c >>= 1
    
    while c & 1 == 1:
        c1 += 1
        c >>= 1
    
    if c0 + c1 > 31 or c0 + c1 == 0:
        return -1

    p = c1 + c0

    num |= 1 << p
    num &= ~((1 << p) - 1)
    num |= (1 << c1 -1) - 1

    return num

def get_prev(num):
    c = num
    c0, c1 = 0, 0

    while c & 1 == 1:
        c1 += 1
        c >>= 1
    
    if c == 0: return -1

    while c & 1 == 0 and c != 0:
        c0 += 1
        c >>= 1
    
    p = c0 + c1

    num &= ~(0) << (p + 1)

    mask = (1 << (c1 + 1)) - 1
    num |= mask << (c0 - 1)

    return num
    


num = 28
next = get_next(num)
prev = get_prev(num)
print(num, bin(num), next, bin(next), prev, bin(prev))

num = 31
next = get_next(num)
prev = get_prev(num)
print(num, bin(num), next, bin(next), prev, bin(prev))

num = 13948
next = get_next(num)
prev = get_prev(num)
print(num, bin(num), next, bin(next), prev, bin(prev))
