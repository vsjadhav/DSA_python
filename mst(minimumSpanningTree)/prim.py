from collections import defaultdict
class Graph:
    def __init__(self):
        self.edges = []
        self.graph = defaultdict(list)
        self.weight = {}
    def addEdge(self,s,d,w):
        self.edges.append([s,d,w])
        self.graph[s].append(d)
        self.weight[(s,d)] = w
    def prim(self):
        vertices = set([v for v in self.graph.keys()])
        min_cost = dict.fromkeys(vertices, float('inf'))
        ans = {}
        startvertex = self.edges[0][0]
        min_cost[startvertex] = 0
        priority_queue = [startvertex]
        visited = []
        while priority_queue:
            current_source= priority_queue.pop(0)
            visited.append(current_source)
            for adj_vertex in self.graph[current_source]:
                if adj_vertex not in visited and self.weight[(current_source,adj_vertex)] < min_cost[adj_vertex]:
                    print(adj_vertex)
                    min_cost[adj_vertex]= self.weight[(current_source,adj_vertex)]
                    for v in vertices:
                        ans.pop((v,adj_vertex), None)
                    ans[(current_source,adj_vertex)]=self.weight[(current_source,adj_vertex)]
                if adj_vertex not in visited and adj_vertex not in priority_queue:
                    priority_queue.append(adj_vertex)
            priority_queue.sort(key= lambda i: min_cost[i])
            
        print(ans)

g = Graph()

# graph= "ab5,ba5,bd8,db8,cd6,dc6,cb10,bc10,ec20,ce20,ac13,ca13,ae15,ea15"
graph = "ab10,ba10,ac20,ca20,bc30,cb30,bd5,db5,cd15,dc15,de8,ed8,ce6,ec6"
l = graph.split(",")
for i in l:
    s = i[0]
    d = i[1]
    w = int(i[2:])
    g.addEdge(s,d,w)

print(g.graph)
g.prim()