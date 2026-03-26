#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1976                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatho <boj.kr/u/meatho>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1976                           #+#        #+#      #+#     #
#    Solved: 2026/03/26 23:42:17 by meatho        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import *

def find(a):
    if a!=arr[a]:
        arr[a]=find(arr[a])
    return arr[a]

def union(a,b):
    keya=find(a)
    keyb=find(b)
    if keya!=keyb:
        arr[keya]=keyb

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

res = set()
sys.setrecursionlimit(10**6)

arr = [i for i in range(201)]
for i in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    for j in range(i):
        if temp[j]==1:
            #j+1 i+1
            union(j+1,i+1)

temp = list(map(int,sys.stdin.readline().split()))
for i in temp:
    res.add(find(i))
if len(res)==1:
    print("YES")
else:
    print("NO")


'''
a-b
z-b
v-p-b
'''
