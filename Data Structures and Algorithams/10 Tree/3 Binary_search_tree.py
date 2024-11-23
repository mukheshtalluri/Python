from Queue import Queue
class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

def insert_node(root_node, value):
    if root_node.data is None:
        root_node.data = value
    elif value <= root_node.data:
        if root_node.left_child is None:
            root_node.left_child = BinarySearchTree(value)
        else:
            insert_node(root_node.left_child, value)
    else:
        if root_node.right_child is None:
            root_node.right_child = BinarySearchTree(value)
        else:
            insert_node(root_node.right_child, value)

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
    if root_node.data == value:
        return "The value found."
    elif value < root_node.data:
        if root_node.left_child.data == value:
            return "The value found."
        else:
            search_value(root_node.left_child, value)
    else:
        if root_node.right_child.data == value:
            return "The value found."
        else:
            search_value(root_node.right_child, value)

def min_value(root_node):
    current_node = root_node
    while current_node.left_child is not None:
        current_node = current_node.left_child
    return current_node

def delete_node(root_node, value):
    if root_node is None:
        return root_node
    if value < root_node.data:
        root_node.left_child = delete_node(root_node.left_child, value)
    elif value > root_node.data:
        root_node.right_child = delete_node(root_node.right_child, value)
    else:
        if root_node.left_child is None:
            temp = root_node.right_child
            root_node = None
            return temp
        if root_node.right_child is None:
            temp = root_node.left_child
            root_node = None
            return temp
        temp = min_value(root_node.right_child)
        root_node.data = temp.data
        root_node.right_child = delete_node(root_node.right_child, temp.data)
    return root_node

def delete_binary_search_tree(root_node):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return "The binary tree is successfully deleted."

binary_search_tree = BinarySearchTree(70)
insert_node(binary_search_tree, 50)
insert_node(binary_search_tree, 90)
insert_node(binary_search_tree, 40)
insert_node(binary_search_tree, 60)
insert_node(binary_search_tree, 80)
insert_node(binary_search_tree, 100)
delete_node(binary_search_tree, 70)
level_order_traverse(binary_search_tree)



