#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1516                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatho <boj.kr/u/meatho>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1516                           #+#        #+#      #+#     #
#    Solved: 2026/04/01 23:42:42 by meatho        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import *

n= int(sys.stdin.readline().rstrip())
dir = [[] for _ in range(n+1)]
forward = [0]*(n+1)
time = [0]*(n+1)
res = [0]*(n+1)
for i in range(1,n+1):
    temp = list(map(int,sys.stdin.readline().rstrip().split()))
    time[i]=temp[0]
    length=len(temp)
    for j in range(1,length-1):
        forward[i]+=1
        dir[temp[j]].append(i)

dq = deque()
for i in range(1,n+1):
    if forward[i]==0:
        dq.append(i)
        res[i]=time[i]

while dq:
    temp=dq.popleft()
    temp_time = res[temp]
    for i in dir[temp]:
        forward[i]-=1
        res[i]=max(res[i],temp_time+time[i])
        # print("------------------")
        # print(f"temp {temp}, {res}")
        # print("------------------")
        if forward[i]==0:
            dq.append(i)

for i in range(1,n+1):
    print(res[i])
