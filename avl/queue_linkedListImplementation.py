class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        '''to iterate objects of this class with "in"-keyword'''
        node = self.head
        while node:
            yield node.value
            node = node.next
    def __str__(self):
        return "\n".join([str(i) for i in self])
    def enq(self,value):
        newNode = Node(value)
        if self.head is None:
            newNode.next = None
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = None
            self.tail.next = newNode
            self.tail = newNode
    def isempty(self):
        if self.head is None:
            return True
        return False
    def dq(self):
        if self.head is None:
            print("list is empty")
            return None
        else:
            if self.head.next is None:
                rtn = self.head.value
                self.head = None
                self.tail =None
                return rtn
            else:
                rtn = self.head.value
                self.head=self.head.next
                return rtn
    def peek(self):
        return self.head.value
        
if __name__ == "__main__":
    q = Queue()
    print(q.isempty())

    q.enq(0)
    q.enq(1)
    q.enq(2)
    q.enq(3)
    q.enq(10)
    q.enq(11)
    q.enq(12)
    q.enq(13)

    print(q)

    p = q.dq()
    print(f"dequeued item: {p}")
    q.enq(14)
    q.enq(15)

    print(q)

    print(q.isempty())

    print(f"peek: {q.peek()}")

    p = q.dq()
    print(f"dequeued item: {p}")
    p = q.dq()
    print(f"dequeued item: {p}")
    p = q.dq()
    print(f"dequeued item: {p}")
    p = q.dq()
    print(f"dequeued item: {p}")
    p = q.dq()
    print(f"dequeued item: {p}")
    p = q.dq()

    print(f"peek after dequeue: {q.peek()}")
    print(f"dequeued item: {p}")

    q.dq()
    q.dq()
    print(f"isempty:{q.isempty()}")

    print(q)
