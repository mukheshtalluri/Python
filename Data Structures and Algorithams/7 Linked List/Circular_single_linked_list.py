class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularSingleLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        new_node.next = new_node
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_linked_list(self):
        result = ""
        temp = self.head
        while temp is not None:
            result += str(temp.value)
            temp = temp.next
            if temp == self.head:
                break
            result += " --> "
        return result

    def append_value(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepend_value(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node
        self.length += 1

    def pop_last_value(self):
        if self.length == 0:
            return "No elements in linked list to remove."
        temp = self.tail
        pre = self.tail
        while temp.next is not self.head:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = self.head
        self.length -= 1
        return temp






circular_single_linked_list = CircularSingleLinkedList(7)
circular_single_linked_list.append_value(16)
circular_single_linked_list.append_value(25)
circular_single_linked_list.pop_last_value()
print(circular_single_linked_list.print_linked_list())