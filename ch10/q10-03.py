from typing import Optional, Sequence


def search_rotated_array(array, num):
    if not array: return None

    return _inner_search(array, num, 0, len(array) - 1)


def _inner_search(array, num, start, end):
    
    middle = ((end - start) // 2) + start
    if array[middle] == num: return middle
    if end - start == 0: return None
    
    result = None
    search_both_sides = False
        
    if array[middle] < num :
        result = _inner_search(array, num, middle + 1, end)
        search_both_sides = True
    if result == None:
        result = _inner_search(array, num, start, middle)
        if result is None and not search_both_sides:
            result = _inner_search(array, num, middle + 1, end)
    
    return result

def search_rotated(array: Sequence[int], num: int) -> Optional[int]:
    if not array: return None
    return _recursive_search(array, num, 0, len(array) -1 )


def _recursive_search(array, num, start, end):
    middle = ((end - start) // 2 + start)
    if array[middle] == num: return middle
    if end - start <= 0: return None

    result = None
    if array[start] < array[middle]: # left side is normal
        if array[start] <= num and num < array[middle]: # serch left
            result = _recursive_search(array, num, start, middle - 1)
        else:
            result = _recursive_search(array, num, middle + 1, end)
    elif array[middle] < array[end]:  # right side is normal
        if array[middle] < num and num <= array[end]:
            result = _recursive_search(array, num, middle + 1, end)
        else:
            result = _recursive_search(array, num, start, middle - 1)
    elif array[start] == array[middle]:
        if array[middle] != array[end]:
            result = _recursive_search(array, num, middle + 1, end)
        else:
            result = _recursive_search(array, num, start, middle - 1)
            if result is None:
                result = _recursive_search(array, num, middle + 1, end)
    return result

def example():
    print(search_rotated([8,9,10,0,1,2,3,4,5,6,7], -1))
    print(search_rotated([8,9,10,0,1,2,3,4,5,6,7], 0))
    print(search_rotated([8,9,10,0,1,2,3,4,5,6,7], 2))
    print(search_rotated([8,9,10,0,1,2,3,4,5,6,7], 3))
    print(search_rotated([8,9,10,0,1,2,3,4,5,6,7], 4))
    print(search_rotated([8,9,10,0,1,2,3,4,5,6,7], 5))
    print(search_rotated([8,9,10,0,1,2,3,4,5,6,7], 6))
    print(search_rotated([8,9,10,0,1,2,3,4,5,6,7], 7))
    print(search_rotated([8,9,10,0,1,2,3,4,5,6,7], 8))
    print(search_rotated([8,9,10,0,1,2,3,4,5,6,7], 9))
    print(search_rotated([8,9,10,0,1,2,3,4,5,6,7], 10))
    print(search_rotated([8,9,10,0,1,2,3,4,5,6,7], 11))
    print('repeated array')
    print(search_rotated([2, 3, 1, 2, 2, 2, 2, 2, 2, 2], 3))
    print(search_rotated([2, 3, 1, 2, 2, 2, 2, 2, 2, 2], 0))
    print(search_rotated([2, 3, 1, 2, 2, 2, 2, 2, 2, 2], 1))
    print(search_rotated([2, 3, 1, 2, 2, 2, 2, 2, 2, 2], 2))


if __name__ == "__main__":
    example()