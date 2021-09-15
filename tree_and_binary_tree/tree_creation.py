class TreeNode:
    """has data and list of childrens"""
    def __init__(self,data,children=[]):
        self.data =data
        self.children =children 
    def __str__(self, level=0):
        tree_str = " "*level + str(self.data) + "\n"
        for child in self.children:
            tree_str+= child.__str__(level+1)
        return tree_str
    def addchild(self,child):
        self.children.append(child)

drinks = TreeNode("drinks",[])
cold = TreeNode("cold",[])
hot = TreeNode("hot",[])
cola = TreeNode("cola",[])
fanta = TreeNode("fanta",[])
tea = TreeNode("tea",[])
coffee = TreeNode("coffee",[])
milk = TreeNode("milk",[])

drinks.addchild(cold)
drinks.addchild(hot)
cold.addchild(cola)
cold.addchild(fanta)
hot.addchild(tea)
hot.addchild(coffee)
hot.addchild(milk)

print(drinks)

