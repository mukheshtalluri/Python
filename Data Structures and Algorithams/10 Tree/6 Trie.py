class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_string = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_word(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch : node})
            current = node
        current.end_of_string = True
        print("Successfully inserted.")

    def search_string(self, word):
        current = self.root
        for i in word:
            node = current.children.get(i)
            if node == None:
                return False
            current = node
        if current.end_of_string == True:
            return True
        else:
            return False


def delete_string(root_node, word, index):
    ch = word[index]
    current = root_node.children.get(ch)
    can_this_node_be_deleted = False

    if len(current.children) > 1:
        delete_string(current, word, index + 1)
        return False

    if index == len(word) -1:
        if len(current.children) >= 1:
            current.end_of_string = False
            return False
        else:
            root_node.children.pop(ch)
            return True
    if current.end_of_string == True:
        delete_string(current, word, index + 1)
        return False
    can_this_node_be_deleted = delete_string(current, word, index +1)
    if can_this_node_be_deleted == True:
        root_node.children.pop(ch)
        return True
    else:
        return False

new_trie = Trie()
new_trie.insert_word("App")
new_trie.insert_word("Appl")
delete_string(new_trie.root, "App", 0)
print(new_trie.search_string("App"))