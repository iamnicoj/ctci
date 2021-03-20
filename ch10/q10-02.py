# O(2 * len(array_string)*len(eachstring)) "average"
# if all strings aren't anagrams, it will be on(^2)
# TODO This can be simplified using a hashtable from the beginning
def group_anagrams(array_strings):
    ordered_array = []
    processed_strings = [0 for _ in array_strings]
    memo = {}

    for index in range(len(array_strings)):
        if processed_strings[index] == 1:
            continue
        ordered_array.append(array_strings[index])
        processed_strings[index] += 1

        bit_array = []
        if memo.get(index, None) is not None:
            bit_array = memo[index]
        else:
            bit_array = get_ascii_bit_array(array_strings[index])
            memo[index] = bit_array

        for cursor in range(index + 1, len(array_strings)):
            if processed_strings[cursor] == 0:
                temp_bit_array = []
                if memo.get(cursor, None) is not None:
                    temp_bit_array = memo[cursor]
                else:
                    temp_bit_array = get_ascii_bit_array(array_strings[cursor])
                    memo[cursor] = temp_bit_array

                result = validate_ascii_tables(temp_bit_array, bit_array[::])
                if result == True:
                    ordered_array.append(array_strings[cursor])
                    processed_strings[cursor] += 1
    return ordered_array

# O(m)
def validate_ascii_tables(main_bit_array, bit_array):
    for bit in range(len(main_bit_array)):
        if main_bit_array[bit] > 0:
            bit_array[bit] -= main_bit_array[bit]
            if bit_array[bit] < 0:
                return False
    return True

# O(n)
def get_ascii_bit_array(string):
    bit_array = [0 for _ in range(127)]
    
    for char in string:
        bit_array[ord(char)] += 1
    return bit_array;



array_strings = ['fluster', 'natas', 'listen', 'nothing to look here', 'santa', 'silent', 'satan', 'restful']

print(group_anagrams(array_strings))