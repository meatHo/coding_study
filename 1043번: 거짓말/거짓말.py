#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1043                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatho <boj.kr/u/meatho>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1043                           #+#        #+#      #+#     #
#    Solved: 2026/03/30 21:39:53 by meatho        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import *

def find(a):
    if a!=parent[a]:
        parent[a]=find(parent[a])
    return parent[a]

def union(a,b):
    parent_a = find(a)
    parent_b = find(b)
    if parent_a != parent_b:
        parent[parent_b]=parent[parent_a]

sys.setrecursionlimit(10**6)

n,m=map(int,sys.stdin.readline().rstrip().split())
known=list(map(int,sys.stdin.readline().rstrip().split()))
del known[0]

parent=[i for i in range(n+1)]

res=0

party=[]
for j in range(m):
    temp=list(map(int,sys.stdin.readline().rstrip().split()))
    for i in range(1,len(temp)):
        union(temp[1],temp[i])
    party.append(temp[1])

for i in party:
    temp_parent = find(i)
    boo = False
    for j in known:
        if temp_parent==find(j):
            boo=True
            break
    if not boo:
        res+=1


print(res)


