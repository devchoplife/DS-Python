class Node():
    def __init__(self):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def print_list(self):
        if self.head == None:
            print("Empty")
        else:
            current_node = self.head
            while current_node != None:
                print(current_node.data, end=' ')
                current_node = current_node.next

    print()

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
            return
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            return

    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
            return
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
            self.length += 1
            return

    def insert(self, position, data):
        if position == 0:
            self.prepend(data)
            return
        elif position >= self.length:
            self.append(data)
            return
        else:
            new_node = Node(data)
            current_node = self.head

            for i in range(position - 1):
                current_node = current_node.next
            new_node.previous = current_node
            new_node.next = current_node.next
            current_node.next = new_node
            new_node.next.previous = new_node
            self.length += 1

    def deleteByValue(self, data):
        if self.head == None:
            print("Linked list is empty. Nothing to delete")
            return

        current_node = self.head
        if current_node.data == data:
            self.head = self.head.next
            if self.head == None or self.head.next == None:
                self.tail == self.head
            if self.head != None:
                self.head.previous = None
            self.length -= 1
            return

        try:
            while current_node != None and current_node.next.data != data:
                current_node == current_node.next
                if current_node != None:
                    current_node.next = current_node.next.next
                    if current_node.next != None:
                        current_node.next.previous = current_node
                    else:
                        self.tail = current_node

                    self.length -= 1
        except AttributeError:
            print("Given value not in linked list")

    def deleteByPos(self, position):
        if self.head == None:
            print("Linked list is empty. Nothing to delete")
            return

        if position == 0:
            self.head = self.head.next
            if self.head == None or self.head.next == None:
                self.tail = self.head
            if self.head != None:
                self.head.previous = None
            self.length -= 1
            return

        if position >= self.length:
            position = self.length - 1

        current_node = self.head
        for i in range(position - 1):
            current_node = current_node.next
        current_node.next = current_node.next.next
        if current_node.next != None:
            current_node.next.previous = current_node
        else:
            self.tail = current_node
        self.length -= 1
        return
