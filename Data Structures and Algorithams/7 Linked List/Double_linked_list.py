class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_linked_list(self):
        result = ""
        temp = self.head
        while temp is not None:
            result += str(temp.value)
            if temp.next is not None:
                result += " <--> "
            temp = temp.next
        return result

    def make_linked_list_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append_value(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def prepend_value(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def pop_last_value(self):
        if self.length == 0:
            return "No items in the linked list to remove."
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None
        self.length -= 1
        return temp

    def pop_first_value(self):
        if self.length == 0:
            return "No items in the linked list to remove."
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        temp.next = None
        self.length -= 1
        return temp

    def get_value(self, index):
        if index < 0 or index >= self.length:
            return "Index out of bound error."
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get_value(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert_value(self, index, value):
        if index < 0 or index > self.length:
            return "Index out of bound of error."
        if index == 0:
            return self.prepend_value(value)
        elif index == self.length:
            return self.append_value(value)
        else:
            new_node = Node(value)
            pre = self.get_value(index - 1)
            temp = self.get_value(index)
            new_node.next = pre.next
            temp.prev = new_node
            new_node.prev = pre
            pre.next = new_node
        self.length += 1

    def delete_value(self, index):
        if index < 0 or index >= self.length:
            return "Index out of bound of error."
        if index == 0:
            return self.pop_first_value()
        elif index == self.length - 1:
            return self.pop_last_value()
        else:
            temp = self.get_value(index)
            temp.next.prev = temp.prev
            temp.prev.next = temp.next
            temp.next = None
            temp.prev = None
        self.length -= 1
        return temp

double_linked_list = DoubleLinkedList(7)
double_linked_list.append_value(16)
double_linked_list.append_value(25)
double_linked_list.append_value(34)
double_linked_list.append_value(43)
double_linked_list.append_value(52)
double_linked_list.append_value(61)
double_linked_list.append_value(70)
double_linked_list.delete_value(7)
print(double_linked_list.print_linked_list())