#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1753                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatho <boj.kr/u/meatho>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1753                           #+#        #+#      #+#     #
#    Solved: 2026/04/06 13:01:45 by meatho        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import *
from queue import *

v,e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline().rstrip())

dir = [[] for _ in range(v+1)]
weight = [sys.maxsize]*(v+1)
for _ in range(e):
    a,b,w = map(int,sys.stdin.readline().split())
    dir[a].append((b,w))

pq = PriorityQueue()
pq.put((0,k))
visited = [False]*(v+1)
visited[0]=True
weight[k]=0

'''
1->2 10
1->3 2
3->2 9
시작점 1

visited[1] true
weight[2] 10
weight[3] 9
pq에 (10,2) (9,3) put

visited[3] true
weight[2] min(10,11) = 10 유지
'''


while not pq.empty():
    temp = pq.get()
    cur_weight = temp[0]
    cur = temp[1]
    if visited[cur]:
        continue
    visited[cur]=True


    for i in dir[cur]:
        to = i[0]
        to_weight=i[1]
        if  weight[to]>cur_weight + to_weight:
            weight[to]=cur_weight+to_weight
            pq.put((weight[to],to))

for i in range(1,v+1):
    if not visited[i]:
        print("INF")
    else:
        print(weight[i])
