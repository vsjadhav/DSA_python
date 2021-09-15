
class Graph:
    def __init__(self,numberOfVertices, vertices):
        self.v = numberOfVertices
        self.vertices = vertices
        self.graph= self.createGraph()
    def createGraph(self): 
        g= []
        for i in range(self.v):
            row = [0]*self.v
            g.append(row)
        return g
    def addEdge(self,s,d,w):
        self.graph[s][d]=w
    def prim(self):
        ans=[]
        visited = [0]*self.v
        e = 0
        visited[0]=True
        while e< self.v -1:
            min = float('inf')
            for i in range(self.v):
                if visited[i]:
                    for j in range(self.v):
                        if (not visited[j] and self.graph[i][j]):
                            if self.graph[i][j] < min:
                                min = self.graph[i][j]
                                s=i
                                d=j
            ans.append([self.vertices[s],self.vertices[d],self.graph[s][d]])
            visited[d]=True
            e+=1
        print(ans)

# graph = "ab8ad1bc1ca4db2dc9"
graph = "ab10,ba10,ac20,ca20,bc30,cb30,bd5,db5,cd15,dc15,de8,ed8,ce6,ec6"
vertices = "abcde"

g =Graph(5,[v for v in vertices])

i=0
for v in vertices:
    graph= graph.replace(v, str(i))
    i+=1

l = graph.split(",")
for i in l:
    s = int(i[0])
    d = int(i[1])
    w = int(i[2:])
    g.addEdge(s,d,w)

# print(g.graph)
g.prim()
