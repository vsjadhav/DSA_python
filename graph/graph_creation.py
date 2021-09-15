class graph:
    def __init__(self,gdict):
        if gdict is None:
            gdict={}
        self.gdict = gdict
    def addedge(self,vertex,edge):
        self.gdict[vertex].append(edge)
    def bfsTraversal(self,start_vertex):
        visited = [start_vertex]
        queue = [start_vertex]
        while queue:
            dequeued = queue.pop(0)
            print(dequeued)
            for adj_vertex in self.gdict[dequeued]:
                if adj_vertex not in visited:
                    queue.append(adj_vertex)
                    visited.append(adj_vertex)
    def dfsTraversal(self,start_vertex):
        visited = [start_vertex]
        stack = [start_vertex]
        while stack:
            poped = stack.pop()
            print(poped)
            for adj_vertex in self.gdict[poped]:
                if adj_vertex not in visited:
                    stack.append(adj_vertex)
                    visited.append(adj_vertex)
                    

g = graph({                         #              A
    "a":["b","c"],                  #             / \
    "b":["a","d","e"],              #            B   C
    "c":["a","e"],                  #            | \ |
    "d":["c","f"],                  #            D---E
    "d":["b","e","f"],              #            \   /
    "e":["d","f"],                  #              F 
    "f":["e","d"]                   #
})


print(g.gdict)
g.bfsTraversal("a")
print("##########")
g.dfsTraversal("a")