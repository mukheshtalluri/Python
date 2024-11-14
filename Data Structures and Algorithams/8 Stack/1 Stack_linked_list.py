class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        for i in range(self.height):
            print(temp.value)
            temp = temp.next

    def push_value(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop_value(self):
        if self.height == 0:
            return "No item in the stack to remove."
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
        self.height -= 1

    def stack_is_empty(self):
        if self.height == 0:
            return True
        return False

    def peek_element(self):
        return self.top.value

    def delete_stack(self):
        self.top = None
        self.height = 0



stack = Stack(7)
stack.push_value(16)
stack.push_value(25)
stack.push_value(34)
stack.push_value(43)
stack.push_value(52)
stack.push_value(61)
stack.push_value(70)
stack.delete_stack()
stack.print_stack()