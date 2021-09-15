from collections import defaultdict

class Graph:
    def __init__(self, numberofVertices):
        self.graph = defaultdict(list)
        self.numberofVertices = numberofVertices
    def append(self, vertex ,edge):
        self.graph[vertex].append(edge)
    def topologicalsortUtil(self, vertex, visited, stack):
        visited.append(vertex)
        for adj_vertex in self.graph[vertex]:
            if adj_vertex not in visited:
                self.topologicalsortUtil(adj_vertex, visited, stack)
        stack.append(vertex)
    def topologicalSort(self):
        visited = []
        stack=[]

        for key in list(self.graph.keys()):
            if key not in visited:
                self.topologicalsortUtil(key, visited, stack)
        
        for i in range(len(stack)):
            p = stack.pop()
            print(p)
g=Graph(8)

g.append("a","c")
g.append("c","e")
g.append("e","h")
g.append("e","f")
g.append("f","g")
g.append("b","d")
g.append("b","c")
g.append("d","f")

print(g.graph)

g.topologicalSort()

        #     A B
        #     |/|
        #     C D
        #    /  |
        #   E   |
        #  / \ /
        # H   F-G