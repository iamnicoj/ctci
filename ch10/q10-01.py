def sorted_merge(A, B):
    current_a = len(A)
    for b in reversed(range(len(B))):
        for ar in reversed(range(current_a)):
            if A[ar] is not None and A[ar] < B[b]:
                if A[ar + 1] is None:
                    A[ar + 1] = B[b]
                    current_a = ar
                else:
                    move_to_the_righ(A, ar)
                    A[ar + 1] = B[b]
                break
            elif ar == 0 and A[ar] > B[b]:
                move_to_the_righ(A,0)
                A[0] = B[b]
                break
    return A 

def move_to_the_righ(array, position):
    for current in reversed(range(position, len(array))):
        if array[current] is not None:
            array[current + 1] = array[current]
        

# print(move_to_the_righ([1,2,3,4,5,None,None], 3))

print(sorted_merge([1,None],[2]))
print(sorted_merge([2, None],[1]))
print(sorted_merge([1,3,5, None, None, None],[2,4,7]))
print(sorted_merge([2,3,5, None, None, None],[1,4,7]))

######

def optimal_sorted_merge(A, B):
    cursor = len(A) - 1
    pointer_b = len(B) - 1
    pointer_a = cursor - pointer_b - 1

    while pointer_b >= 0:
        if pointer_a >= 0 and A[pointer_a] > B[pointer_b]:
            A[cursor] = A[pointer_a]
            pointer_a -= 1
        else:
            A[cursor] = B[pointer_b]
            pointer_b -= 1
        cursor -=1
    return A

print("optimal mode:")
print(optimal_sorted_merge([1,None],[2]))
print(optimal_sorted_merge([2, None],[1]))
print(optimal_sorted_merge([1,3,5, None, None, None],[2,4,7]))
print(optimal_sorted_merge([2,3,5, None, None, None],[1,4,7]))