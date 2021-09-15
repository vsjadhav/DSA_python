
class Graph:
    def __init__(self,numberOfVertices):
        self.v = numberOfVertices
        self.graph= self.createGraph()
    def createGraph(self): 
        g= []
        for i in range(self.v):
            row = [0]*self.v
            for j in range(self.v):
                if i!=j:
                    row[j]= float('inf')
            g.append(row)
        return g
    def addEdge(self,s,d,w):
        self.graph[s][d]=w
    def floydWarshall(self):
        distance = self.graph.copy()

        for v in range(self.v):
            for i in range(self.v):
                for j in range(self.v):
                    distance[i][j] = min(distance[i][j], distance[i][v]+distance[v][j])
        return distance

g =Graph(4)
graph = "ab8ad1bc1ca4db2dc9"
graph= graph.replace("a","0")
graph= graph.replace("b","1")
graph= graph.replace("c","2")
graph= graph.replace("d","3")
j=0
for i in range(len(graph)//3):
    temp = graph[j:j+3]
    l=[]
    for k in temp:
        l.append(k)
    s = int(l[0])
    d = int(l[1])
    w = int(l[2])
    g.addEdge(s,d,w)
    j+=3

print(g.floydWarshall())
