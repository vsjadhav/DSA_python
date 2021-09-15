class Queue:
    def __init__(self,maxsize):
        self.list = maxsize*[None]
        self.maxsize = maxsize
        self.first = None
        self.last = None
    def __str__(self):
        if self.isempty():
            return "Queue is empty"
        else:
            l = [self.list[self.first]]
            temp=self.first 
            while temp!=self.last:
                temp = self.cyclicIncrement(temp)
                l.append(self.list[temp]) 
            return "\n".join([str(i) for i in l])              
    def cyclicIncrement(self,n):
        return (n+1)%self.maxsize
    def isfull(self):
        if self.isempty():
            return False
        if self.cyclicIncrement(self.last) == self.first:
            return True
    def isempty(self):
        if self.first is None and self.last is None:
            return True
        return False
    def enq(self,value):
        if self.isempty():
            self.list[0]= value
            self.first=0
            self.last = 0
        elif self.isfull():
            print("Queue is full")
        else:
            self.last= self.cyclicIncrement(self.last)
            self.list[self.last] = value
    def dq(self):
        if self.isempty():
            print("q is empty")
            return None
        elif self.first == self.last:
                rtn = self.list[self.first]
                self.first = None
                self.last = None
                return rtn
        else:
            rtn = self.list[self.first]
            self.first = self.cyclicIncrement(self.first)
            return rtn
    def peek(self):
        if self.isempty():
            print("q is empty")
            return None
        return self.list[self.first]

q = Queue(7)
print(q.list)
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
print(f"isfull:{q.isfull()}")

print(q)
