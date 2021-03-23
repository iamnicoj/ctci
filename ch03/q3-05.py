from stack import stack


def sort_stack(mystack):
    order_stack = stack()
    temp = None

    while len(mystack) > 0:
        temp = mystack.pop()

        if len(order_stack) == 0 or order_stack.peek() < temp:
            order_stack.push(temp)
        else:
            while len(order_stack) > 0 and order_stack.peek() > temp:
                mystack.push(order_stack.pop())
            order_stack.push(temp)

    while len(order_stack) > 0:
        mystack.push(order_stack.pop())


def tests():
    mystack = stack()
    mystack.push(44)
    mystack.push(4)
    mystack.push(5)
    mystack.push(51)
    mystack.push(8)
    mystack.push(9)
    mystack.push(11)
    print(mystack)

    sort_stack(mystack)
    print(mystack)
    print(mystack.pop())

if __name__ == "__main__":
    tests()