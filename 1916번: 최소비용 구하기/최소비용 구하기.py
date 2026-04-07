#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1916                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatho <boj.kr/u/meatho>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1916                           #+#        #+#      #+#     #
#    Solved: 2026/04/06 23:34:01 by meatho        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import *
from queue import *

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

dir=[[] for _ in range(n+1)]

for _ in range(m):
    a,b,w=map(int,sys.stdin.readline().split())
    dir[a].append((b,w))

start, dest = map(int,sys.stdin.readline().split())

pq = PriorityQueue()
visited = [False]*(n+1)
weight = [sys.maxsize]*(n+1)
weight[start]=0
pq.put((0,start))

while not pq.empty():
    temp = pq.get()
    cur=temp[1]
    cur_weight=temp[0]
    
    if visited[cur]:
        continue
    visited[cur]=True
    if visited[dest]:
        break

    for i in dir[cur]:
        to = i[0]
        to_weight=i[1]

        if weight[to]>cur_weight+to_weight:
            weight[to]=cur_weight+to_weight
            pq.put((weight[to],to))


print(weight[dest])