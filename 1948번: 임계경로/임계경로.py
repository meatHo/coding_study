#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1948                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatho <boj.kr/u/meatho>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1948                           #+#        #+#      #+#     #
#    Solved: 2026/04/02 01:18:26 by meatho        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import *

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

# 1->(2,4),(3,2)
dir = [[] for _ in range(n+1)]
reverse_dir = [[] for _ in range(n+1)]

indegree = [0]*(n+1)
reverse_indegree = [0]*(n+1)

for _ in range(m):
    temp=list(map(int,sys.stdin.readline().rstrip().split()))
    dir[temp[0]].append((temp[1],temp[2]))
    reverse_dir[temp[1]].append((temp[0],temp[2]))
    indegree[temp[1]]+=1

dq = deque()

han,rome=map(int,sys.stdin.readline().rstrip().split())
time=[0]*(n+1)
road=0

dq.append(han)

while dq:
    cur = dq.popleft()
    
    for i in dir[cur]:
        cost = i[1]
        to = i[0]
        time[to]=max(time[to],time[cur]+cost)
        indegree[to]-=1
        if indegree[to]==0:
            dq.append(to)

max_time = max(time)
path = 0

visited = [False]*(n+1)
dq.append(rome)

while dq:
    cur = dq.popleft()
    for i in reverse_dir[cur]:
        cost = i[1]
        to = i[0]
        if time[to]+cost==time[cur]:
            path+=1
            if not visited[to]:
                dq.append(to)
                visited[to]=True

print(max_time)
print(path)