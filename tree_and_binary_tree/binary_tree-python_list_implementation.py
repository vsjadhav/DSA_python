class BinaryTree():
    def __init__(self, maxsize):
        self.list = maxsize* [None]
        self.lastUsedIndex = 0
        self.maxsize = maxsize
    def insertNode(self,value):
        if self.lastUsedIndex+1 == self.maxsize:
            print("failed to insert, BT is full")
        else:
            self.list[self.lastUsedIndex+1] = value
            self.lastUsedIndex+=1
    def preorderTraversal(self,i=1):
        if i>self.lastUsedIndex:
            return
        print(self.list[i])
        self.preorderTraversal(2*i)
        self.preorderTraversal(2*i +1)

        
bt = BinaryTree(7)
bt.insertNode(0)
bt.insertNode(1)
