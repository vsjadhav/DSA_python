import queue_linkedListImplementation as Q

class TreeNode:
    def __init__(self,data=None):
        self.data = data
        self.leftchild = None
        self.rightchild= None
    def __str__(self, level=0):
        tree_str = "  "*level + str(self.data) + "\n"
        for child in (self.leftchild,self.rightchild):
            if child is None:
                continue
            tree_str+= child.__str__(level+1)
        return tree_str

bt = TreeNode("drinks")
cold = TreeNode("cold")
hot = TreeNode("hot")
cola = TreeNode("cola")
tea = TreeNode("tea")
coffee = TreeNode("coffee")
bt.leftchild = cold
bt.rightchild = hot
cold.leftchild=cola
hot.leftchild=tea
hot.rightchild=coffee

def preorderTraversal(rootnode): # root->left->right
    if not rootnode:
        return 
    print(rootnode.data)
    preorderTraversal(rootnode.leftchild)
    preorderTraversal(rootnode.rightchild)

def inorderTraversal(rootnode): # left->root->right
    if not rootnode:
        return
    inorderTraversal(rootnode.leftchild)
    print(rootnode.data)
    inorderTraversal(rootnode.rightchild)

def postorderTraversal(rootnode): # left->right->root
    if not rootnode:
        return
    postorderTraversal(rootnode.leftchild)
    postorderTraversal(rootnode.rightchild)
    print(rootnode.data)

def levelorderTraversal(rootnode):
    if not rootnode:
        return
    else:
        q = Q.Queue()
        q.enq(rootnode)
        while not(q.isempty()):
            node = q.dq()
            print(node.data)    
            if node.leftchild:
                q.enq(node.leftchild)
            if node.rightchild:
                q.enq(node.rightchild)  

def searchBT(rootnode,value):
    if not rootnode:
        return "BT is empty"
    else:
        q = Q.Queue()
        q.enq(rootnode)
        while not(q.isempty()):
            node = q.dq()
            if node.data == value:
                return "value found in BT"   
            if node.leftchild:
                q.enq(node.leftchild)
            if node.rightchild:
                q.enq(node.rightchild) 
        return "value not found in BT"

def insertnode(rootnode,value):
    '''inserts acording to level order traversal'''
    if rootnode.data is None:
        rootnode.data = value
    else:
        q = Q.Queue()
        q.enq(rootnode)
        while not(q.isempty()):
            node = q.dq()
            if not node.leftchild:
                node.leftchild = TreeNode(value)
                return
            if not node.rightchild:
                node.rightchild = TreeNode(value)
                return
            if node.leftchild:
                q.enq(node.leftchild)
            if node.rightchild:
                q.enq(node.rightchild)
            


print(bt)
print()
print("preorder:")
preorderTraversal(bt)
print("\ninorder")
inorderTraversal(bt)
print("\npostorder")
postorderTraversal(bt)
print("\nlevelorder")
levelorderTraversal(bt)
print()

print(searchBT(bt,"sger"))

print(searchBT(bt,"tea"))


insertnode(bt, "new")
insertnode(bt, 7)
insertnode(bt, 87486)
print(bt)

bt1 = TreeNode()
insertnode(bt1, 0)
insertnode(bt1, 1)
insertnode(bt1, 2)
insertnode(bt1, 3)
insertnode(bt1, 4)
insertnode(bt1, 5)
insertnode(bt1, 6)
insertnode(bt1, 7)
insertnode(bt1, 8)
insertnode(bt1, 9)

print(bt1)