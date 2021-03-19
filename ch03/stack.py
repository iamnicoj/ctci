class stack:
    def __init__(self):
        self.list = []
    
    def __len__(self):
        return len(self.list)

    def __str__(self):
        return "".join([str(item) + ' ' for item in self.list])

    def __bool__(self):
        return bool(self.list) 
    
    def __iter__(self):
        return iter(self.list)

    def push(self, item):
        self.list.append(item)
    
    def pop(self):
        return self.list.pop()        

    def peek(self):
        return self.list[len(self.list) - 1]
    

#######

# myStack = stack()

# print(myStack)

# myStack.push(2)    
# myStack.push(3)
# myStack.push(4)
# myStack.push(5)

# print(myStack)

# print(myStack.peek())

# print(myStack.pop())

# print(myStack)

# print(myStack.pop())

# print(myStack)

# print(myStack.pop())

# print(myStack)

# print(myStack.pop())

# print(myStack)

# print(myStack.pop())

# print(myStack)