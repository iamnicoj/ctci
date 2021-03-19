def number_to_binary_str(number):    
    # 33  / 2 = 16 | 1
    # 16  / 2 = 8  | 0
    # 8   / 2 = 8  | 0
    # 4   / 2 = 4  | 0
    # 2   / 2 = 1  | 0
    #         V 1  | 1
    if number == 0: return "0"

    result = ''

    while number > 1:
        flag = number % 2
        if flag: 
            result = "1" + result
        else:
            result = "0" + result
        number = int(number / 2);

    result = "1" + result

    return result


# print(number_to_binary_str(0))
# print(number_to_binary_str(1))
# print(number_to_binary_str(2))
# print(number_to_binary_str(16))
# print(number_to_binary_str(300))
    


def switch_number(number):
    switched = []
    while(number > 10):
        switched.append(number % 10)
        number = int(number /10)
    switched.append(number)

    result = 0
    i = 0
    for num in reversed(switched):
        result += int(num * (10**i))
        i += 1

    return result

def decimal_to_binary_str(decimal):    
    one = False    
    if decimal > 1:
        one = True

    great_number = decimal * (10 ** 10)

    reversed_number = switch_number (great_number)

    if one: reversed_number = int(reversed_number / 10)

    temporalstr = number_to_binary_str(reversed_number)

    originalbinary = temporalstr[::-1]

    if one: originalbinary = "1." + originalbinary
    else: originalbinary = "0." + originalbinary 

    if len(originalbinary) > 32: raise ValueError

    return originalbinary


print(decimal_to_binary_str(0.1234))
print(decimal_to_binary_str(1.123411116))
print(decimal_to_binary_str(1.1234111111))
