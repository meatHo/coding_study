#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11659                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatHo <boj.kr/u/meatHo>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11659                          #+#        #+#      #+#     #
#    Solved: 2026/03/11 23:17:14 by meatHo        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import *
import sys

n, h=map(int,sys.stdin.readline().rstrip().split())
data = list(map(int,sys.stdin.readline().rstrip().split()))
guganhap=list()
temp = 0
guganhap.append(temp)
for i in data:
    temp+=i
    guganhap.append(temp)

for i in range(h):
    a, b=map(int,sys.stdin.readline().rstrip().split())
    print(guganhap[b]-guganhap[a-1])
