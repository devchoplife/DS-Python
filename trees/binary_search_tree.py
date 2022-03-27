class Node():
    def __init__(self, data):
        self.head = data
        self.left = None
        self.right = None


class BST():
    def __init__(self):
        self.root = None
        self.node_size = 0

    # The complexity is O(log N) in avg case and O(n) in worst case.
    def insert(self, head):
        new_node = Node(head)
        if self.root == None:
            self.root = new_node
            self.node_size += 1
            return
        else:
            current_node = self.root
            while(current_node.left != new_node) and (current_node.right != new_node):
                if new_node.head > current_node.head:
                    if current_node.right == None:
                        current_node.right = new_node
                    else:
                        current_node = current_node.right
                elif new_node.head < current_node.head:
                    if current_node.left == None:
                        current_node, left = new_node
                    else:
                        current_node = current_node.left
            self.node_size += 1
            return
