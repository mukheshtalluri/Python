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
        temp = self.head
        while temp.next is not self.tail:
            temp = temp.next
        temp.next = None
        self.tail = temp
        self.length -= 1
        return temp

    def pop_first_value(self):
        if self.length == 0:
            return "No elements in linked list to remove."
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.tail.next = self.head
        self.length -= 1
        return temp

    def get_value(self, index):
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get_value(index)
        if temp:
            temp.value = value
            return True
        return  False

    def insert_value(self, index, value):
        if index < 0 or index > self.length:
            return "Index out of bound."
        elif index == 0:
            return self.prepend_value(value)
        elif index == self.length:
            return self.append_value(value)
        else:
            new_node = Node(value)
            pre = self.get_value(index - 1)
            new_node.next = pre.next
            pre.next =  new_node
        self.length += 1










circular_single_linked_list = CircularSingleLinkedList(7)
circular_single_linked_list.append_value(16)
circular_single_linked_list.append_value(25)
circular_single_linked_list.append_value(34)
circular_single_linked_list.append_value(43)
circular_single_linked_list.append_value(52)
circular_single_linked_list.append_value(61)
circular_single_linked_list.append_value(70)
circular_single_linked_list.insert_value(3, 1)
print(circular_single_linked_list.print_linked_list())