def string_compression(string):
    result = ""
    i = 0
    while i < len(string):
        count = 1
        anchor = string[i]
        j = i + 1
        while j < len(string) and anchor == string[j]:
            count += 1    
            j += 1        
        result = "".join([result, string[i] , str(count)])
        i = j
        if len(result) > len(string):
            return string
    return result

print(string_compression("helllllooooowwwwwwworld"))                
print(string_compression("aaasssdddfffgghjjkll"))                