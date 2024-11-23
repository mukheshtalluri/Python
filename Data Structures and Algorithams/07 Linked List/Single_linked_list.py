from types import new_class


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SingleLinkedList:
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
                result += " --> "
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
            self.tail = new_node
        self.length += 1

    def prepend_value(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_last_value(self):
        if self.length == 0:
            return "No elements in the linked list."
        pre = self.head
        temp = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        return temp.value

    def pop_first_value(self):
        if self.length == 0:
            return "No elements in the linked list."
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length -= 1
        return temp.value

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
            return "Index out of bound error."
        if index == 0:
            return self.prepend_value(value)
        elif index == self.length:
            return self.append_value(value)
        else:
            new_node = Node(value)
            pre = self.get_value(index - 1)
            temp = self.get_value(index)
            new_node.next = pre.next
            pre.next = new_node
        self.length += 1

    def delete_node(self, index):
        if index < 0 or index > self.length:
            return "Index out of bound error."
        if index == 0:
            return self.pop_first_value()
        elif index == self.length:
            return self.pop_last_value()
        else:
            pre = self.get_value(index - 1)
            temp = self.get_value(index)
            pre.next = temp.next
            temp.next = None
        self.length -= 1
        return temp.value

    def reverse_linkedlist(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

if __name__ == "__main__":
    single_linked_list = SingleLinkedList(7)
    single_linked_list.append_value(16)
    single_linked_list.append_value(25)
    single_linked_list.append_value(34)
    single_linked_list.append_value(43)
    single_linked_list.append_value(52)
    single_linked_list.append_value(61)
    single_linked_list.append_value(70)
    single_linked_list.reverse_linkedlist()
    print(single_linked_list.print_linked_list())
