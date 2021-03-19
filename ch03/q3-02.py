from stack import stack

class min_stack(stack):
    def __init__(self):
        super().__init__()
        self.minima = stack()    # This could've been a stack itself
    
    def min(self):
        if len(self.list) > 0:
            return self.list[self.minima.peek()]
        return None

    def push(self, item):
        super().push(item)

        if len(self.minima) == 0:
            self.minima.push(0)
            return
        
        minvalue = self.min()

        if item < minvalue:
            self.minima.push(len(self.minima))
        else:
            self.minima.push(self.minima.peek())


    def pop(self):
        self.minima.pop()
        return super().pop()        
    

#############################
mystack = min_stack()

mystack.push(2)
mystack.push(1)
mystack.push(33)
mystack.push(5)
mystack.push(0)

print(mystack)
print(mystack.pop())
print(mystack)
print(mystack.min())
