from Queue import Queue
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

binary_tree = BinaryTree("Drinks")
cold = BinaryTree("Cold")
hot = BinaryTree("Hot")
binary_tree.left_child = cold
binary_tree.right_child = hot
cola = BinaryTree("Cola")
fanta = BinaryTree("Fanta")
cold.left_child = cola
cold.right_child = fanta
coffee = BinaryTree("Coffee")
tea = BinaryTree("Tea")
hot.left_child = coffee
hot.right_child = tea

def pre_order_traverse(root_node):
    if not root_node:
        return
    print(root_node.data)
    pre_order_traverse(root_node.left_child)
    pre_order_traverse(root_node.right_child)

def in_order_traverse(root_node):
    if not root_node:
        return
    in_order_traverse(root_node.left_child)
    print(root_node.data)
    in_order_traverse(root_node.right_child)

def post_order_traverse(root_node):
    if not root_node:
        return
    post_order_traverse(root_node.left_child)
    post_order_traverse(root_node.right_child)
    print(root_node.data)

def level_order_traverse(root_node):
    if not root_node:
        return
    else:
        custom_queue = Queue()
        custom_queue.enqueue_value(root_node)
        while not custom_queue.queue_is_empty():
            root = custom_queue.dequeue_value()
            print(root.value.data)
            if root.value.left_child is not None:
                custom_queue.enqueue_value(root.value.left_child)
            if root.value.right_child is not None:
                custom_queue.enqueue_value(root.value.right_child)

def search_value(root_node, value):
    if not root_node:
        return
    else:
        custom_queue = Queue()
        custom_queue.enqueue_value(root_node)
        while not custom_queue.queue_is_empty():
            root = custom_queue.dequeue_value()
            if root.value.data == value:
                return "Value found"
            if root.value.left_child is not None:
                custom_queue.enqueue_value(root.value.left_child)
            if root.value.right_child is not None:
                custom_queue.enqueue_value(root.value.right_child)
        return "Value not found"

def insert_value(root_node, new_value):
    if not root_node:
        root_node = new_value
    else:
        custom_queue = Queue()
        custom_queue.enqueue_value(root_node)
        while not custom_queue.queue_is_empty():
            root = custom_queue.dequeue_value()
            if root.value.left_child is not None:
                custom_queue.enqueue_value(root.value.left_child)
            else:
                root.value.left_child = new_value
                return "Value is inserted successfully."
            if root.value.right_child is not None:
                custom_queue.enqueue_value(root.value.right_child)
            else:
                root.value.right_child = new_value
                return "Value is inserted successfully."

def get_deep_node(root_node):
    if not root_node:
        return
    else:
        custom_queue = Queue()
        custom_queue.enqueue_value(root_node)
        while not custom_queue.queue_is_empty():
            root = custom_queue.dequeue_value()
            if root.value.left_child is not None:
                custom_queue.enqueue_value(root.value.left_child)
            if root.value.right_child is not None:
                custom_queue.enqueue_value(root.value.right_child)
        deep_node = root.value
        return deep_node

def delete_deep_node(root_node, deep_node):
    if not root_node:
        return
    else:
        custom_queue = Queue()
        custom_queue.enqueue_value(root_node)
        while not custom_queue.queue_is_empty():
            root = custom_queue.dequeue_value()
            if root.value.data is deep_node:
                root.value.data = None
                return
            if root.value.left_child:
                if root.value.left_child is deep_node:
                    root.value.left_child = None
                    return
                else:
                    custom_queue.enqueue_value(root.value.left_child)
            if root.value.right_child:
                if root.value.right_child is deep_node:
                    root.value.right_child = None
                    return
                else:
                    custom_queue.enqueue_value(root.value.right_child)

def delete_node(root_node, node):
    if not root_node:
        return "The binary tree is does not exists."
    else:
        custom_queue = Queue()
        custom_queue.enqueue_value(root_node)
        while not custom_queue.queue_is_empty():
            root = custom_queue.dequeue_value()
            if root.value.data == node:
                deep_node = get_deep_node(root_node)
                root.value.data = deep_node.data
                delete_deep_node(root_node, deep_node)
                return "The node is deleted successfully."
            if root.value.left_child is not None:
                custom_queue.enqueue_value(root.value.left_child)
            if root.value.right_child is not None:
                custom_queue.enqueue_value(root.value.right_child)

def delete_binary_tree(root_node):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return "The binary tree is deleted successfully."

delete_binary_tree(binary_tree)
print(level_order_traverse(binary_tree))