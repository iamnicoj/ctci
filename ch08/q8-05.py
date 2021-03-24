def bit_manipulation_multiply(a, b):
    result, outer_sig = 0, 0
    while a > 0:
        temp = 0
        inner_sig = 0
        temp_b = b
        while temp_b > 0:
            temp += ((a & 1) & (temp_b & 1)) << inner_sig
            temp_b >>= 1
            inner_sig += 1
        temp <<= outer_sig
        result += temp
        outer_sig += 1
        a >>= 1
    return result

def recursive_multiply(a, b):
    if not b:
        return 0
    if b == 1:
        return a
    return recursive_multiply(a, b - 1) + a

def recursive_multiply_opt(a, b):
    def inner_recursive(min, max):
        if not b:
            return 0
        if b == 1:
            return max
        middle = min >> 1
        half = recursive_multiply(middle, max)
        half += half + (max if (min % 2 > 0) else 0)
        return half

    low = a if a < b else b
    high = a if a > b else b

    return inner_recursive(low, high)

def tests():
    print(bit_manipulation_multiply(1,0))
    print(bit_manipulation_multiply(1,1))
    print(bit_manipulation_multiply(1,2))
    print(bit_manipulation_multiply(2,2))
    print(bit_manipulation_multiply(5,6))
    print(recursive_multiply(1,0))
    print(recursive_multiply(1,1))
    print(recursive_multiply(1,2))
    print(recursive_multiply(2,2))
    print(recursive_multiply(5,6))
    print(recursive_multiply_opt(1,0))
    print(recursive_multiply_opt(1,1))
    print(recursive_multiply_opt(1,2))
    print(recursive_multiply_opt(2,2))
    print(recursive_multiply_opt(5,6))

if __name__ == "__main__":
    tests()
