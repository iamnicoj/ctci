from avl_tree import avl_tree

# O(NLogN)
def is_unique(string):
    # I can use a bit array but we are not assuming ASCII vs UNICODE
    # With brute force O(len(string)^2) against the array

    # I can also use a sorted structed e.g balanced binary tree
    binary_tree = avl_tree()

    for ch in string:
        search = binary_tree.search(ch)
        if search is True: return False;

        binary_tree.add(ch)

    return True


print(is_unique('')) # True
print(is_unique('a')) # True
print(is_unique('asedf')) # True
print(is_unique('asdfa')) # False
print(is_unique('fjkashdgfkjasdfgaksjdhfgaskjdhfgasdkjfh')) # False
print(is_unique('qwertyuiopasdfghjklzxcvbnm,./;][`1234567890-=+_)(*&^%$#@!~')) # True

#############################################

# O(N) Asumming only ASCII strings
def is_unique_bitarray(string):
    dashboard = [False for _ in range(127)]

    for char in string:
        if dashboard[ord(char)]: return False

        dashboard[ord(char)] = True

    return True


print(is_unique_bitarray('')) # True
print(is_unique_bitarray('a')) # True
print(is_unique_bitarray('asedf')) # True
print(is_unique_bitarray('asdfa')) # False
print(is_unique_bitarray('fjkashdgfkjasdfgaksjdhfgaskjdhfgasdkjfh')) # False
print(is_unique_bitarray('qwertyuiopasdfghjklzxcvbnm,./;][`1234567890-=+_)(*&^%$#@!~')) # True




