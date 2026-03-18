#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2018                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatho <boj.kr/u/meatho>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2018                           #+#        #+#      #+#     #
#    Solved: 2026/03/18 13:37:23 by meatho        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import *

n = int(sys.stdin.readline().rstrip())


s=e=res = 0
sum=0
while e<n:
    if sum==n:
        res+=1
        e+=1
        sum += e

    elif sum>n:
        sum-=s
        s+=1
    else:
        e+=1
        sum += e

print(res+1)