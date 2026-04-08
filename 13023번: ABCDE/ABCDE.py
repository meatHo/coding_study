#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13023                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatho <boj.kr/u/meatho>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13023                          #+#        #+#      #+#     #
#    Solved: 2026/04/09 00:14:23 by meatho        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import *

n,m = map(int, sys.stdin.readline().split())

graph = defaultdict(list)
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

res = 0
visited = [False]*(n)

def dfs(cur,res):
    visited[cur]=True
    for i in graph[cur]:
        if not visited[i]:
            res+=1
            if res == 5:
                return True
            if dfs(i,res):
                return True

for i in range(n):
    if not i:
        temp = dfs(i,0)
        if temp:
            break
if temp:
    print(1)
else:
    print(0)

