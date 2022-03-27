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

    def search(self, headToSearch):
        if self.root == None:
            return "Tree is empty"
        else:
            current_node = self.root
            while True:
                if current_node == None:
                    return "Not Found"
                if current_node.head == headToSearch:
                    return "Found"
                elif current_node.head > headToSearch:
                    current_node = current_node.left
                elif current_node.head < headToSearch:
                    current_node = current_node.right

    def remove(self, headToRemove):
        if self.root == None:
            return "Tree is empty"

        current_node = self.root
        parent_node = None
        while current_node != None:
            if current_node.head > headToRemove:
                parent_node = current_node
                current_node = current_node.left
            elif current_node.head < headToRemove:
                parent_node = current_node
                current_node = current_node.right
            else:
                # Node has left child only
                if current_node.right == None:
                    if parent_node == None:
                        self.root = current_node.left
                        return
                    else:
                        if parent_node.head > current_node.head:
                            parent_node.left = current_node.left
                            return
                        else:
                            parent_node.right = current_node.left
                            return

                # Node has right child only
                elif current_node.left == None:
                    if parent_node == None:
                        self.root = current_node.right
                        return
                    else:
                        if parent_node.head > current_node.head:
                            parent_node.left = current_node.right
                            return
                        else:
                            parent_node.right = current_node.right
                            return

                # Node has neither left nor right child
                elif current_node.left == None and current_node.right == None:
                    if parent_node == None:
                        current_node = None
                        return
                    if parent_node.head > current_node.head:
                        parent_node.left = None
                        return
                    else:
                        parent_node.right = None
                        return

                # Node has both left and right child
                elif current_node.left != None and current_node.right != None:
                    del_node = current_node.right
                    del_node_parent = current_node.right
                    while del_node.left != None:
                        del_node_parent = del_node
                        del_node = del_node.left
                    current_node.head = del_node.head
                    if del_node == del_node_parent:
                        current_node.right = del_node.right
                        return
                    if del_node.right == None:
                        del_node_parent.left = None
                        return
                    else:
                        del_node_parent.left = del_node.right
                        return
        return "Not found"
