import sys

class Stack():
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        return self.stack.pop();
    
    def peek(self):
        return self.stack[len(self.stack) - 1]

    def __len__(self):
        return len(self.stack)
    

def towers_of_hanoi(n):
    first = Stack()
    second = Stack()
    third = Stack()
    counter = 0

    for i in reversed(range(n)):
        first.push(i)

    move_things_around_intelligently(first, second, third)

    # return then all
    return (first, second, third)

def move_things_around_intelligently(first, second, third, floor = sys.maxsize):
    # check if peek/len is not empty in first
    while len(first) > 0 and first.peek() < floor:
        # pop from first to last
        third.push(first.pop())
        if len(first) > 0 and first.peek() < floor:
            # move everything out of second to 1 .. check counter for more efficiente way
            if len(second) > 0 and second.peek() < first.peek():
                move_things_around_intelligently(second, third, first, first.peek())
            # pop everything from thrid to second, 
            second.push(third.pop())
            # move all small from frist to second
            if len(first) > 0 and first.peek() < second.peek():
                move_things_around_intelligently(first, third, second, second.peek())


    if len(second) > 0 and second.peek() < third.peek():
        # if done, move second to third
        move_things_around_intelligently(second, first, third, third.peek())
 

def tests():
    print(towers_of_hanoi(0));
    print(towers_of_hanoi(1));
    print(towers_of_hanoi(2));
    print(towers_of_hanoi(3));
    print(towers_of_hanoi(6));
    print(towers_of_hanoi(1000));


if __name__ == "__main__":
    tests()