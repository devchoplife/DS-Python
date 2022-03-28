# Undirected graph implementation
class Graph():
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacencyList = {}

    def insert_node(self, data):
        if data not in self.adjacencyList:
            self.adjacencyList[data] = []
            self.numberOfNodes += 1
            return

    def insert_edge(self, vertex1, vertex2):
        if vertex2 not in self.adjacencyList[vertex1]:
            self.adjacencyList[vertex1].append(vertex2)
            self.adjacencyList[vertex2].append(vertex1)
            return
        return "Edge already exists"

    def show_connections(self):
        for node in self.adjacencyList:
            print(
                f'{node} -->> {" ".join(map(str, self.adjacencyList[node]))}')
