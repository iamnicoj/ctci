# Option to have flexible divisions and a way to move stacks around
# array manage as a circular object
# moving indexes allow for flexibility when pushing

class stack:
    def __init__(self, head, tail, arraysize):
        self.head = head
        self.tail = tail
        self.arraysize = arraysize

# TODO: Refactor to use modular class
# TODO: Refactor to use dynamic number of stacks

class moving_stacks:
    def __init__(self, size):
        self.array = [0 for _ in range(size)]
        self.stack1head = 0
        self.stack2head = int(size*(1/3))
        self.stack3head = int(size*(2/3))
        self.stack1end = self.stack1head
        self.stack2end = self.stack3head
        self.stack3end = self.stack3head
        self.edgecase = len(array) * -1
    
    def push(self, stack, object):
        if self._is_stack_full(): raise ValueError()
        
        if _can_push(stack) == False:
            if _can_push(_next_stack(stack)) == False:
                self._move_stack(_next_stack(stack)
            else:
                self._move_stack(_next_stack(_next_stack(stack)))
                self._move_stack(_next_stack(stack))

        if stack == 1:        
            if stack1end < len(self.array) - 1 
                stack1end += 1
            else
                stack1end = 0

            self.array[stack1end] = object

        if stack == 2:        
            if stack2end < len(self.array) - 1 
                stack2end += 1
            else
                stack1end = 0

            self.array[stack2end] = object

        if stack == 3:        
            if stack3end < len(self.array) - 1 
                stack3end += 1
            else
                stack3end = 0

            self.array[stack3end] = object

    def _next_stack(stack):
        if stack == 1: return 2
        elif stack == 2: return 3
        else: return 1


    def _can_push(self, stack):
        if stack == 1 and self.stack2head - self.stack1end == 1 or self.stack2head - self.stack1end == self.edgecase: return False
        elif stack == 2 and self.stack3head - self.stack2end == 1 or self.stack3head - self.stack2end == self.edgecase: return False
        elif stack == 3 and self.stack1head - self.stack3end == 1 or self.stack1head - self.stack3end == self.edgecase: return False

        return True
    
    def _move_stack(self, stack):
        stack_size = self._stack_size(stack)
        for i in reversed(range(stack_size)):
            self._move_object(stack, i)
        self._move_indexes(stack)
        
    def _move_object(self, stack, i):
        if stack == 1:
            arrayposition = self.stack1head + i - 1
        elif stack == 2:
            arrayposition = self.stack2head + i - 1
        else:
            arrayposition = self.stack3head + i - 1

        if arrayposition >= len(self.array): arrayposition -= len(self.array)
        
        newarrayposition = arrayposition + 1

        if newarrayposition >= len(self.array): newarrayposition -= len(self.array)
        
        self.array[newarrayposition] = self.array[arrayposition]


    def _move_indexes(self, stack):
        if stack == 1:
            self.stack1head += 1
            if self.stack1head >= len(self.array): self.stack1head = 0
            self.stack1end += 1
            if self.stack1end >= len(self.array): self.stack1end = 0
            
        elif stack == 2:
            self.stack2head += 1
            if self.stack2head >= len(self.array): self.stack2head = 0
            self.stack2end += 1
            if self.stack2end >= len(self.array): self.stack2end = 0

        else:
            self.stack3head += 1
            if self.stack3head >= len(self.array): self.stack3head = 0
            self.stack3end += 1
            if self.stack3end >= len(self.array): self.stack3end = 0



    def _stack_size(self, stack)
        if stack ==1:
            if self.stack1end >= self.stack1head: return self.stack1end - self.stack1head + 1
            return self.stack1end + len(self.array) - self.stack1head + 1
        elif stack ==2:
            if self.stack2end >= self.stack2head: return self.stack2end - self.stack2head + 1
            return self.stack2end + len(self.array) - self.stack2head + 1
        else:
            if self.stack3end >= self.stack3head: return self.stack3end - self.stack3head + 1
            return self.stack3end + len(self.array) - self.stack3head + 1


    def _is_stack_full(self):
        if (self.stack2head - self.stack1end == 1 and self.stack3head - self.stack2end == 1 and self.stack1head - self.stack3end == 1) or (self.stack2head - self.stack1end == self.edgecase and self.stack3head - self.stack2end == self.edgecase and self.stack1head - self.stack3end == self.edgecase)
            return True
        return False
    
    def peek(self, stack):
        if stack == 1: return self.array[self.stack1end]
        elif stack == 2: return self.array[self.stack2end]
        else: return self.array[self.stack3end]
    
    def pop(self, stack):
        if stack == 1: 
            result = self.array[self.stack1end]
            if self.stack1end == 0:
                self.stack1end = len(self.array) - 1
        elif stack == 2: 
            result = self.array[self.stack2end]
                self.stack2end = len(self.array) - 1
        else: 
            result = self.array[self.stack3end]
                self.stack3end = len(self.array) - 1

        return result
    

# Add test cases



