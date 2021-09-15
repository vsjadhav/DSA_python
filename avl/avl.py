import queue_linkedListImplementation as Q

class BSTNode:
    def __init__(self,data=None):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.height = 1
    def __str__(self, level=0):
        tree_str = "  "*level + str(self.data) + "\n"
        for child in (self.leftchild,self.rightchild):
            if child is None:
                continue
            tree_str+= child.__str__(level+1)
        return tree_str
    def preorderTraversal(self,rootnode):# root->left->right
        if rootnode is None:
            return 
        print(rootnode.data)
        rootnode.preorderTraversal(rootnode.leftchild)
        rootnode.preorderTraversal(rootnode.rightchild)
    def inorderTraversal(self,rootnode): # left->root->right
        if rootnode is None:
            return 
        rootnode.inorderTraversal(rootnode.leftchild)
        print(rootnode.data)
        rootnode.inorderTraversal(rootnode.rightchild)
    def postorderTraversal(self,rootnode): # left->right->root
        if rootnode is None:
            return 
        rootnode.postorderTraversal(rootnode.leftchild)
        rootnode.postorderTraversal(rootnode.rightchild)
        print(rootnode.data)
    def levelorderTraversal(self,rootnode):
        q = Q.Queue()
        q.enq(rootnode)
        while not(q.isempty()):
            node = q.dq()
            print(node.data)    
            if node.leftchild:
                q.enq(node.leftchild)
            if node.rightchild:
                q.enq(node.rightchild)
    def search(self,ptr,data):
        if ptr is None:
            return "data not Found"
        if ptr.data == data:
            return "data found"
        if ptr.data>=data:
            ptr = ptr.leftchild
            return ptr.search(ptr,data)
        else:
            ptr = ptr.rightchild
            return ptr.search(ptr,data)
    
    def getHeight(self,node):
        if node is None:
            return 0
        return node.height
    def rightRotation(self,node):
        new_root = node.leftchild
        node.leftchild = node.leftchild.rightchild
        new_root.rightchild = node
        node.height = 1+ max(self.getHeight(node.leftchild), self.getHeight(node.rightchild))
        new_root.height = 1+ max(self.getHeight(new_root.leftchild), self.getHeight(new_root.rightchild))
        return new_root
    def leftRotation(self,node):
        new_root = node.rightchild
        node.rightchild = node.rightchild.leftchild
        new_root.leftchild = node
        node.height = 1+ max(self.getHeight(node.leftchild), self.getHeight(node.rightchild))
        new_root.height = 1+ max(self.getHeight(new_root.leftchild), self.getHeight(new_root.rightchild))
        return new_root
    def getBalence(self,node):
        if node is None:
            return 0
        return self.getHeight(node.leftchild) - self.getHeight(node.rightchild)
    def min_value_node(self,root,data):
        while (root.leftchild is not None):
            root = root.leftchild
        return root
    def deleteNode(self,ptr,data):
        if ptr is None:
            return ptr
        elif data < ptr.data :
            ptr.leftchild = ptr.deleteNode(ptr.leftchild,data)
        elif data > ptr.data :
            ptr.rightchild = ptr.deleteNode(ptr.rightchild,data)
        else:
            if ptr.leftchild is None:
                temp = ptr.rightchild
                ptr = None
                return temp
            if ptr.rightchild is None:
                temp = ptr.leftchild
                ptr = None
                return temp
            temp = ptr.min_value_node(ptr.rightchild,data)
            ptr.data = temp.data
            ptr.rightchild = ptr.deleteNode(ptr.rightchild, temp.data)
        
        ptr.height = 1+ max(self.getHeight(ptr.leftchild), self.getHeight(ptr.rightchild))
        # print(ptr.height)
        balance = self.getBalence(ptr)
        # print(balance)
        if balance>1 and data<= ptr.leftchild.data:
            return self.rightRotation(ptr)
        elif balance>1 and data> ptr.leftchild.data:
            ptr.leftchild= self.leftRotation(ptr)
            return self.rightRotation(ptr)
        elif balance<-1 and data> ptr.rightchild.data:
            print("left rotation")
            return self.leftRotation(ptr)
        elif balance>1 and data<= ptr.rightchild.data:
            ptr.rightchild= self.rightRotation(ptr)
            return self.leftRotation(ptr)
        # print(self)
        return ptr




class BST:
    def __init__(self):
        self.rootnode = None
    def __str__(self, ptr=None , level=0):
        ptr= self.rootnode
        if ptr is None:
            return "bst is empty"
        return ptr.__str__()
    def preorderTraversal(self,ptr=None):
        ptr= self.rootnode
        if ptr is None:
            return "bst is empty"
        ptr.preorderTraversal(ptr)
    def levelorderTraversal(self):
        ptr = self.rootnode
        if ptr is None:
                return "bst is empty"
        ptr.levelorderTraversal(ptr)
    def getHeight(self,node):
        if node is None:
            return 0
        return node.height
    def rightRotation(self,node):
        new_root = node.leftchild
        node.leftchild = node.leftchild.rightchild
        new_root.rightchild = node
        node.height = 1+ max(self.getHeight(node.leftchild), self.getHeight(node.rightchild))
        new_root.height = 1+ max(self.getHeight(new_root.leftchild), self.getHeight(new_root.rightchild))
        return new_root
    def leftRotation(self,node):
        new_root = node.rightchild
        node.rightchild = node.rightchild.leftchild
        new_root.leftchild = node
        node.height = 1+ max(self.getHeight(node.leftchild), self.getHeight(node.rightchild))
        new_root.height = 1+ max(self.getHeight(new_root.leftchild), self.getHeight(new_root.rightchild))
        return new_root
    def getBalence(self,node):
        if node is None:
            return 0
        return self.getHeight(node.leftchild) - self.getHeight(node.rightchild)

    def insertnodeUtil(self,data,ptr):
        if ptr is None:
            return BSTNode(data)
        elif data<= ptr.data:
            # print("left entry")
            ptr.leftchild = self.insertnodeUtil(data, ptr.leftchild)
        elif data> ptr.data:
            # print("right entry")
            ptr.rightchild = self.insertnodeUtil(data, ptr.rightchild)

        ptr.height = 1+ max(self.getHeight(ptr.leftchild), self.getHeight(ptr.rightchild))
        # print(ptr.height)
        balance = self.getBalence(ptr)
        # print(balance)
        if balance>1 and data<= ptr.leftchild.data:
            return self.rightRotation(ptr)
        elif balance>1 and data> ptr.leftchild.data:
            ptr.leftchild= self.leftRotation(ptr)
            return self.rightRotation(ptr)
        elif balance<-1 and data> ptr.rightchild.data:
            return self.leftRotation(ptr)
        elif balance>1 and data<= ptr.rightchild.data:
            ptr.rightchild= self.rightRotation(ptr)
            return self.leftRotation(ptr)
        # print(self)
        return ptr
    
    def insertnode(self,data):
        if self.rootnode is None:
            self.rootnode = BSTNode(data)
            return
        ptr = self.rootnode
        self.rootnode = self.insertnodeUtil(data, ptr)
        return

    def searchnode(self,data):
        if self.rootnode is None:
            return "bst is empty"
        ptr = self.rootnode
        while True:
            if ptr is None:
                return "not found"
            elif ptr.data == data:
                return "data found"
            elif ptr.data > data:
                if ptr.leftchild is None:
                    return "value not found"
                elif ptr.leftchild == data:
                    return "data found"
                else:
                    ptr=ptr.leftchild
            else:
                if ptr.rightchild is None:
                    return "value not found"
                elif ptr.rightchild == data:
                    return "data found"
                else:
                    ptr=ptr.rightchild
    def searchnode_withRecursion(self,data):
        ptr = self.rootnode
        if ptr is None:
            return "BST is empty"
        return ptr.search(ptr,data)
    def deleteNode(self,data): # uses recursion
        ptr = self.rootnode
        ptr.deleteNode(ptr,data)
    def deleteNode_withoutRecursion(self,data): ###########--debug required--###########
        if self.rootnode is None:
            return "bst is empty"
        ptr = self.rootnode
        flag = None
        while True:
            if ptr is None:
                return "data not found"
            elif ptr.data == data:
                data_ptr = ptr
                break
            elif ptr.data > data:
                if ptr.leftchild is None:
                    return "data not found"
                elif ptr.leftchild == data:
                    data_ptr = ptr.leftchild
                    flag = 0
                    break
                else:
                    ptr=ptr.leftchild
            else:
                if ptr.rightchild is None:
                    return "data not found"
                elif ptr.rightchild == data:
                    data_ptr = ptr.rightchild
                    flag = 1
                    break
                else:
                    ptr=ptr.rightchild
        while True:
            if data_ptr.leftchild is None:
                temp = data_ptr.rightchild
                if flag == 0:
                    ptr.leftchild = temp
                    return "node deleted successfully"
                elif flag == 1: 
                    ptr.rightchild = temp
                    return "node deleted successfully"
                else: 
                    ptr.data = ptr.rightchild.data
                    data_ptr = ptr.rightchild
                    flag == 1
            if data_ptr.rightchild is None:
                temp = data_ptr.rightchild
                if flag == 0:
                    ptr.leftchild = temp
                    return "node deleted successfully"
                elif flag == 1: 
                    ptr.rightchild = temp
                    return "node deleted successfully"
                else: 
                    ptr.data = ptr.lefttchild.data
                    data_ptr = ptr.leftchild
                    flag == 0
            else: break
        temp = data_ptr.rightchild
        min_ptr = data_ptr.rightchild
        i=0
        while min_ptr.leftchild is not None:
            if i>0:
                temp = temp.leftchild
            min_ptr = min_ptr.leftchild
            i+=1
        # temp = ptr.min_value_node(ptr.rightchild,data)
        data_ptr.data = min_ptr.data
        if i>0:
            data_ptr.rightchild = temp.rightchild
            return "node deleted successfully"
        temp.leftchild = min_ptr.rightchild
        return "node deleted successfully"
        



        
bst = BST()
bst.insertnode(0)
bst.insertnode(10)
bst.insertnode(20)
bst.insertnode(30)
bst.insertnode(40)
bst.insertnode(50)
bst.insertnode(60)
bst.insertnode(70)
bst.insertnode(80)
bst.insertnode(90)
print(bst)

bst.levelorderTraversal()
print(bst.searchnode(20))
print(bst.searchnode_withRecursion(20))

bst.deleteNode(70)
print("AVL tree after deleting node with value 70:")
print(bst)