class DisjoinSet():
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {v:v for v in self.vertices}
        self.rank = dict.fromkeys(self.vertices, 0)
    def find_parent(self,x):
        if self.parent[x] == x:
            return x
        return self.find_parent(self.parent[x])
    def union(self,x,y):
        xroot = self.find_parent(x)
        yroot = self.find_parent(y)

        if self.rank[xroot]>self.rank[yroot]:
            self.parent[yroot]=xroot
        if self.rank[yroot]>self.rank[xroot]:
            self.parent[xroot]=yroot
        else:
            self.parent[yroot]= xroot
            self.rank[xroot] +=1

if __name__ == "__main__":
    vertices = ["a","b","c","d","e"]
    dSet = DisjoinSet(vertices)
    print(dSet.find_parent("a"))
    print(dSet.find_parent("b"))

    dSet.union("a","b")
    print(dSet.find_parent("a"))
    print(dSet.find_parent("b"))
    print(dSet.find_parent("e"))

    dSet.union("a","e")
    print(dSet.find_parent("a"))
    print(dSet.find_parent("e"))













# def find_parent_without_recursion(x):
#     l=[]
#     v=[]
#     x="A"
#     i = v.index(x)
#     temp = x
#     while True:
#         if l[i] == temp:
#             return l[i]
#         i = v.index(l[i])
#         temp = l[i]