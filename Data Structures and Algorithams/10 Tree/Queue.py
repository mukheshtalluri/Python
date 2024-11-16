class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def print_queue(self):
        result = ""
        temp = self.first
        while temp is not None:
            result += str(temp.value)
            if temp.next is not None:
                result += " --> "
            temp = temp.next
        return result

    def enqueue_value(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue_value(self):
        if self.length == 0:
            return "No elements in the queue to remove"
        else:
            temp = self.first
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

    def queue_is_empty(self):
        if self.length == 0:
            return True
        return False

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue_value(7)
    queue.enqueue_value(16)
    queue.enqueue_value(25)
    queue.dequeue_value()
    print(queue.print_queue())



