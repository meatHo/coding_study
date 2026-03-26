#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1717                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatho <boj.kr/u/meatho>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1717                           #+#        #+#      #+#     #
#    Solved: 2026/03/26 23:05:40 by meatho        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import *

def find(a):
    if a != arr[a]:
        arr[a]=find(arr[a])
    return arr[a]

def union(a,b):
    keya = find(a)
    keyb = find(b)
    if keya!=keyb:
        arr[keya]= keyb



n,m=map(int,sys.stdin.readline().rstrip().split())

arr=[i for i in range(n+1)]

for _ in range(m):
    k,a,b=map(int,sys.stdin.readline().rstrip().split())
    if k==0:
        union(a,b)
    else:
        if find(a) != find(b):
            print("NO")
        else:
            print("YES")