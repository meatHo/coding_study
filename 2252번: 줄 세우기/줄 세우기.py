#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2252                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatho <boj.kr/u/meatho>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2252                           #+#        #+#      #+#     #
#    Solved: 2026/03/30 22:31:03 by meatho        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import *

n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[0]*(n+1)
dir=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    dir[a].append(b)
    arr[b]+=1
dq = deque()
for i in range(1,n+1):
    if arr[i]==0:
        dq.append(i)

while dq:
    temp = dq.popleft()
    print(temp, end=" ")
    for i in dir[temp]:
        arr[i]-=1
        if arr[i]==0:
            dq.append(i)
            
