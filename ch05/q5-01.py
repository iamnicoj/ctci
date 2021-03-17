import bit_manipulation as bit

## O()
##
def insertion(N, M, i, j):
    int_n = int(N, 2)
    int_m = int(M, 2)

    # 2. clean the N
    for x in range(i, j+1):
        int_n = bit.clearbit(int_n, x)
        # print("{0:b}".format(int_n))
    
    # 3. apply M
    new_m = int_m << i
    
    result = int_n | new_m

    return "{0:b}".format(result)

def optimized(N, M, i, j):
    int_n = int(N, 2)
    int_m = int(M, 2)
    # 1. create the mask
    left = -1 << j + 1
    right = (1 << i ) - 1
    mask = left | right
    # 2. clean the N
    clean_n = int_n & mask
    # 3. apply M
    new_m = int_m << i
    result = clean_n | new_m

    return "{0:b}".format(result)

###########
print(insertion('11111111111111', '00000', 5, 9))
print(insertion('11111111111111', '00001', 5, 9))
print(insertion('11111111111111', '00010', 5, 9))
print(insertion('11111111111111', '00100', 5, 9))
print(insertion('11111111111111', '01000', 5, 9))
print(insertion('11111111111111', '10000', 5, 9))

print(optimized('11111111111111', '00000', 5, 9))
print(optimized('11111111111111', '00001', 5, 9))
print(optimized('11111111111111', '00010', 5, 9))
print(optimized('11111111111111', '00100', 5, 9))
print(optimized('11111111111111', '01000', 5, 9))
print(optimized('11111111111111', '10000', 5, 9))