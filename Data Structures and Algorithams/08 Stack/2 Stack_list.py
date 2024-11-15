class Stack:
    def __init__(self):
        self.values = []

    def print_stack(self):
        for val in reversed(range(len(self.values))):
            print(self.values[val])

    def push_value(self, value):
        return self.values.append(value)

    def pop_value(self):
        return self.values.pop()

    def stack_is_empty(self):
        if len(self.values) == 0:
            return True
        return False

    def peek_element(self):
        return self.values[len(self.values) - 1]


stack = Stack()
stack.push_value(7)
stack.push_value(16)
stack.push_value(25)
stack.push_value(34)
stack.push_value(43)
stack.push_value(52)
stack.push_value(61)
stack.push_value(70)
stack.pop_value()
stack.pop_value()
stack.pop_value()
print(stack.peek_element())
print(stack.stack_is_empty())
stack.print_stack()


