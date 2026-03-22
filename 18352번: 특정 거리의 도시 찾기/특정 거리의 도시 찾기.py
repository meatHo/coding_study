#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 18352                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatho <boj.kr/u/meatho>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/18352                          #+#        #+#      #+#     #
#    Solved: 2026/03/22 22:19:10 by meatho        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import *

n,m,k,x=map(int,sys.stdin.readline().rstrip().split())
dir = [[]for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    dir[a].append(b)

dq=deque()
visited=[-1]*(n+1)
visited[x]+=1
dq.append(x)
while dq:
    current=dq.popleft()
    for i in dir[current]:
        if(visited[i]==-1):
            visited[i]=visited[current]+1
            dq.append(i)
answer=list()
for i in range(1,n+1):
    if visited[i]==k:
        answer.append(i)

if answer:
    answer.sort()
    for i in answer:
        print(i)
else:
    print(-1)
