# Quite not the exact same problem than the book. Mainly for two 
# reasons:
#   1. I don't use the trueLength
#   2. I assum the extra spaces match perfectly with the inner with
#       spaces (well at in a least 2 to 1 ratio) 
#
def URLify(chararray):
    last_empty = len(chararray) -1
    count_spaces = 0
    ready_to_insert = False
    for current in reversed(range(len(chararray))):
        if chararray[current] == ' ':
            if ready_to_insert:
                chararray[last_empty - 2] = '%'
                chararray[last_empty - 1] = '2'
                chararray[last_empty ] = '0'
                last_empty -= 3
                ready_to_insert = False
                count_spaces -= 2
            else:
                count_spaces += 1
        elif chararray[current] != ' ' and count_spaces >= 2:
            chararray[last_empty] = chararray[current]
            chararray[current] = ' '
            last_empty -= 1
            if count_spaces >= 2:
                ready_to_insert = True
            
    return chararray

print(URLify(['a', 'j', 'a', ' ', 'a', 'j', 'a', ' ', 'a', 'j', 'a', ' ', ' ', ' ', ' ']))