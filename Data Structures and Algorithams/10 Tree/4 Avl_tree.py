from Queue import Queue
class AVLTree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1
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
        if root_node.left_child == value:
            return "The value found."
        else:
            search_value(root_node.left_child, value)
    else:
        if root_node.right_child == value:
            return "The value found."
        else:
            search_value(root_node.right_child, value)

def get_height(root_node):
    if not root_node:
        return 0
    return root_node.height

def left_rotate(disbalance_node):
    new_root = disbalance_node.right_child
    disbalance_node.right_child = disbalance_node.right_child.left_child
    new_root.left_child = disbalance_node
    disbalance_node.height = 1 + max(get_height(disbalance_node.left_child), get_height(disbalance_node.right_child))
    new_root.height = 1 + max(get_height(new_root.left_child), get_height(new_root.right_child))
    return new_root

def right_rotate(disbalance_node):
    new_root = disbalance_node.left_child
    disbalance_node.left_child = disbalance_node.left_child.right_child
    new_root.right_child = disbalance_node
    disbalance_node.height = 1 + max(get_height(disbalance_node.left_child), get_height(disbalance_node.right_child))
    new_root.height = 1 + max(get_height(new_root.left_child), get_height(new_root.right_child))
    return new_root

def get_balance(root_node):
    if not root_node:
        return 0
    return get_height(root_node.left_child) - get_height(root_node.right_child)

def insert_node(root_node, value):
    if not root_node:
        return AVLTree(value)
    elif value < root_node.data:
        root_node.left_child = insert_node(root_node.left_child, value)
    else:
        root_node.right_child = insert_node(root_node.right_child, value)

    root_node.height = 1 + max (get_height(root_node.left_child), get_height(root_node.right_child))
    balance = get_balance(root_node)
    if balance > 1 and value < root_node.left_child.data:
        return right_rotate(root_node)
    if balance > 1 and value > root_node.left_child.data:
        root_node.left_child = left_rotate(root_node.left_child)
        return right_rotate(root_node)
    if balance < -1 and value > root_node.right_child.data:
        return left_rotate(root_node)
    if balance < -1 and value < root_node.right_child.data:
        root_node.right_child = right_rotate(root_node.right_child)
        return left_rotate(root_node)
    return root_node

def min_value(root_node):
    if root_node or root_node.left_child is None:
        return root_node
    return min_value(root_node.left_child)

def delete_node(root_node, value):
    if not root_node:
        return root_node
    elif value < root_node.data:
        root_node.left_child = delete_node(root_node.left_child, value)
    elif value > root_node.data:
        root_node.right_child = delete_node(root_node.right_child, value)
    else:
        if root_node.left_child is None:
            temp = root_node.right_child
            root_node = None
            return temp
        elif root_node.right_child is None:
            temp = root_node.left_child
            root_node = None
            return temp
        temp = min_value(root_node.right_node)
        root_node.data = temp.data
        root_node.right_child = delete_node(root_node.right_child, temp.data)
        balance = get_balance(root_node)
        if balance > 1 and value < root_node.left_child.data:
            return right_rotate(root_node)
        if balance > 1 and value > root_node.left_child.data:
            root_node.left_child = left_rotate(root_node.left_child)
            return right_rotate(root_node)
        if balance < -1 and value > root_node.right_child.data:
            return left_rotate(root_node)
        if balance < -1 and value < root_node.right_child.data:
            root_node.right_child = right_rotate(root_node.right_child)
            return left_rotate(root_node)
        return root_node

def delete_tree(root_node):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return "The AVL tree is deleted successfully."




avl_tree = AVLTree(20)
avl_tree = insert_node(avl_tree, 30)
avl_tree = insert_node(avl_tree, 40)
avl_tree = insert_node(avl_tree, 50)
avl_tree = insert_node(avl_tree, 60)
avl_tree = insert_node(avl_tree, 70)
avl_tree = insert_node(avl_tree, 80)

level_order_traverse(avl_tree)



