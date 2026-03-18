#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1253                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatho <boj.kr/u/meatho>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1253                           #+#        #+#      #+#     #
#    Solved: 2026/03/18 14:43:24 by meatho        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import *

n=int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()

res=0

for i in range(0,n):
    num = arr[i]
    s=0
    e=n-1
    while s<e:
        temp = arr[s]+arr[e]
        if temp==num:
            if s!=i and e!=i:
                res+=1
                break
            elif s==i:
                s+=1
            elif e==i:
                e-=1
        elif temp<num:
            s+=1
        else:
            e-=1
print(res)