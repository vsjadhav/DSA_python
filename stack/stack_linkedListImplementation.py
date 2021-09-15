class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    def __iter__(self):
        '''to iterate objects of this class with "in"-keyword'''
        node = self.head
        while node:
            yield node.value
            node = node.next
    def __str__(self):
        return "\n".join([str(i) for i in self])
    def push(self,value):
        newNode = Node(value)
        if self.head is None:
            newNode.next = None
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    def isempty(self):
        if self.head is None:
            return True
        return False
    def pop(self):
        if self.head is None:
            print("list is empty")
            return None
        else:
            if self.head.next is None:
                p = self.head.value
                self.head = None
                self.tail =None
                return p
            else:
                p = self.head.value
                self.head=self.head.next
                return p
    def peek(self):
         if self.head is None:
            print("list is empty")
            return None
        return self.head.value
        

stack1 = Stack()
print(stack1.isempty())

stack1.push(2)
stack1.push(7)
stack1.push(9)
stack1.push(6)
stack1.push(11)
stack1.push(17)
print(stack1)

print(stack1.isempty())

print(f"peek: {stack1.peek()}")

stack1.pop()

print(f"peek after pop: {stack1.peek()}")
