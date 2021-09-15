class A(object):
    def foo(self):
        print('A.foo()')

class B(object):
    def foo(self):
        print('B.foo()')

class C(A, B):
    def zoo(self):
        super(C, self).foo()
        print('C.foo()')
        A.foo(self)
        B.foo(self)


c = C()
c.foo()
print(C.__mro__)