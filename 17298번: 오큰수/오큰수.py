#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17298                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatho <boj.kr/u/meatho>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17298                          #+#        #+#      #+#     #
#    Solved: 2026/03/18 23:36:15 by meatho        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import *

n = int(sys.stdin.readline().rstrip())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
res = [0]*n

mystack=deque()
for i in range(n):
    while mystack and arr[mystack[-1]]<arr[i]:
        res[mystack.pop()]=arr[i]
    mystack.append(i)

while mystack:
    res[mystack.pop()]=-1

for i in res:
    print(i, end=" ")
