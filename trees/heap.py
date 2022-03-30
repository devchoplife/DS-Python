import sys


# A Max heap( and min heap) is typically represented as an array. The root element will be at Arr[0]
# Arr[(i-1)/2] Returns the parent node
# Arr[(2*i)+1] Returns the left child node.
# Arr[(2*i)+2] Returns the right child node

"""
Operations on Max Heap (and min heap) include:
getMax(): It returns the root element of Max Heap. Time Complexity of this operation is O(1).
extractMax(): Removes the maximum element from MaxHeap. Time Complexity of this Operation is O(Log n)as this operation needs to maintain the heap property (by calling heapify()) after removing root.
insert(): Inserting a new key takes O(Log n) time. We add a new key at the end of the tree.
If new key is smaller than its parent, then we dont need to do anything. Otherwise, we need to traverse up to fix the violated heap property.
Here we are going to implement a max-heap
"""


class MaxHeap():
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.FRONT = 1

    def parent(self, pos):
        return pos // 2

    def left_child(self, pos):
        return (2 * pos) + 1

    def right_child(self, pos):
        return (2 * pos) + 2

    # Method that returns true if the passed node is a leaf node.
    # All the nodes in the second half of the heap(when viewed as an array) are leaf nodes.
    # So we just check if the position entered is >= half of the size of the heap and <= size of the heap
    def is_leaf(self, pos):
        if pos >= (self.size // 2) and pos <= self.size:
            return True
        return False

    # Swap two nodes of the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    """
    Method to heapify the node at pos. This method will be called whenever the heap property is disturbed, to restore the heap property of the heap
    We will check if the concerned node is a leaf node or not first. If it is, then no need to do anything.
    If it is not and it is smaller than any of its children, then we will check which of its children is largest
    and swap the node with its largest child. After doing this, the heap property may be disturbed. So we will call max_heapify again.
    """

    def maxHeapify(self, pos):
        # Check if it is a leaf node
        if not self.is_leaf(pos):
            if (self.Heap[pos] < self.Heap[self.left_child(pos)] or
                    self.Heap[pos] < self.Heap[self.right_child(pos)]):

                # Swap with the left child and heapify the left child
                if self.Heap[self.left_child(pos)] > self.Heap[self.right_child(pos)]:
                    self.swap(pos, self.left_child(pos))
                    self.maxHeapify(self.left_child(pos))

                # Swap with the right child and heapify
                else:
                    self.swap(pos, self.right_child(pos))
                    self.maxHeapify(self.right_child(pos))

    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element
        current = self.size
        while self.Heap[current] > self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def printHeap(self):
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.Heap[i]) + " LEFT CHILD : " + str(
                self.Heap[(2 * i) + 1]) + " RIGHT CHILD : " + str(self.Heap[(2 * i) + 2]))

    # Method to remove and return the maximun element in the heap 
    def extract_max(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.maxHeapify(self.FRONT)
        return popped
