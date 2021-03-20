def number_to_binary_str(number):    
    if number == 0: return "0"

    result = ''

    while number > 1:
        flag = number % 2
        result = str(flag) + result
        number = number // 2;

    result = str(number) + result

    return result


# print(number_to_binary_str(0))
# print(number_to_binary_str(1))
# print(number_to_binary_str(2))
# print(number_to_binary_str(16))
# print(number_to_binary_str(300))

####################

def switch_number(number):
    switched = []
    while(number > 10):
        switched.append(number % 10)
        number = number // 10
    switched.append(number)

    result = 0
    i = 0
    for num in reversed(switched):
        result += int(num * (10**i))
        i += 1

    return result

#########

def decimal_to_binary_str(decimal):    
    one = False    
    if decimal > 1:
        one = True

    # TODO this is not precise 
    great_number = decimal * (10 ** 10)
    reversed_number = switch_number (great_number)

    if one: reversed_number = reversed_number // 10

    temporalstr = number_to_binary_str(reversed_number)
    originalbinary = temporalstr[::-1]

    if one: originalbinary = "1." + originalbinary
    else: originalbinary = "0." + originalbinary 

    if len(originalbinary) > 32: raise ValueError

    return originalbinary


####
print('My answer')

print(decimal_to_binary_str(0.95))
print(decimal_to_binary_str(1.123411116))
try:
    print(decimal_to_binary_str(1.1234111111))
except ValueError:
    print('ValueError')


##############


# Official answer
def printBinary(double):
    if double >= 1 or double < 0:
        raise ValueError

    binary = '.'

    while double > 0:
        if len(binary) > 32: 
            return binary
        
        r = double * 2 
        if r >= 1:
            binary += '1'
            double = r - 1
        else:
            binary += '0'
            double = r
    return binary

print('Official answer?')
print(printBinary(0.95))
print(printBinary(0.123411116))
try:
    print(printBinary(0.1234111111))
except ValueError:
    print('ValueError')
