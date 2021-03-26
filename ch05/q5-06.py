def conversion(A, B):
    counter = 0
    xor = A ^ B
    while xor:
        if xor & 1:
            counter += 1
        xor = xor & (xor -1)
    return counter

def tests():
    print(conversion(0, 0) ) # 0
    print(conversion(0, 1) ) # 1 
    print(conversion(5, 15))  # 101 => 1111
    print(conversion(8, 4) ) #  1000 vs 100 = 2
    print(conversion(31, 2))

if __name__ == "__main__":
    tests()