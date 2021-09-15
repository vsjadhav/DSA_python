class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        '''to iterate objects of this class with "in"-keyword'''
        node = self.head
        while node:
            yield node.value
            node = node.next
    def insert(self,value,index=-1):
        newNode = Node(value)
        if self.head is None:
            newNode.next = None
            self.head = newNode
            self.tail = newNode
        elif index == 0:
            newNode.next = self.head
            self.head = newNode
        elif index == -1:
            newNode.next = None
            self.tail.next = newNode
            self.tail = newNode
        else:
            i = -2
            flag=True
            temp = self.head
            while i<index-3:
                temp = temp.next
                if temp is None:
                    print(f"could not insert node : length of list is {i+3} but index given was {index}")
                    flag =False
                    break
                i+=1
            if flag:
                if temp.next is None:
                    self.tail = newNode
                newNode.next= temp.next
                temp.next = newNode
    def traverse(self):
        if self.head is None:
            print("list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.value)
                temp = temp.next
    def search(self,nodevalue):
        if self.head is None:
            print("not found, list is empty")
        else:
            temp = self.head
            i=0
            while temp:
                if temp.value == nodevalue:
                    return f"value {nodevalue} found at index {i}"
                i+=1
                temp = temp.next
            return "value not found"
    def pop(self,index=-1):
        if self.head is None:
            print("list is empty")
        elif index == 0:
            if self.head.next is None:
                self.head = None
                self.tail =None
            else:
                self.head=self.head.next
        elif index == -1:
            temp = self.head
            while temp.next.next:
                temp=temp.next
            temp.next = None
            self.tail = temp
        else:
            i = -2
            flag=True
            temp = self.head
            while i<index-3:
                temp = temp.next
                if temp is None:
                    print(f"could not delete node : length of list is {i+3} but index given was {index}")
                    flag =False
                    break
                i+=1
            if flag:
                if temp.next.next is None:
                    temp.next = None
                    self.tail=temp
                else:
                    temp.next = temp.next.next


sll1= SinglyLinkedList()
# node1 = Node(1)
# node2 = Node(2)

# sll1.head = node1
# sll1.head.next = node2
# sll1.tail = node2
sll1.insert(1)
sll1.insert(2)
sll1.insert(3)
sll1.insert(4)
sll1.insert(0,0)
sll1.insert(5)
sll1.insert(77,6)
print(sll1.tail.value)
print([i for i in sll1])

# sll1.insert(7,4)
# print([i for i in sll1])

# sll1.traverse()
# print(sll1.search(7))

# sll1.pop(5)
# print([i for i in sll1])
