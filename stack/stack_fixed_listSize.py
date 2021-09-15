
class stack:
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.list = []
    def __str__(self):
        l = self.list.copy()
        l.reverse()
        l1 = [str(i) for i in l]
        return "\n".join(l1)
    def isempty(self):
        if self.list:
            return False
        return True
    def isfull(self):
        if len(self.list)==self.maxsize:
            return True
        else: return False
    def push(self,value):
        if self.isfull():
            print("stack is full")
        else:   
            self.list.append(value)
    def pop(self):
        if self.isempty():
            print("stack is empty")
            return None
        else:
            return self.list.pop()
    def peek(self):
        if self.isempty():
            return None
        return self.list[-1]

stack1 = stack(5)
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


