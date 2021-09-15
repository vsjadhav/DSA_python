class Graph:
    def __init__(self,numberofVrtices):
        self.v = numberofVrtices
        self.graph= []
        self.nodes=[]
    def addnode(self,node):
        self.nodes.append(node)
    def addEdge(self, s, d, w):
        self.graph.append([s,d,w])
    def bellmanFord(self,startVertex):
        min_distance = dict.fromkeys(self.nodes, float('inf')) #or {i:float('inf) for i in self.nodes}
        min_distance[startVertex]=0
        for _ in range(self.v - 1):
            for s,d,w in self.graph:
                if min_distance[s] != float('inf'):
                    new_dist = min_distance[s] + w
                    if new_dist< min_distance[d]:
                        min_distance[d]=new_dist
        for s,d,w in self.graph:
            new_dist = min_distance[s] + w
            if min_distance[s] != float('inf') and new_dist< min_distance[d]:
                return "there is a negative loop in graph"
        return min_distance
    def bellmanFord_withPath(self,startVertex):
        min_distance = dict.fromkeys(self.nodes, float('inf')) #or {i:float('inf) for i in self.nodes}
        min_path = dict.fromkeys(self.nodes, [])
        min_distance[startVertex]=0
        min_path[startVertex].append(startVertex)
        for _ in range(self.v - 1):
            for s,d,w in self.graph:
                if min_distance[s] != float('inf'):
                    new_dist = min_distance[s] + w
                    if new_dist< min_distance[d]:
                        min_distance[d]=new_dist
                        min_path[d] = min_path[s].copy()
                        min_path[d].append(d)
        for s,d,w in self.graph:
            new_dist = min_distance[s] + w
            if min_distance[s] != float('inf') and new_dist< min_distance[d]:
                return "there is a negative loop in graph"
        return min_distance, min_path

g=Graph(5)

# nodes = "abcdefg"
nodes = "abcde"
for node in nodes:
    g.addnode(node)
# graph = "ab2ac5bc6bd1be3de4cf8eg9gf7"
graph = "eb4ed2db1ba3ad6ac6cd1dc2"
j=0
for i in range(len(graph)//3):
    temp = graph[j:j+3]
    l=[]
    for k in temp:
        l.append(k)
    s = l[0]
    d = l[1]
    w = int(l[2])
    g.addEdge(s,d,w)
    j+=3
# print(g.nodes)
# print(g.edges)
# print(g.weight)

print(g.bellmanFord("e"))
min_dist , min_path = g.bellmanFord_withPath("e")
print(min_dist)
print(min_path)

g.graph[4][2]=-6
print(g.bellmanFord("e"))
