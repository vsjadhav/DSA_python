class graph:
    def __init__(self,gdict):
        if gdict is None:
            gdict={}
        self.gdict = gdict
    def addedge(self,vertex,edge):
        self.gdict[vertex].append(edge)

g = graph({
    "a":["b","c"],
    "b":["a","g"],
    "c":["a","d","e"],
    "d":["c","f"],
    "d":["b","c","f"],
    "e":["c","f"],
    "f":["e","d","g"],
    "g":["b"]
})