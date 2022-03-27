class Stack():
    def __init__(self):
        self.array = []

    # In the peek method we access the last element of the array(top element of the stack)
    def peek(self):
        return self.array[len(self.array) - 1]

    def push(self, data):
        self.array.append(data)
        return
    
    def pop(self):
        if len(self.array) == 0:
            print("Stack is empty")
            return 
        else:
            self.array.pop()
            return
        
    def printStack(self):
        for i in range(len(self.array) - 1, -1, -1):
            print(self.array[i])
        return 