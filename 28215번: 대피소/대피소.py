#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 28215                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatho <boj.kr/u/meatho>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/28215                          #+#        #+#      #+#     #
#    Solved: 2026/04/08 21:03:49 by meatho        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import *
from itertools import combinations

n,k = map(int,sys.stdin.readline().split())

home = list()
for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    home.append((x,y))

res = sys.maxsize
for shelters in combinations(range(n),k):
    distance = 0
    for ho_x,ho_y in home:
        to_shelter=sys.maxsize
        for sh in shelters:
            sh_x=home[sh][0]
            sh_y=home[sh][1]
            to_shelter = min(to_shelter,abs(sh_x-ho_x)+abs(sh_y-ho_y))
        distance=max(distance,to_shelter)
    res = min(res,distance)

print(res)


# if k==1:
#     res=sys.maxsize
#     for sh_x,sh_y in home:
#         distance = 0
#         for ho_x,ho_y in home:
#             if sh_x==ho_x and sh_y==ho_y:
#                 continue
#             distance = max(distance, abs(sh_x-ho_x)+abs(sh_y-ho_y))
#         res = min(res, distance)
# if k==2:
#     res = sys.maxsize