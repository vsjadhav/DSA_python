class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        '''to iterate objects of this class with "in"-keyword'''
        node = self.head
        while node:
            yield node.value
            if node.next == self.head:
                break
            node = node.next
    def insert(self,value,index=-1):
        newNode = Node(value)
        if self.head is None:
            newNode.next = newNode
            self.head = newNode
            self.tail = newNode
        elif index == 0:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = newNode
        elif index == -1:
            newNode.next = self.head
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
                if temp.next == self.head:
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
                if temp == self.head:
                    temp = None
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
                if temp==self.head:
                    return f"value {nodevalue} not found"
    def pop(self,index=-1):
        if self.head is None:
            print("list is empty")
        elif index == 0:
            if self.head.next is self.head:
                self.head = None
                self.tail =None
            else:
                self.head=self.head.next
                self.tail.next = self.head
        elif index == -1:
            temp = self.head
            while temp.next.next!=self.head:
                temp=temp.next
            temp.next = self.head
            self.tail = temp
        else:
            i = -2
            flag=True
            temp = self.head
            while i<index-3:
                temp = temp.next
                if (temp is self.head) or (temp.next is self.head):
                    print(f"could not delete node : length of list is {i+3} but index given was {index}")
                    flag =False
                    break
                i+=1
            if flag:
                if temp.next.next == self.head:
                    temp.next = self.head
                    self.tail=temp
                else:
                    temp.next = temp.next.next


csll = CircularSinglyLinkedList()
csll.insert(1)
csll.insert(2)
csll.insert(3)
csll.insert(4)
csll.insert(5)

csll.insert(0,0)

csll.insert(7,6)

print([i for i in csll])
print(f"tail: {csll.tail.value}")
print(f"tail.next: {csll.tail.next.value}")

csll.traverse()

print(csll.search(4))
print(csll.search(79))
print(csll.search(7))

print(f"before pop(): {[i for i in csll]}")
csll.pop(3)
print(f"before pop(): {[i for i in csll]}")
