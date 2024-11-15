class Queue:
    def __init__(self):
        self.values = []

    def enqueue_value(self, value):
        return self.values.append(value)

    def print_queue(self):
        for val in range(len(self.values)):
            print(self.values[val], end = " ")

    def dequeue_value(self):
        return self.values.pop(0)

    def queue_is_empty(self):
        if len(self.values) == 0:
            return True
        return False

queue = Queue()
queue.enqueue_value(7)
queue.enqueue_value(16)
queue.enqueue_value(25)
queue.enqueue_value(34)
queue.enqueue_value(43)
queue.enqueue_value(52)
queue.enqueue_value(61)
queue.enqueue_value(70)
queue.dequeue_value()
queue.print_queue()



