## Is power of 2
def debugger(n):
    return (n & (n-1) == 0)


for num in range(-5, 515):
    if debugger(num):
        print(num)