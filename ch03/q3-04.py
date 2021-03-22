
from stack import stack
class MyQueue():
    def __init__(self):
        self.queue_stack = stack() 
        self.unqueue_stack = stack() 

    def queue(self, item):
        self.queue_stack.push(item)
    

    def enqueue(self):
        try:
            value = self.unqueue_stack.pop()
        except IndexError:
            can_iterate = True            
            while can_iterate:
                try:
                    temp = self.queue_stack.pop()
                    self.unqueue_stack.push(temp)
                
                except IndexError:
                    can_iterate = False
                        
            value = self.unqueue_stack.pop()
        return value

myq = MyQueue()
myq.queue(1)
print(myq.enqueue())


myq = MyQueue()
myq.queue(1)
myq.queue(2)
myq.queue(3)
myq.queue(4)
print(myq.enqueue())
print(myq.enqueue())
myq.queue(5)
myq.queue(6)
myq.queue(7)
myq.queue(8)
print(myq.enqueue())
print(myq.enqueue())
print(myq.enqueue())
print(myq.enqueue())
print(myq.enqueue())
print(myq.enqueue())