from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.weight = {}
    def addnode(self ,node):
        self.nodes.add(node)
    def addEdge(self, source, destination, weight):
        self.edges[source].append(destination)
        self.edges[destination].append(source)
        self.weight[(source,destination)]= weight
        self.weight[(destination,source)]= weight
    def dijkstra(self,start):
        min_cost = dict.fromkeys(self.nodes, float('inf'))
        min_cost[start]=0
        done=[]
        priority_queue = [start]
        while priority_queue:
            temp_source = priority_queue.pop(0)
            if temp_source not in done:
                done.append(temp_source) 
            for adj_vertex in self.edges[temp_source]:
                new_cost = min_cost[temp_source] + self.weight[(temp_source,adj_vertex)]
                if new_cost < min_cost[adj_vertex]:
                    min_cost[adj_vertex]= new_cost
                if adj_vertex not in done:
                    priority_queue.append(adj_vertex)
            priority_queue = sorted(priority_queue, key= lambda vertex: min_cost[vertex])
        return min_cost

g = Graph()

nodes = "abcdefg"
for node in nodes:
    g.addnode(node)
graph = "ab2ac5bc6bd1be3de4cf8eg9gf7"
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

print(g.dijkstra("e"))

# d= {"aewfc":9,"fsd":3,"wa":0,"awed":1}
# print(d)
# m = max(d.items(), key=lambda i : i[1])
# print(m)
# d=dict(sorted(d.items(),key=lambda i:i[1]))
# print(d)


# ans = {"a":0,"b":5,"c":float('inf'),"d":float('inf')}
# q = ["c","d","a","b"]
# print(q)
# q=sorted(q, key= lambda i: ans[i])
# print(q)