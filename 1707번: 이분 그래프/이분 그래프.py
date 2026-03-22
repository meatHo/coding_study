#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1707                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatho <boj.kr/u/meatho>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1707                           #+#        #+#      #+#     #
#    Solved: 2026/03/22 23:43:48 by meatho        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import *

def bfs(root):
    dq=deque()
    dq.append(root)
    while dq:
        cur=dq.popleft()
        for i in dir[cur]:
            if visited[i]==0:
                visited[i] = 1 if visited[cur]==-1 else -1
                dq.append(i)
            elif visited[i]==visited[cur]:
                return False
    return True


k=int(sys.stdin.readline().rstrip())
for _ in range(k):
    v,e=map(int,sys.stdin.readline().rstrip().split())
    dir = [[] for _ in range(v+1)]
    for _ in range(e):
        a,b = map(int,sys.stdin.readline().rstrip().split())
        dir[a].append(b)
        dir[b].append(a)
    visited=[0]*(v+1)
    dq=deque()
    dq.append(1)

    ans = False
    for i in range(1,v+1):
        if visited[i]==0:
            if not bfs(i):
                ans = True
                break
    print("NO" if ans else "YES")
