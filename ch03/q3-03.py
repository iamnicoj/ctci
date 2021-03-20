
# TODO implement a full rebalancing when removing a item from inner
# stack.  
#
class Stack():
    def __init__(self):
        self.stack = []
    
    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return "".join([str(item) + ' ' for item in self.stack])

    def __bool__(self):
        return bool(self.stack) 
    
    def __iter__(self):
        return iter(self.stack)

    def pop(self):
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)
    
    def peek(self):
        return self.stack[len(self.stack) - 1]

        
class SetOfStacks(Stack):
    def __init__(self, max_size):
        self.stack_list = [Stack()]
        self.current_stack = 0
        self.max_size = max_size

    def __str__(self):
        val =  ""        
        for ministack in self.stack_list:
            val += "::"
            val += str(ministack)
        
        return val

    
    def pop(self):
        item = self.stack_list[self.current_stack].pop()
        if len(self.stack_list[self.current_stack]) == 0:
            self.current_stack -= 1
        return item        

    def pop_index(self, stack):
        if self.current_stack < stack: return None

        item = self.stack_list[stack].pop()
        return item        
    
    def push(self, item):
        if self.max_size == len(self.stack_list[self.current_stack]):
            self.stack_list.append(Stack())
            self.current_stack += 1;
        self.stack_list[self.current_stack].push(item)
    
    def peek(self):
        return self.stack_list[self.current_stack].peek()
    
mySOSs = SetOfStacks(3)

mySOSs.push(1)
mySOSs.push(2)
mySOSs.push(3)
mySOSs.push(4)
mySOSs.push(5)
mySOSs.push(6)
mySOSs.push(1)
mySOSs.push(2)
mySOSs.push(3)
mySOSs.push(4)
mySOSs.push(5)
mySOSs.push(6)

print(mySOSs)

print(mySOSs.pop())
print(mySOSs)

print(mySOSs.pop())
print(mySOSs)
print(mySOSs.pop())
print(mySOSs)
print(mySOSs.pop())
print(mySOSs)
print(mySOSs.pop())
print(mySOSs)
print(mySOSs.pop())
print(mySOSs)
print(mySOSs.pop())
print(mySOSs)

mySOSs.push(2)
mySOSs.push(3)
mySOSs.push(4)
mySOSs.push(5)
mySOSs.push(6)

print(mySOSs)

print(mySOSs.pop_index(0))
print(mySOSs)