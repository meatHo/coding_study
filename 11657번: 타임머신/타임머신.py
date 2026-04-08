#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11657                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatho <boj.kr/u/meatho>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11657                          #+#        #+#      #+#     #
#    Solved: 2026/04/07 14:57:22 by meatho        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import *

n,m=map(int,sys.stdin.readline().split())
dir = list()
for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    dir.append((a,b,c))


start = 1

weight = [sys.maxsize]*(n+1)
weight[start]=0

cycle = False
for i in range(1,n+1):
    for cur,to,w in dir:
        
        if weight[cur] != sys.maxsize and weight[to]>weight[cur]+w:
            if i==n:
                cycle=True
                break
            weight[to]=weight[cur]+w
    if cycle:
        break

if cycle:
    print(-1)
else:
    for i in range(2,n+1):
        if weight[i]==sys.maxsize:
            print(-1)
        else:
            print(weight[i])



# for cur in range(1,n+1):
#     if weight[cur]==sys.maxsize:
#         continue
#     for to,to_weight in dir[cur]:
#         if weight[to]>weight[cur]+to_weight:
#             weight[to]=weight[cur]+to_weight

# cycle = False
# for cur in range(1,n+1):
#     if weight[cur]==sys.maxsize:
#         continue
#     for to,to_weight in dir[cur]:
#         if weight[to]>weight[cur]+to_weight:
#             cycle=True
#             break
#     if  cycle:
#         break
# if cycle:
#     print(-1)
# else:
#     for i in range(2,n+1):
#         if weight[i]==sys.maxsize:
#             print(-1)
#         else:
#             print(weight[i])
