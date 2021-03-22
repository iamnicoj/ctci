def magic_index(array, seed = 0):
    if len(array) == 0: return None

    middle = len(array) // 2
    if array[middle] == middle + seed: return middle + seed
    if middle == 0: return None
    if array[middle] > middle:
        return magic_index(array[:middle], seed)
    return magic_index(array[(middle + 1):], middle + 1)




print(magic_index([0]))  # 0 
print(magic_index([1]))  # None
print(magic_index([0,21]))  # None
print(magic_index([0,3,5,76,123]))  # 0
print(magic_index([0,1,2,3,123]))  # 0
print(magic_index([-11,-5,0,3,4]))  # 0
print(magic_index([-11,-5,0,1, 2, 3, 6, 555]))  # 0
# WONT WORK
print(magic_index([1,1,1,3, 3, 3, 3, 3, 8, 123]))  # 0 binary search WONT WORK AS WORK SIZES could have 
