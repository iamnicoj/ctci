def one_way(str_a, str_b):
    len_a = len(str_a)
    len_b = len(str_b)

    if abs(len_a - len_b) > 1:
        return False

    one_way = 0
    j = 0
    shortest = len_b if len_a > len_b else len_a
    for i in range(shortest):
        if str_a[i] == str_b[j]:
            j += 1
        elif one_way > 1:
            return False      
        elif len_a > len_b:
            if str_a[i + 1] == str_b[j]:
                one_way += 1
            else:
                return False
        elif len_a < len_b:
            if str_a[i] == str_b[j + 1]:
                one_way += 1
                j += 2
            else:
                return False
        else:
            j += 1
            one_way += 1
    return True



def tests():
    print(one_way('pale', 'pa'))  ## False
    print(one_way('pa', 'pale'))  ## False
    print(one_way('pale', 'ple'))  ## True
    print(one_way('pales', 'pale'))  ## True
    print(one_way('ples', 'pales'))  ## True
    print(one_way('paless', 'palea'))  ## False
    print(one_way('palea', 'paless'))  ## False
    print(one_way('pale', 'bale'))  ## True
    print(one_way('pales', 'bake'))  ## False

if __name__ == "__main__":
    tests()