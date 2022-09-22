

class Stack():

    def __init__(self):
        self.stack = list()

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]

        else:
            return None

    def _str_(self):
        return str(self.stack)


if __name__ == '__main__':
    my_stack = Stack()
    my_stack.push(3)

    my_stack.push(34)
    my_stack.push(9)

    print(my_stack)
    print(my_stack.pop())