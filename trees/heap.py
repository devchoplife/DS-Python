from re import M
import sys


class MaxHeap():
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.FRONT = 1

    def parent(self, pos):
        return pos // 2

    def left_child(self, pos):
        return 2 * pos

    def right_child(self, pos):
        return (2 * pos) + 1

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

    def maxHeapify(self, pos):
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
                self.Heap[2 * i]) + " RIGHT CHILD : " + str(self.Heap[2 * i + 1]))

    def extract_max(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.maxHeapify(self.FRONT)
        return popped