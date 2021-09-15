class graph:
    def __init__(self,gdict):
        if gdict is None:
            gdict={}
        self.gdict = gdict
    def addedge(self,vertex,edge):
        self.gdict[vertex].append(edge)
    def bfsForSSSP(self,start_vertex, end_vertex):
        queue = [[start_vertex]]
        while queue:
            path = (queue.pop(0))
            node = path[-1]
            if node == end_vertex:
                return path
            for adj_vertex in self.gdict.get(node,[]):
                new_path=path.copy()
                new_path.append(adj_vertex)
                queue.append(new_path)
                # path.append(adj_vertex)
                # queue.append(path)


g= graph({
    "a":["b","c"],
    "b":["d","g"],
    "c":["d","e"],
    "d":["f"],
    "e":["f"],
    "g":["f"]
})
print(g.gdict)

print(g.bfsForSSSP("a","f"))


                # A-B
                # | |\
                # C-D G
                # | |/
                # E-F