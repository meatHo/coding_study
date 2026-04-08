#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1219                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatho <boj.kr/u/meatho>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1219                           #+#        #+#      #+#     #
#    Solved: 2026/04/07 22:17:04 by meatho        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import *

n, start, dest, m = map(int,sys.stdin.readline().split())

dir = []
dir2 = [[]for _ in range(n)]
for i in range(m):
    dir.append(list(map(int,sys.stdin.readline().split())))
    dir2[dir[i][0]].append(dir[i][1])

earn = list(map(int,sys.stdin.readline().split()))

for i in range(m):
    dir[i][2]=dir[i][2]-earn[dir[i][1]]

weight = [sys.maxsize]*n
weight[start]=-earn[start]
cycle=list()
for i in range(n+1):
    for cur,to,w in dir:
        if weight[cur]!=sys.maxsize and weight[to]>weight[cur]+w:
            if i==n:
                cycle.append(cur)
            weight[to]=weight[cur]+w

cycle_to_dest = False


for i in cycle:
    dq = deque()
    visited=[False]*n
    dq.append(i)
    while dq:
        cur = dq.popleft()
        visited[cur]=True
        if cur == dest:
            cycle_to_dest=True
            break
        for j in dir2[cur]:
            if not visited[j]:
                dq.append(j)
    if cycle_to_dest:
        break



if weight[dest]==sys.maxsize:
    print("gg")
elif cycle_to_dest:
    print("Gee")
else:
    print(-weight[dest])
