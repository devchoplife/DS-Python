class my_array():
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        print(self.data.values())
        # This will print the attributes of the array class(length and data) in string format when print(array_instance) is executed
        return str(self.__dict__)

    def get(self, index):
        # This method takes in the index of the element as a parameter and returns the corresponding element in O(1) time.
        return self.data[index]

    def push(self, item):
        self.length += 1
        # Adds the item provided to the end of the array
        self.data[self.length - 1] = item

    def pop(self):
        last_item = self.data[self.length - 1]  # collects the last element
        del self.data[self.length - 1]  # delete the last element of the array
        self.length -= 1
        return last_item

    def insert(self, index, item):
        self.length += 1
        for i in range(self.length - 1, index, -1):
            # shifts elements from the given index to the end by one place towards the left. THis makes space at the soecified index
            self.data[i] = self.data[i - 1]
        # adds the element at the given index O(n) operation
        self.data[index] = item

    def delete(self, index):
        for i in range(index, self.length - 1):
            # shifts elements from the given index to the ned by one place towards right
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1
