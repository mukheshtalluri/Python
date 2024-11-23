class BinaryTree:
    def __init__(self, size):
        self.custom_list = size * [None]
        self.last_used_index = 0
        self.max_size = size

    def insert_node(self, value):
        if self.last_used_index + 1 == self.max_size:
            return "The binary tree is full."
        self.custom_list[self.last_used_index + 1] = value
        self.last_used_index += 1
        return "The value inserted successfully."

    def search_node(self, value):
        for i in range(len(self.custom_list)):
            if self.custom_list[i] == value:
                return "Value found"
        return "Value not found"

    def pre_order_traverse(self, index):
        if index > self.last_used_index:
            return
        print(self.custom_list[index])
        self.pre_order_traverse(index * 2)
        self.pre_order_traverse(index * 2 + 1)

    def in_order_traverse(self, index):
        if index > self.last_used_index:
            return
        self.in_order_traverse(index * 2)
        print(self.custom_list[index])
        self.in_order_traverse(index * 2 + 1)

    def post_order_traverse(self, index):
        if index > self.last_used_index:
            return
        self.post_order_traverse(index * 2)
        self.post_order_traverse(index * 2 + 1)
        print(self.custom_list[index])

    def level_order_traverse(self, index):
        for i in range(index, self.last_used_index + 1):
            print(self.custom_list[i])

    def delete_node(self, value):
        if self.last_used_index == 0:
            return "No nodes in linked list to delete."
        for i in range(1, self.last_used_index + 1):
            if self.custom_list[i] == value:
                self.custom_list[i] = self.custom_list[self.last_used_index]
                self.custom_list[self.last_used_index] = None
                self.last_used_index -= 1
                return "The node is successfully deleted."

    def delete_binary_tree(self):
        self.custom_list = None
        return "The binary tree is successfully deleted."

binary_tree = BinaryTree(8)
binary_tree.insert_node("Drinks")
binary_tree.insert_node("Hot")
binary_tree.insert_node("Cold")
binary_tree.insert_node("Coffee")
binary_tree.insert_node("Tea")
binary_tree.insert_node("Cola")
binary_tree.insert_node("Fanta")
binary_tree.pre_order_traverse(1)



