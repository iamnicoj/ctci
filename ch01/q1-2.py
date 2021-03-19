# A Permutation of a string is another string that contains same characters, 
# only the order of characters can be different. For example, “abcd” and “dabc” 
# are Permutation of each other


# This is actually a wrong implementation as it identify if all characters
# of string A are included in string B, which is not the definition of permutation 
# O((N + M) * (Log M))
def str_is_a_superset(string_a, string_b):
    memo = {}
    cursor_b = 0

    for cursor_a in range(len(string_a)):
        if memo.get(string_a[cursor_a], None) is not None:
            continue
        elif cursor_b == len(string_b): return False

        while cursor_b < len(string_b):
            memo[string_b[cursor_b]] = 1
            cursor_b += 1
            if string_a[cursor_a] == string_b[cursor_b - 1]:
                break
            elif cursor_b == len(string_b): return False
            
    return True

# print(str_is_a_superset('', ''))            # True
# print(str_is_a_superset('s', ''))           # False
# print(str_is_a_superset('', 's'))           # True 
# print(str_is_a_superset('s', 's'))          # False
# print(str_is_a_superset('asdf', 'fdsa'))    # True
# print(str_is_a_superset('asdfg', 'fdsa'))   # False
# print(str_is_a_superset('fasdfasdfasdfasdfasdfasdfasdfasdf', 'fdsa'))       # True
# print(str_is_a_superset('asdfdfdsasdasdfasfdasdfasdfasdfasdg', 'asdf'))     # False


def check_permutation(string_a, string_b):
    if len(string_a) != len(string_b): return False

    dashboard = [0 for _ in range(127)]

    for char_a in range(len(string_a)):
        dashboard[ord(string_a[char_a])] += 1

    for char_b in range(len(string_b)):
        dashboard[ord(string_b[char_b])] -= 1
        if dashboard[ord(string_b[char_b])] < 0: return False
    
    return True

print(check_permutation('', 's'))           # True 
print(check_permutation('s', 's'))          # False
print(check_permutation('asdf', 'fdsa'))    # True
print(check_permutation('asdg', 'fdsa'))    # False
print(check_permutation('fasdfasdfasdfasdfasdfasdfasdfasdf', 'fasdfasdfasdfasdfasdfasdfasdfasdf'))       # True
print(check_permutation('asdfdfdsasdasdfasfdasdfasdfasdfag', 'asdfdfdsasdasdfasfdasdfasdfasdfaf'))     # False