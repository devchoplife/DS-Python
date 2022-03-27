"""
Time complexities are as follows:
Peek - O(1)
Enqueue - O(1)
Dequeue - o(1)
"""
class Queue():
    def __init__(self):
        self.array = []
        
    # Queues have the FIFO policy 
    def peek(self):
        return self.array[0]
    
    def Enqueue(self, data):
        self.array.append(data)
        return
    
    # This removes the first element in the queue
    def Dequeue(self):
        if len(self.array) == 0:
            print("Queue is empty")
            return 
        else:
            to_dequeue = self.array[0]
            self.array = self.array[1:]
            return to_dequeue
        
    def printQueue(self):
        for i in range(0, len(self.array) - 1):
            print(self.array[1])
        return