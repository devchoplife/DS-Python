class trieNode():
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class Trie():
    def __init__(self):
        self.root = trieNode()

    # We define a private helper function to calculate the numerical index of each character in the range of 0-25
    def characterIndex(self, char):
        if char.isupper():
            return ord(char) - ord('A')
        else:
            return ord(char) - ('a')

    # Time complexity for the insert method is O(n)
    def insert(self, string):
        pointer = self.root
        for character in string:
            index = self.characterIndex(character)
            if not pointer.children[index]:
                pointer.children[index] = trieNode()
            pointer = pointer.children[index]
        pointer.isEnd = True
        return

    def search(self, string):
        pointer = self.root
        for character in string:
            index = self.characterIndex(string)
            if not pointer.children[index]:
                return False
            pointer = pointer.children[index]
        return pointer and pointer.isEnd
