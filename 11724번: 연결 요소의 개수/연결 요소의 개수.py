#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11724                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatho <boj.kr/u/meatho>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11724                          #+#        #+#      #+#     #
#    Solved: 2026/04/08 23:46:45 by meatho        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import *
sys.setrecursionlimit(10**6)
graph = defaultdict(list)
n,m=map(int,sys.stdin.readline().split())

for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)
res=0

def dfs(cur):
    visited[cur]=True
    for to in graph[cur]:
        if not visited[to]:
            dfs(to)

for i in range(1,n+1):
    if not visited[i]:
        res+=1
        dfs(i)

print(res)
