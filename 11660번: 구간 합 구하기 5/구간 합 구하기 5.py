#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11660                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatHo <boj.kr/u/meatHo>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11660                          #+#        #+#      #+#     #
#    Solved: 2026/03/17 00:15:03 by meatHo        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import *

n,m = map(int, sys.stdin.readline().rstrip().split())
n+=1
temp = [[0]*n]
sum_arr = [[0]*n for _ in range(n)]

for _ in range(n-1):
    temp_row = [0]+ list(map(int,sys.stdin.readline().rstrip().split()))
    temp.append(temp_row)

for i in range(1,n):
    for j in range(1,n):
        sum_arr[i][j]=sum_arr[i-1][j]+sum_arr[i][j-1]-sum_arr[i-1][j-1]+temp[i][j]

for i in range(m):
    x1,y1,x2,y2=map(int,sys.stdin.readline().rstrip().split())
    print(sum_arr[x2][y2]+sum_arr[x1-1][y1-1]-sum_arr[x1-1][y2]-sum_arr[x2][y1-1])