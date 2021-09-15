# ########collection's deque module############

# from collections import deque

# q = deque(maxlen=4)

# q.append(0)
# q.append(1)
# q.append(2)
# q.append(3)
# print(q)

# q.append(77)
# print(q)

# poped = q.popleft()
# print(q)
# print(poped)


##################Queue module###################
# it has fifo,lifo and priority queue 
# we will see fifo here

import queue as Q

q = Q.Queue(maxsize=3)
print(q.empty())

q.put(0)
q.put(1)
q.put(2)

print(q.full())
print(f"size:{q.qsize()}")

print(q.get())
print(q.full())
print(f"size:{q.qsize()}")

q.put(7)
print(q.get())

##############multiprocessing queue module###########

from multiprocessing import Queue

q = Queue(maxsize=3)
# it also has put() and get()