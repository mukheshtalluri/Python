class Node:
    def __init__(self, value = 0):
        self.value = value
        self.next = None
    def __str__(self):
        values = []
        temp = self
        while temp:
            values.append(str(temp.value))
            temp = temp.next
        return " --> ".join(values)

def create_linked_list(values):
    temp = current = Node()
    for value in values:
        current.next = Node(value)
        current = current.next
    return temp.next

# Merge two sorted linked list or Merge two linked list in ascending order
def merge_linkedlist(l1, l2):
    temp = current = Node()
    while l1 and l2:
        if l1.value <= l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    if l1:
        current.next = l1
    else:
        current.next = l2
    return temp.next

# Remove duplicates from the linked list
def remove_duplicates(head):
    current = head
    while current and current.next:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next
    return head

# Remove element from the linked list
def remove_element(head, element):
    current = head
    while current.next:
        if current.next.value == element:
            current.next = current.next.next
        else:
            current = current.next
    return head

# Reverse linked list
def reverse_linkedlist(head):
    curr_node = head
    prev_node = None
    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    return prev_node

# Palindrome linked list
def palindrome_linkedlist(head : Node()):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
    while prev:
        if head.value != prev.value:
            return False
        head = head.next
        prev = prev.next
    return True

# Middle element in the linked list
def middle_element_in_linkedlist(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.value


list_of_values_1 = [2, 4, 6, 8, 10, 12]
list_of_values_2 = [3, 6, 9, 12, 15, 18]
list_of_values_3 = [1, 2, 3, 2, 1]
linkedlist_1 = create_linked_list(list_of_values_1)
linkedlist_2 = create_linked_list(list_of_values_2)
linkedlist_3 = create_linked_list(list_of_values_3)
print(middle_element_in_linkedlist(linkedlist_3))


        
    