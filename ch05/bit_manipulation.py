def setbit(num, i):
    return num | (1 << i)

def getbit(num,i):
    return (num & (1 << i)) != 0

def clearbit(num, i):
    mask = ~(1 << i) 
    return num & mask

def clearMStoI(num, i):
    mask = (1 << i) - 1
    return num & mask

def clearIto0(num, i):
    mask = (-1 << i)
    return num & mask

def printbinary(num):
    print("{0:b}".format(num))

def updatebit(num, bit, i):
    value = 1 if bit == True else 0
    mask =  ~(1 << i)
    return num & mask | value << i