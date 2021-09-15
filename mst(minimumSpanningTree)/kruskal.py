import disjoinSet as D

class Graph():
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = []
    def addEdge(self,s,d,w):
        self.graph.append([s,d,w])
    def kruskal(self):
        djset = D.DisjoinSet(self.vertices)
        ans=[]
        cost = 0
        g = sorted(self.graph, key= lambda i: i[2], reverse=True)
        while g:
            s,d,w = g.pop()
            if djset.find_parent(s) != djset.find_parent(d):
                djset.union(s,d)
                cost += w
                ans.append([s,d,w])
        print(f"cost: {cost}")
        print(ans)
    
    def kruskal_withoutCreatingCopyOfGraph(self):
        djset = D.DisjoinSet(self.vertices)
        ans=[]
        cost = 0
        self.graph = sorted(self.graph, key= lambda i: i[2])
        i,e=0,0
        while e < len(self.vertices) -1:
            s,d,w = self.graph[i]
            i+=1
            if djset.find_parent(s) != djset.find_parent(d):
                e+=1
                djset.union(s,d)
                cost += w
                ans.append([s,d,w])
        print(f"cost: {cost}")
        print(ans)

inputstr = "abcde"
vertices = [i for i in inputstr]            
g = Graph(vertices)

graph= "ab5,ba5,bd8,db8,cd6,dc6,cb10,bc10,ec20,ce20,ac13,ca13,ae15,ea15"
l = graph.split(",")
for i in l:
    s = i[0]
    d = i[1]
    w = int(i[2:])
    g.addEdge(s,d,w)


g.kruskal()

g.kruskal_withoutCreatingCopyOfGraph()