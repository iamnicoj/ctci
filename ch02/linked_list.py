class node:
    def __init__(self, data):
        self.item = data
        self.next = None

class linked_list:

    count = 0

    def __init__(self):
        self.head = None
        self.count = 0

    def add(self, element):
        if(self.head is None):
            self.head = node(element)
        else:
            temp =  node(element)
            temp.next = self.head
            self.head = temp
        self.count += 1

    def get(self, data):
        temp = self.head
        while temp is not None:
            if temp.item == data:
                return temp.item
            temp = temp.next
    
    def remove(self, data):
        if self.head is None: 
        elif self.head.item == data:
            self.head = self.head.next
            self.count -= self.count
            return
        
        current = self.head.next
        past = self.head

        # keep track of current and past item
        while current is not None:            
            if current.item == data:
                past.next = current.next
                self.count -= self.count
                return;
            past = current
            current = current.next;
    
    def reverse(self):
        return;
    
    def bubblesort(self):
        for i in range(self.count):
            current = self.head
            while current is not None and current.next is not None:
                if current.item > current.next.item:
                    temp = current.item
                    current.item = current.next.item
                    current.next.item = temp
                current = current.next
            i += i

    def reverse(self):
        current = self.head
        queue = []
        while current is not None:
            queue.append(current.item)            
            current = current.next

        self.head = None

        while(len(queue) > 0):
            item = queue.pop(0)
            self.add(item)

    def print_list (self):
        temp = self.head
        while temp is not None:
            print(temp.item)
            temp = temp.next

