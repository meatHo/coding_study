from queue import *

pq = PriorityQueue()

pq.put((-1,1))
pq.put((-3,2))
pq.put((1,3))

while not pq.empty():
    print(pq.get())