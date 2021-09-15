class Queue:
    def __init__(self):
        self.list = []
    def __str__(self):
        return "\n".join([str(i) for i in self.list])
    def enq(self,value):
        self.list.append(value)
    def isempty(self):
        if self.list:
            return False
        return True
    def dq(self):
        if self.isempty():
            print("q is empty")
            return None
        return self.list.pop(0)
    def peek(self):
        if self.isempty():
            print("q is empty")
            return None
        return self.list[0]

q = Queue()
print(q.isempty())

q.enq(2)
q.enq(7)
q.enq(9)
q.enq(6)
print(q)

print(q.isempty())

print(f"peek: {q.peek()}")

p = q.dq()
p = q.dq()
p = q.dq()
p = q.dq()
p = q.dq()
p = q.dq()

print(f"peek after dequeue: {q.peek()}")
print(f"dequeued item: {p}")

