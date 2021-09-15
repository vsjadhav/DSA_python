
class stack:
    def __init__(self):
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
    def push(self,value):
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

stack1 = stack()
print(stack1.isempty())

stack1.push(2)
stack1.push(7)
stack1.push(9)
stack1.push(6)
print(stack1)

print(stack1.isempty())

print(f"peek: {stack1.peek()}")

p = stack1.pop()
p = stack1.pop()
p = stack1.pop()
p = stack1.pop()
p = stack1.pop()
p = stack1.pop()

print(f"peek after pop: {stack1.peek()}")
print(f"poped item: {p}")


